"""The archive preserves source and excludes private/generated files; not a secret classifier."""
import importlib.util,tempfile,unittest,zipfile,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('release',ROOT/'scripts/release_bundle.py');release=importlib.util.module_from_spec(spec);spec.loader.exec_module(release)
class ReleaseTests(unittest.TestCase):
 def test_archive_is_versioned_and_excludes_private_and_runtime_material(self):
  with tempfile.TemporaryDirectory() as name:
   root=Path(name)/'source';root.mkdir()
   for path in ['VERSION','README.md','skills/story/SKILL.md','examples/demo/output/secret.pdf','research/private/interview.txt','development/private/letter.txt','.context/events.json','skills/story/toolkit/old.txt','examples/demo/pdfs/reviewed.pdf']:
    target=root/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_text('0.2.0-preview.1' if path=='VERSION' else 'fixture')
   (root/'README-link.md').symlink_to(root/'README.md')
   archive=release.build(root,Path(name)/'out')
   with zipfile.ZipFile(archive) as z:
    files=z.namelist();self.assertTrue(any(x.endswith('/skills/story/SKILL.md') for x in files));self.assertTrue(any(x.endswith('/pdfs/reviewed.pdf') for x in files))
    self.assertFalse(any(any(part in {'private','.context','output','toolkit'} for part in Path(x).parts) for x in files))
    manifest=json.loads(z.read('story-factory-0.2.0-preview.1/RELEASE_MANIFEST.json'));self.assertEqual(manifest['version'],'0.2.0-preview.1')
   self.assertTrue(Path(str(archive)+'.sha256').is_file())
   with self.assertRaisesRegex(ValueError,'already exists'):release.build(root,Path(name)/'out')
if __name__=='__main__':unittest.main()
