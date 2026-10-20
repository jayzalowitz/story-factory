"""Upgrades preserve writing and reject unowned/edited helpers before modifying anything."""
import importlib.util,tempfile,unittest,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('upgrade',ROOT/'story_factory/upgrade_project.py');upgrade=importlib.util.module_from_spec(spec);spec.loader.exec_module(upgrade)
class UpgradeTests(unittest.TestCase):
 def test_new_helpers_added_without_touching_manuscript_then_owned_refresh(self):
  with tempfile.TemporaryDirectory() as temp:
   root=Path(temp);(root/'screenplay').mkdir();draft=root/'screenplay/act1.tex';draft.write_text('My actual writing')
   count=upgrade.upgrade(root,ROOT/'story_factory');self.assertEqual(count,len(upgrade.HELPERS));self.assertEqual(draft.read_text(),'My actual writing')
   self.assertEqual(upgrade.upgrade(root,ROOT/'story_factory'),count)
 def test_local_edit_blocks_before_other_helper_added(self):
  with tempfile.TemporaryDirectory() as temp:
   root=Path(temp);(root/'scripts').mkdir();(root/'scripts/workflow.py').write_text('my custom workflow')
   with self.assertRaisesRegex(ValueError,'modified or unowned'):upgrade.upgrade(root,ROOT/'story_factory')
   self.assertFalse((root/'scripts/delivery.py').exists());self.assertEqual((root/'scripts/workflow.py').read_text(),'my custom workflow')
 def test_symlinked_ownership_record_never_overwrites_other_file(self):
  with tempfile.TemporaryDirectory() as temp:
   root=Path(temp);outside=root/'manuscript.txt';outside.write_text('My writing')
   (root/'.story-factory-tools.json').symlink_to(outside)
   with self.assertRaisesRegex(ValueError,'symlinked ownership'):upgrade.upgrade(root,ROOT/'story_factory')
   self.assertEqual(outside.read_text(),'My writing');self.assertFalse((root/'scripts').exists())
 def test_old_installed_toolkit_can_establish_ownership(self):
  with tempfile.TemporaryDirectory() as temp:
   root=Path(temp);(root/'scripts').mkdir();old=root/'.agents/skills/story/toolkit/story_factory';old.mkdir(parents=True)
   for p in [old/'workflow.py',root/'scripts/workflow.py']:p.write_text('old toolkit workflow')
   upgrade.upgrade(root,ROOT/'story_factory');self.assertEqual((root/'scripts/workflow.py').read_bytes(),(ROOT/'story_factory/workflow.py').read_bytes())
if __name__=='__main__':unittest.main()
