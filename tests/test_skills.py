"""Behavioral contracts for portable dual-host skills and evidence controls."""
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('checks',ROOT/'story_factory/story_check.py')
checks=importlib.util.module_from_spec(spec);spec.loader.exec_module(checks)


class SkillTests(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.root=Path(self.temp.name)
 def install(self,*extra):
  return subprocess.run([sys.executable,str(ROOT/'install.py'),'--project',str(self.root/'project'),*extra],capture_output=True,text=True)
 def test_host_entries_and_references_are_discoverable(self):
  catalog=json.loads((ROOT/'COMMANDS.json').read_text());self.assertEqual(len(catalog),21)
  for item in catalog:
   folder=ROOT/'skills'/item['name'];text=(folder/'SKILL.md').read_text()
   self.assertIn(f"name: {item['name']}\n",text)
   for relative in re.findall(r'\]\(([^)]+)\)',text):self.assertTrue((folder/relative).is_file(),relative)
   self.assertIn('$'+item['name'],(folder/'agents/openai.yaml').read_text())
 def test_both_hosts_install_portable_shared_guidance(self):
  result=self.install();self.assertEqual(result.returncode,0,result.stderr)
  project=self.root/'project'
  for item in json.loads((ROOT/'COMMANDS.json').read_text()):
   claude=project/'.claude/skills'/item['name']/'SKILL.md';codex=project/'.agents/skills'/item['name']/'SKILL.md'
   self.assertEqual(claude.read_bytes(),codex.read_bytes())
  for host in ['.claude','.agents']:
   toolkit=project/host/'skills/story/toolkit'
   self.assertTrue((toolkit/'skills/story/references/original-creative-brief.md').is_file())
   self.assertTrue((toolkit/'skills/story/references/RESEARCH.md').is_file())
   self.assertFalse((toolkit/'.git').exists())
  self.assertEqual(self.install('--check').returncode,0)
 def test_conflict_is_detected_before_any_other_host_is_written(self):
  foreign=self.root/'project/.agents/skills/story';foreign.mkdir(parents=True);(foreign/'SKILL.md').write_text('My own skill')
  result=self.install();self.assertNotEqual(result.returncode,0)
  self.assertFalse((self.root/'project/.claude').exists())
  self.assertEqual((foreign/'SKILL.md').read_text(),'My own skill')
 def test_local_edits_are_preserved(self):
  self.assertEqual(self.install('--host','claude').returncode,0)
  path=self.root/'project/.claude/skills/story-draft/SKILL.md';path.write_text('My edited skill')
  result=self.install('--host','claude');self.assertNotEqual(result.returncode,0)
  self.assertEqual(path.read_text(),'My edited skill')
 def test_cache_files_do_not_block_an_owned_reinstall(self):
  self.assertEqual(self.install('--host','codex').returncode,0)
  path=self.root/'project/.agents/skills/story/toolkit/story_factory/__pycache__';path.mkdir();(path/'x.pyc').write_bytes(b'cache')
  self.assertEqual(self.install('--host','codex').returncode,0)
 def test_installed_exporter_outlives_its_source_and_preserves_preamble(self):
  source=self.root/'source';source.mkdir()
  for name in ['Makefile','latexmkrc','.gitignore','install.py','COMMANDS.json','MASTER_PROMPT.md','WORKFLOW.md','WRITING_GUIDE.md']:shutil.copyfile(ROOT/name,source/name)
  for name in ['story_factory','common','fonts','screenplay','package','one_pagers','skills','examples']:
   shutil.copytree(ROOT/name,source/name,ignore=shutil.ignore_patterns('__pycache__','*.pyc','toolkit'))
  destination=self.root/'project'
  result=subprocess.run([sys.executable,str(source/'install.py'),'--project',str(destination),'--host','codex'],capture_output=True,text=True)
  self.assertEqual(result.returncode,0,result.stderr);shutil.rmtree(source)
  script=destination/'.agents/skills/story/toolkit/story_factory/new_story.py';child=self.root/'A fresh story & more'
  result=subprocess.run([sys.executable,str(script),str(child),'--title','A & B','--source-mode','inspired-by','--no-skills'],capture_output=True,text=True)
  self.assertEqual(result.returncode,0,result.stderr)
  preamble=(child/'common/preamble.tex').read_text()
  self.assertEqual(preamble.count('\\input{../common/metadata}'),1)
  self.assertIn('\\input{../common/colors}',preamble);self.assertIn('\\hypersetup',preamble)
  self.assertEqual(json.loads((child/'research/source_mode.json').read_text())['mode'],'inspired-by')
  result=subprocess.run([sys.executable,str(child/'scripts/workflow.py'),'status'],capture_output=True,text=True)
  self.assertIn('research: pending',result.stdout)
 def test_quality_receipts_are_specific_to_draft_and_requested_target(self):
  root=self.root;(root/'screenplay').mkdir();(root/'development').mkdir()
  script=root/'screenplay/act1.tex';script.write_text('A first version with named women and actual dialogue.')
  fingerprint=checks.draft_fingerprint(root)
  quality={'draft_sha256':fingerprint,'coverage':'full-draft','verdict':'READY','summary':'Concrete editorial findings reviewed.'}
  bechdel={'draft_sha256':fingerprint,'coverage':'full-draft','status':'FAIL','summary':'The complete draft has no qualifying conversation.','evidence':[]}
  (root/'development/quality.json').write_text(json.dumps(quality));(root/'development/bechdel.json').write_text(json.dumps(bechdel))
  self.assertEqual(checks.quality_problems(root),[])
  (root/'development/preferences.json').write_text('{"bechdel_target":"pass"}')
  self.assertTrue(any('requested a Bechdel pass' in p for p in checks.quality_problems(root)))
  script.write_text(script.read_text()+' Changed scene.')
  self.assertTrue(any('Stale' in p for p in checks.quality_problems(root)))
 def test_nested_scene_edits_invalidate_quality_and_truth_fingerprints(self):
  root=self.root;(root/'screenplay/scenes').mkdir(parents=True)
  (root/'screenplay/main_screenplay.tex').write_text(r'\input{scenes/opening}')
  scene=root/'screenplay/scenes/opening.tex';scene.write_text('An archivist makes an irreversible decision.')
  old=checks.draft_fingerprint(root)
  scene.write_text('The archivist avoids making that decision.')
  self.assertNotEqual(old,checks.draft_fingerprint(root))
 def test_bechdel_pass_needs_two_distinct_named_women(self):
  root=self.root;(root/'screenplay').mkdir();(root/'development').mkdir()
  (root/'screenplay/act1.tex').write_text('A woman speaks to herself about the damaged recording.')
  fingerprint=checks.draft_fingerprint(root)
  quality={'draft_sha256':fingerprint,'coverage':'full-draft','verdict':'READY','summary':'Reviewed the actual complete draft.'}
  bechdel={'draft_sha256':fingerprint,'coverage':'full-draft','status':'PASS','summary':'Supposed qualifying exchange.','evidence':[{'women':['Mara','Mara'],'scene_id':'S1','exchange':'Mara speaks twice.','non_man_topic':'The recording'}]}
  (root/'development/quality.json').write_text(json.dumps(quality));(root/'development/bechdel.json').write_text(json.dumps(bechdel))
  self.assertTrue(any('two named women' in p for p in checks.quality_problems(root)))
 def test_writer_page_cap_rejects_overrun_and_invalid_limit(self):
  folder=self.root/'development';folder.mkdir()
  prefs=folder/'preferences.json'
  prefs.write_text(json.dumps({'screenplay_max_pages':3}))
  self.assertTrue(checks.output_limit_problems(self.root,{'screenplay.pdf':{'pages':5}}))
  self.assertEqual(checks.output_limit_problems(self.root,{'screenplay.pdf':{'pages':3}}),[])
  prefs.write_text(json.dumps({'screenplay_max_pages':True}))
  self.assertTrue(checks.output_limit_problems(self.root,{'screenplay.pdf':{'pages':1}}))
 def test_verified_claims_cannot_use_missing_or_synthetic_sources(self):
  root=self.root;(root/'research').mkdir()
  (root/'research/source_mode.json').write_text('{"mode":"based-on"}')
  (root/'research/truth_report.md').write_text('Concept review only, not legal clearance.')
  data={'sources':[],'claims':[{'id':'C1','text':'A claimed event','status':'verified','source_ids':['S1']}]}
  (root/'research/claims.json').write_text(json.dumps(data))
  problems=checks.truth_problems(root);self.assertTrue(any('missing source' in p for p in problems));self.assertTrue(any('no source' in p for p in problems))
  data['sources']=[{'id':'S1','url':'https://example.invalid/source','title':'Synthetic','accessed':'2026-10-20','locator':'page 1'}]
  (root/'research/claims.json').write_text(json.dumps(data));self.assertTrue(any('usable citation' in p for p in checks.truth_problems(root)))
  self.assertTrue(any('full-draft' in p for p in checks.truth_problems(root,require_draft=True)))


if __name__=='__main__':unittest.main()
