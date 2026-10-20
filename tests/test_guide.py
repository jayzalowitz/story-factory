"""Keep the readable/public guide in sync with its source and supported menu."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('build_guide',ROOT/'scripts/build_guide.py')
builder=importlib.util.module_from_spec(spec);spec.loader.exec_module(builder)

class GuideTests(unittest.TestCase):
    def test_published_and_markdown_guides_are_current(self):
        for path,expected in builder.render().items():
            self.assertEqual(path.read_text(),expected,'Rebuild the guide before publishing: '+str(path))

    def test_advertised_complete_materials_match_supported_selection(self):
        from story_factory.package_options import SECTIONS,PITCHES
        data=json.loads((ROOT/'docs/guide-content.json').read_text())
        self.assertEqual(data['catalog_ids']['sections'],SECTIONS)
        self.assertEqual(data['catalog_ids']['pitches'],PITCHES)
        package=next(s for s in data['sections'] if s['id']=='package')
        tables=[block['blocks'][0] for block in package['blocks'] if block['type']=='details']
        self.assertEqual([len(t['rows']) for t in tables],[len(SECTIONS),len(PITCHES)])

if __name__=='__main__':unittest.main()
