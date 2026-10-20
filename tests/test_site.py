"""Check that the public site stays self-contained and its promised paths exist."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.elements = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


class PublicSiteTests(unittest.TestCase):
    def setUp(self):
        self.text = (SITE / 'index.html').read_text()
        self.doc = Document(self.text)

    def test_links_assets_and_fragments_resolve_inside_public_artifact(self):
        ids = [attrs['id'] for _, attrs in self.doc.elements if 'id' in attrs]
        self.assertEqual(len(ids), len(set(ids)), 'duplicate IDs break deep links and labels')
        for tag, attrs in self.doc.elements:
            for attribute in ['href', 'src']:
                if attribute not in attrs:
                    continue
                value = attrs[attribute]
                if value.startswith('#'):
                    self.assertIn(value[1:], ids)
                else:
                    if value.startswith('https://'):
                        self.assertEqual(attribute, 'href', 'external navigation is allowed, remote assets are not')
                        self.assertIn(value.split('/')[2], {'github.com', 'code.claude.com', 'learn.chatgpt.com', 'grok.com', 'developers.openai.com', 'platform.claude.com'})
                        continue
                    self.assertNotIn('://', value, 'remote assets are not allowed')
                    target = (SITE / value).resolve()
                    self.assertTrue(target.is_relative_to(SITE.resolve()))
                    self.assertTrue(target.is_file(), str(target))
        for asset in re.findall(r"url\(['\"]?([^)'\"]+)", (SITE / 'style.css').read_text()):
            self.assertTrue((SITE / asset).is_file(), asset)

    def test_navigation_and_form_have_accessible_sources(self):
        self.assertEqual(sum(tag == 'h1' for tag, _ in self.doc.elements), 1)
        panels = [attrs['id'] for tag, attrs in self.doc.elements if tag == 'section']
        tabs = [attrs['href'][1:] for _, attrs in self.doc.elements if attrs.get('class') == 'chapter-tab']
        self.assertEqual(tabs, panels)
        labels = {attrs.get('for') for tag, attrs in self.doc.elements if tag == 'label'}
        for tag, attrs in self.doc.elements:
            if tag in ['input', 'textarea', 'select']:
                self.assertIn(attrs['id'], labels)
        self.assertIn('<noscript>', self.text)
        self.assertIn('aria-live="polite"', self.text)

    def test_site_has_no_outbound_data_or_persisted_story_code(self):
        js = (SITE / 'app.js').read_text()
        self.assertNotRegex(js, r'\b(fetch|XMLHttpRequest|WebSocket|sendBeacon|localStorage|sessionStorage)\b')
        policies = [attrs['content'] for tag, attrs in self.doc.elements if attrs.get('http-equiv') == 'Content-Security-Policy']
        self.assertEqual(len(policies), 1)
        self.assertIn("connect-src 'none'", policies[0])
        self.assertIn("form-action 'none'", policies[0])
        self.assertNotIn('<iframe', self.text)
        self.assertIn('github.com/jayzalowitz/story-factory', self.text)

    def test_publication_contains_only_reviewed_public_files(self):
        allowed = {
            'index.html', 'style.css', 'app.js', 'story-starter.txt', '.nojekyll',
            'assets/Tinos-Regular.ttf', 'assets/Tinos-Italic.ttf', 'assets/Arimo-Regular.ttf',
            'assets/LICENSE.txt', 'assets/favicon.svg',
            'assets/ledger-room-screenplay.png', 'assets/ledger-room-package.png',
        }
        for stem in ['screenplay', 'studio-package', 'one-pager', 'actor-pitch', 'director-pitch',
                     'financier-pitch', 'distributor-pitch', 'producer-pitch', 'festival-pitch',
                     'streamer-pitch', 'coproduction-pitch', 'talent-rep-pitch', 'awards-pitch',
                     'public-funder-pitch', 'exhibitor-pitch', 'cultural-partnership-pitch',
                     'press-pitch', 'craft-pitch']:
            allowed.add('examples/the-letter-to-the-father/' + stem + '.pdf')
            allowed.add('examples/the-night-window/' + stem + '.pdf')
            allowed.add('examples/the-ledger-room/' + stem + '.pdf')
        allowed.add('examples/adaptation/twelve-seconds.pdf')
        allowed.add('examples/inspired-by/the-pool.pdf')
        allowed.add('examples/the-letter-to-the-father/screenplay-revised.pdf')
        actual = {path.relative_to(SITE).as_posix() for path in SITE.rglob('*') if path.is_file()}
        self.assertEqual(actual, allowed, 'review new public files before changing the publication allowlist')

    def test_beginner_path_and_optional_controls_match_supported_hosts(self):
        for phrase in ['Download the toolkit ZIP', 'Extract All', 'Code</strong> tab',
                       'included installer for my current assistant', '$story-run', '/story-run',
                       '/story-handoff', '/story-resume', 'has not been tested']:
            self.assertIn(phrase, self.text)
        component_inputs = [attrs for tag, attrs in self.doc.elements
                            if tag == 'input' and attrs.get('name') == 'component']
        self.assertEqual(len(component_inputs), 32)
        self.assertTrue(all('checked' not in attrs for attrs in component_inputs))
        self.assertIn('<option value="off">Off', self.text)
        js = (SITE / 'app.js').read_text()
        for phrase in ['packageBrief', 'sourceBrief', 'swarmBrief', 'development/package_options.json',
                       'Parallel helpers are OFF', 'do not allow simultaneous screenplay edits']:
            self.assertIn(phrase, js)
        self.assertNotIn('Access is by invitation', self.text)

    def test_downloadable_starter_is_real_and_honest(self):
        text = (SITE / 'story-starter.txt').read_text()
        self.assertGreater(len(text), 1000)
        self.assertIn('MY IDEA', text)
        self.assertIn('one useful question at a time', text)
        self.assertIn('Do not publish', text)
        self.assertNotIn('DRAFT PLACEHOLDER', text)
        self.assertFalse(list(SITE.glob('*.pdf')), 'no deck PDF companion was requested')
        self.assertIn('not newly generated by the command suite', self.text)
        self.assertIn('Proposed casting is unattached', self.text)
        self.assertFalse((SITE / '.git').exists())


if __name__ == '__main__':
    unittest.main()
