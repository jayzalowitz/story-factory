import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock
import zipfile

ROOT = Path(__file__).resolve().parents[1]

def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'story_factory' / (name + '.py'))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result

reader = module('import_source')
doctor = module('setup_check')

class SourceImportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.project = self.root / 'project'
    def tearDown(self): self.temp.cleanup()
    def write(self, name, data):
        path = self.root / name
        path.write_bytes(data)
        return path
    def test_text_preserves_source_and_repeated_imports_and_locations(self):
        data = 'INT. CAFÉ — NIGHT\nMARA\nThe meter’s running.\n'.encode()
        source = self.write('My draft.fountain', data)
        folder, manifest = reader.import_source(source, self.project)
        again, _ = reader.import_source(source, self.project)
        self.assertNotEqual(folder, again)
        self.assertEqual(source.read_bytes(), data)
        self.assertEqual((folder / 'original.fountain').read_bytes(), data)
        payload = json.loads((folder / 'segments.json').read_text())
        self.assertEqual(payload['segments'][2]['location'], 'line 3')
        self.assertEqual(manifest['source_sha256'], reader.digest(data))
        self.assertEqual(manifest['reading_completeness'], 'not yet checked against original')
        self.assertEqual(folder.stat().st_mode & 0o777, 0o700)
    def test_fdx_content_not_title_page_and_types(self):
        data = b'<FinalDraft><Content><Paragraph Type="Scene Heading"><Text>INT. SHOP</Text></Paragraph><Paragraph Type="Dialogue"><Text>Not </Text><Text>yet.</Text></Paragraph></Content><TitlePage><Paragraph><Text>Private title</Text></Paragraph></TitlePage></FinalDraft>'
        folder, _ = reader.import_source(self.write('draft.fdx', data), self.project)
        text = (folder / 'reading.txt').read_text()
        self.assertIn('[paragraph 2: Dialogue]\nNot yet.', text)
        self.assertNotIn('Private title', text)
    def test_fdx_entities_and_utf16_rejected(self):
        attack = '<!DOCTYPE FinalDraft [<!ENTITY x "bad">]><FinalDraft><Content><Paragraph><Text>&x;</Text></Paragraph></Content></FinalDraft>'
        for data in [attack.encode(), attack.encode('utf-16')]:
            with self.assertRaises(ValueError):
                reader.import_source(self.write('bad.fdx', data), self.project)
        self.assertFalse((self.project / 'sources').exists())
    def docx(self, body):
        target = io.BytesIO()
        with zipfile.ZipFile(target, 'w') as archive: archive.writestr('word/document.xml', body)
        return target.getvalue()
    def test_docx_tables_unicode_and_limitations(self):
        data = self.docx('<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:r><w:t>Élan</w:t><w:tab/><w:t>two</w:t></w:r></w:p><w:tbl><w:tr><w:tc><w:p><w:r><w:t>Cell</w:t></w:r></w:p></w:tc></w:tr></w:tbl></w:body></w:document>')
        folder, report = reader.import_source(self.write('book.docx', data), self.project, 'adaptation')
        self.assertIn('Élan\ttwo', (folder / 'reading.txt').read_text())
        self.assertIn('body paragraph 2', (folder / 'reading.txt').read_text())
        self.assertIn('permission', report['next_step'])
        self.assertTrue(any('footnotes' in item for item in report['warnings']))
    def test_bad_docx_and_oversized_archive_rejected(self):
        with self.assertRaises(ValueError): reader.extract(b'not a zip', 'docx', None)
        with mock.patch.object(reader, 'MAX_SOURCE', 20):
            with self.assertRaises(ValueError): reader.extract(self.docx('<document>' + 'x' * 30 + '</document>'), 'docx', None)
    def test_pdf_page_locations_and_blank_page_warning(self):
        def fake_run(command, **kwargs):
            Path(command[-1]).write_text('Page one\f\fThird page\f')
            return mock.Mock(returncode=0)
        with mock.patch.object(reader.shutil, 'which', return_value='/observed/pdftotext'), mock.patch.object(reader.subprocess, 'run', side_effect=fake_run):
            folder, report = reader.import_source(self.write('text.pdf', b'%PDF fixture'), self.project)
        data = json.loads((folder / 'segments.json').read_text())
        self.assertEqual(data['segments'][2]['location'], 'PDF page 3')
        self.assertTrue(any('PDF page 2' in text for text in report['warnings']))
    def test_scanned_pdf_never_claims_readable(self):
        def fake_run(command, **kwargs):
            Path(command[-1]).write_text('\f\f')
            return mock.Mock(returncode=0)
        with mock.patch.object(reader.shutil, 'which', return_value='/observed/pdftotext'), mock.patch.object(reader.subprocess, 'run', side_effect=fake_run):
            _, report = reader.import_source(self.write('scan.pdf', b'%PDF fixture'), self.project)
        self.assertEqual(report['status'], 'needs_ocr_or_text_copy')
        self.assertIn('not yet checked', report['reading_completeness'])
    def test_no_pdf_tool_stops_without_an_import(self):
        with mock.patch.object(reader.shutil, 'which', return_value=None):
            with self.assertRaisesRegex(ValueError, 'No OCR'): reader.import_source(self.write('scan.pdf', b'%PDF'), self.project)
        self.assertFalse((self.project / 'sources').exists())
    def test_symlink_private_directory_rejected(self):
        (self.project / 'sources').mkdir(parents=True)
        (self.project / 'sources/private').symlink_to(self.root, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'symbolic link'): reader.import_source(self.write('x.txt', b'text'), self.project)
    def test_mirrors_match(self):
        for name in ['import_source.py', 'setup_check.py']:
            self.assertEqual((ROOT / 'scripts' / name).read_bytes(), (ROOT / 'story_factory' / name).read_bytes())

class SetupTests(unittest.TestCase):
    def test_observed_tools_do_not_imply_activation(self):
        with tempfile.TemporaryDirectory() as folder:
            entry = Path(folder) / '.agents/skills/story/SKILL.md'
            entry.parent.mkdir(parents=True)
            entry.write_text('installed')
            with mock.patch.object(doctor.shutil, 'which', return_value='/fake/program'):
                report = doctor.inspect_setup(folder)
        self.assertTrue(report['pdf_build_ready'])
        self.assertTrue(report['hosts']['codex']['project_skill_files_present'])
        self.assertEqual(report['hosts']['codex']['native_activation'], 'not tested')
        self.assertEqual(report['hosts']['codex']['account_and_usage'], 'not checked')
    def test_tectonic_fallback_matches_makefile(self):
        with mock.patch.object(doctor.shutil, 'which', side_effect=lambda name: '/fake/' + name if name in ('make', 'pdfinfo', 'tectonic') else None):
            self.assertTrue(doctor.inspect_setup('.')['pdf_build_ready'])
        with mock.patch.object(doctor.shutil, 'which', side_effect=lambda name: '/fake/' + name if name in ('make', 'pdfinfo', 'tectonic', 'latexmk') else None):
            self.assertFalse(doctor.inspect_setup('.')['pdf_build_ready'])
    def test_missing_tools_have_recovery_without_blocking_writing(self):
        with mock.patch.object(doctor.shutil, 'which', return_value=None):
            report = doctor.inspect_setup('.')
        self.assertFalse(report['pdf_build_ready'])
        self.assertTrue(any('Writing and reviewing can continue' in text for text in report['issues']))

if __name__ == '__main__': unittest.main()
