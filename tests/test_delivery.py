"""Delivery checks protect selection/isolation/currency, not artistic judgment or real viewing."""
import importlib.util,json,hashlib,sys,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'story_factory'))
import delivery

class DeliveryTests(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.root=Path(self.temp.name)/'project'
  for folder in ['development','screenplay','fonts','output','one_pagers','sources/private']:(self.root/folder).mkdir(parents=True)
  for name,content in {'Makefile':'all:\n\ttrue\n','latexmkrc':'# local configuration','screenplay/main_screenplay.tex':'\\input{act1}','screenplay/act1.tex':'Actual original scenes.','one_pagers/actor_pitch.tex':'Actual actor pitch.','fonts/local.ttf':'font fixture','sources/private/book.txt':'PRIVATE ORIGINAL'}.items():(self.root/name).write_text(content)
  options={'screenplay':True,'sections':[],'pitches':['actor_pitch']};(self.root/'development/package_options.json').write_text(json.dumps(options))
  self.records={}
  for name,pages in [('screenplay',2),('actor-pitch',1)]:
   data=('%PDF fixture '+name).encode();(self.root/'output'/f'{name}.pdf').write_bytes(data)
   self.records[name+'.pdf']={'pages':pages,'sha256':hashlib.sha256(data).hexdigest()}
  (self.root/'output/unselected.pdf').write_text('should not be delivered')
  (self.root/'development/build.json').write_text(json.dumps({'outputs':self.records}))
  self.visual={'outputs':{name:{'sha256':record['sha256'],'pages_inspected':list(range(1,record['pages']+1)),'verdict':'PASS','observations':'Fixture declaration; no real PDF layout claim.'} for name,record in self.records.items()}}
  self.save_visual()
 def save_visual(self):(self.root/'development/visual_review.json').write_text(json.dumps(self.visual))
 def prepare(self,destination=None):
  # Existing review/build validators are exercised elsewhere; isolate file preparation here.
  with patch.object(delivery,'build_problems',return_value=[]),patch.object(delivery,'quality_problems',return_value=[]),patch.object(delivery,'truth_problems',return_value=[]):return delivery.prepare(self.root,destination)
 def test_only_selected_files_delivered_private_original_excluded(self):
  result=self.prepare()
  self.assertEqual({p.name for p in (result/'pdfs').iterdir()},{'screenplay.pdf','actor-pitch.pdf'})
  self.assertFalse((result/'editable/sources').exists())
  self.assertEqual((result/'editable/screenplay/act1.tex').read_text(),'Actual original scenes.')
  manifest=json.loads((result/'manifest.json').read_text());self.assertEqual(manifest['files']['pdfs/screenplay.pdf']['pages'],2)
 def test_missing_or_stale_visual_review_blocks_delivery(self):
  self.visual['outputs']['screenplay.pdf']['sha256']='older-draft';self.save_visual()
  with self.assertRaisesRegex(ValueError,'stale'):self.prepare()
 def test_partial_page_inspection_blocks_delivery(self):
  self.visual['outputs']['screenplay.pdf']['pages_inspected']=[1];self.save_visual()
  with self.assertRaisesRegex(ValueError,'every delivered page'):self.prepare()
 def test_prior_delivery_never_overwritten(self):
  dest=self.root/'delivery/first';dest.mkdir(parents=True);(dest/'KEEP').write_text('my copy')
  with self.assertRaisesRegex(ValueError,'must not exist'):self.prepare(dest)
  self.assertEqual((dest/'KEEP').read_text(),'my copy')
 def test_private_print_input_requires_separate_review(self):
  (self.root/'screenplay/main_screenplay.tex').write_text('\\input{../sources/private/book.txt}')
  with self.assertRaisesRegex(ValueError,'Private or external'):self.prepare()
 def test_private_original_cannot_leak_through_font_symlink(self):
  (self.root/'fonts/reading-notes.txt').symlink_to(self.root/'sources/private/book.txt')
  with self.assertRaisesRegex(ValueError,'Private or external'):self.prepare()
 def test_private_original_cannot_leak_through_selected_source_symlink(self):
  path=self.root/'screenplay/act1.tex';path.unlink();path.symlink_to(self.root/'sources/private/book.txt')
  with self.assertRaisesRegex(ValueError,'Private or external'):self.prepare()
 def test_failed_editorial_gate_blocks_even_with_visual_receipt(self):
  with patch.object(delivery,'build_problems',return_value=[]),patch.object(delivery,'quality_problems',return_value=['Quality review still requires revision']),patch.object(delivery,'truth_problems',return_value=[]):
   with self.assertRaisesRegex(ValueError,'requires revision'):delivery.prepare(self.root)

if __name__=='__main__':unittest.main()
