"""Selected documents affect source validation, assembly, builds and receipts."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from story_factory import package_options as options

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('selected_checks',ROOT/'story_factory/story_check.py')
checks=importlib.util.module_from_spec(spec);spec.loader.exec_module(checks)


class PackageSelectionTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name).resolve()/'project'
        result=subprocess.run([sys.executable,str(ROOT/'story_factory/new_story.py'),str(self.root),'--title','A Different Story','--no-skills'],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
    def select(self,**changes):
        data=options.defaults();data.update(changes)
        (self.root/'development/package_options.json').write_text(json.dumps(data))
        return data
    def finish_metadata(self):
        path=self.root/'common/metadata.tex'
        path.write_text(path.read_text().replace('DRAFT PLACEHOLDER -- replace before delivery.','An archivist risks her job to save a disappearing recording.').replace('To be developed','Drama'))
    def test_full_default_matches_all_original_deliverables(self):
        self.assertEqual(options.load(self.root),options.defaults())
        self.assertEqual(len(options.output_names(options.defaults())),18)
        self.assertEqual(len(options.defaults()['sections']),15)
        self.assertEqual(len(options.defaults()['pitches']),16)
    def test_unselected_blank_templates_do_not_block_selected_pitch(self):
        self.select(screenplay=False,sections=[],pitches=['actor_pitch'])
        self.finish_metadata()
        path=self.root/'one_pagers/actor_pitch.tex'
        path.write_text(path.read_text().replace('DRAFT PLACEHOLDER -- replace before delivery.','A difficult part built around one irreversible choice.'))
        self.assertEqual(checks.source_problems(self.root),[])
        self.assertIn('DRAFT PLACEHOLDER',(self.root/'package/treatment.tex').read_text())
        path.write_text(path.read_text()+'\nTODO\n')
        self.assertIn('Unwritten content: one_pagers/actor_pitch.tex',checks.source_problems(self.root))
    def test_invalid_empty_duplicate_and_unknown_selections_rejected(self):
        for data in [dict(screenplay=False,sections=[],pitches=[]),dict(screenplay=True,sections=['nonexistent'],pitches=[]),dict(screenplay=True,sections=[],pitches=['actor_pitch','actor_pitch']),dict(screenplay='yes',sections=[],pitches=[])]:
            with self.assertRaises(ValueError):options.validate(data)
    def test_selected_wrapper_preserves_cover_and_omits_unrequested_sections(self):
        data=self.select(screenplay=False,sections=['treatment','budget_and_scope'],pitches=[])
        entry=options.package_entry(self.root,data,write=True)
        text=entry.read_text()
        self.assertIn('\\tableofcontents',text)
        self.assertIn('\\input{treatment}',text)
        self.assertIn('\\input{budget_and_scope}',text)
        self.assertNotIn('\\input{casting_notes}',text)
        self.assertTrue(text.endswith('\\end{document}\n'))
        self.assertIn('\\input{casting_notes}',(self.root/'package/studio_package.tex').read_text())
    def test_selection_change_invalidates_build_receipt(self):
        self.select(screenplay=False,sections=[],pitches=['actor_pitch'])
        out=self.root/'output';out.mkdir()
        pdf=out/'actor-pitch.pdf';pdf.write_bytes(b'%PDF selected test fixture')
        import hashlib
        receipt={'source_sha256':checks.print_fingerprint(self.root),'outputs':{'actor-pitch.pdf':{'pages':1,'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest()}}}
        (self.root/'development/build.json').write_text(json.dumps(receipt))
        self.assertEqual(checks.build_problems(self.root),[])
        self.select(screenplay=False,sections=[],pitches=['director_pitch'])
        errors=checks.build_problems(self.root)
        self.assertIn('Print sources changed since the build',errors)
        self.assertIn('Build receipt does not match selected documents',errors)
    def test_build_calls_only_selected_make_target_and_measures_pdf(self):
        self.select(screenplay=False,sections=[],pitches=['actor_pitch']);self.finish_metadata()
        path=self.root/'one_pagers/actor_pitch.tex';path.write_text(path.read_text().replace('DRAFT PLACEHOLDER -- replace before delivery.','An actor faces a difficult choice.'))
        def fake_make(command,**kwargs):
            self.assertEqual(command,['make','-B','output/actor-pitch.pdf'])
            (self.root/'output').mkdir();(self.root/'output/actor-pitch.pdf').write_bytes(b'%PDF fixture')
        with patch.object(checks.shutil,'which',return_value='/usr/bin/pdfinfo'),patch.object(checks.subprocess,'run',side_effect=fake_make),patch.object(checks.subprocess,'check_output',return_value='Pages: 1\n'):
            checks.build(self.root)
        self.assertEqual(checks.build_problems(self.root),[])
    def test_workflow_package_checks_only_requested_sources_and_hashes_selection(self):
        self.select(screenplay=False,sections=[],pitches=['actor_pitch'])
        (self.root/'one_pagers/actor_pitch.tex').write_text('An archivist confronts the person who destroyed her recording. '*5)
        (self.root/'development/package_review.md').write_text('Reviewed the actor pitch against the story brief and avoided unsupported attachment claims.\nVerdict: PASS\n')
        code='import json,sys;from pathlib import Path;sys.path.insert(0,str(Path(sys.argv[1])/"scripts"));import workflow;workflow.ROOT=Path(sys.argv[1]);print(json.dumps(workflow.artifacts("package")))'
        result=subprocess.run([sys.executable,'-c',code,str(self.root)],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        files,errors=json.loads(result.stdout)
        self.assertEqual(errors,[])
        self.assertEqual(set(files),{'one_pagers/actor_pitch.tex','development/package_review.md','development/package_options.json'})
        self.select(screenplay=True,sections=[],pitches=['actor_pitch'])
        changed=subprocess.run([sys.executable,'-c',code,str(self.root)],capture_output=True,text=True)
        self.assertNotEqual(files,json.loads(changed.stdout)[0])
