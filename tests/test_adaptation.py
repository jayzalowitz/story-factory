"""Adaptation checks prevent changed evidence from inheriting a prior review."""
import copy
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from story_factory import adaptation
ROOT=Path(__file__).resolve().parents[1]
class AdaptationTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)/'story'
        shutil.copytree(ROOT/'examples/adaptation',self.root)
    def save(self,data):
        (self.root/'adaptation/project.json').write_text(json.dumps(data))
    def test_complete_example_is_current(self):
        self.assertEqual(adaptation.problems(self.root,True),[])
    def test_source_edit_invalidates_reading_and_review(self):
        p=self.root/'sources/nps-reading-notes.md';p.write_text(p.read_text()+'\nChanged source\n')
        errors=adaptation.problems(self.root,True)
        self.assertTrue(any('source changed' in e for e in errors));self.assertTrue(any('stale for source' in e for e in errors))
    def test_draft_edit_requires_rereview(self):
        p=self.root/'screenplay/twelve-seconds.fountain';p.write_text(p.read_text()+'\nA different ending.\n')
        self.assertTrue(any('stale for the screenplay' in e for e in adaptation.problems(self.root,True)))
    def test_unread_source_and_unapproved_departure_block_ready(self):
        data=adaptation.load(self.root);data['sources'][0]['read_units']=[1];data['departures'][0]['decision']='proposed';self.save(data)
        errors=adaptation.problems(self.root,True)
        self.assertTrue(any('unread units' in e for e in errors));self.assertTrue(any('not approved' in e for e in errors))
    def test_scene_omission_and_bad_locator_rejected(self):
        data=adaptation.load(self.root);data['scenes'].pop();data['scenes'][0]['source_refs'][0]['locator']='';self.save(data)
        errors=adaptation.problems(self.root,True)
        self.assertTrue(any('Scene map does not match' in e for e in errors));self.assertTrue(any('invalid source reference' in e for e in errors))
    def test_outside_or_symlink_source_rejected(self):
        data=adaptation.load(self.root);data['sources'][0]['path']='../../outside';self.save(data)
        self.assertTrue(any('outside' in e for e in adaptation.problems(self.root)))
        p=self.root/'sources/link';p.symlink_to(self.root/'sources/nps-reading-notes.md');data['sources'][0]['path']='sources/link';self.save(data)
        self.assertTrue(any('symlink' in e for e in adaptation.problems(self.root)))
    def test_malformed_structured_fields_rejected_without_traceback(self):
        data=adaptation.load(self.root);data['sources'][0]['kind']=[];data['sources'][0]['rights']['status']=[];data['departures'][0]['id']=[];data['scenes'][0]['id']=[];self.save(data)
        self.assertGreater(len(adaptation.problems(self.root,True)),3)
    def test_malformed_record_rejected(self):
        (self.root/'adaptation/project.json').write_text('[]')
        self.assertTrue(adaptation.problems(self.root))
if __name__=='__main__':unittest.main()
