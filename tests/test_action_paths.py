"""Offline CTA/link gate; no HTTP calls, form submissions or publishing."""
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = ['index.html', 'pearl-thrift-store.html', 'byram-thrift-store.html', 'privacy-policy.html']


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.fields = []
        self.forms = []
        self._link = None
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.append(attrs['id'])
        if tag == 'a':
            self._link = [attrs.get('href', ''), '']
        if tag in ('input', 'select', 'textarea'):
            self.fields.append((tag, attrs))
        if tag == 'form':
            self.forms.append(attrs)

    def handle_data(self, data):
        if self._link is not None:
            self._link[1] += data

    def handle_endtag(self, tag):
        if tag == 'a' and self._link is not None:
            self.links.append(tuple(self._link))
            self._link = None


class ActionPaths(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pages = {p: Page(ROOT / p) for p in PAGES}

    def test_all_internal_link_files_and_fragments(self):
        for filename, page in self.pages.items():
            for href, _ in page.links:
                parsed = urlsplit(href)
                if parsed.scheme in ('tel', 'mailto'):
                    continue
                if parsed.netloc and parsed.netloc != 'superthriftdeals.org':
                    continue
                path = unquote(parsed.path)
                dest = ROOT / ('index.html' if path == '/' else path.lstrip('/')) if path.startswith('/') else ROOT / (path or filename)
                if not dest.suffix and not dest.exists():
                    dest = dest.with_suffix('.html')
                self.assertTrue(dest.is_file(), (filename, href))
                if parsed.fragment:
                    target = Page(dest)
                    self.assertIn(parsed.fragment, target.ids, (filename, href))

    def test_unique_ids_and_published_targets(self):
        for filename, page in self.pages.items():
            self.assertEqual(len(page.ids), len(set(page.ids)), filename)
        self.assertTrue({'schedule-pickup', 'what-we-accept', 'locations', 'pearl-location', 'byram-location'}.issubset(self.pages['index.html'].ids))

    def test_home_request_labels_and_shopping_target(self):
        html = (ROOT / 'index.html').read_text()
        links = self.pages['index.html'].links
        self.assertIn(('#schedule-pickup', 'Request a Donation Pickup'), links)
        self.assertIn(('#locations', 'Find a Store to Shop'), links)
        self.assertIn(('#locations', 'Find a SuperThrift Location'), links)
        self.assertNotIn('>Donate Now<', html)
        self.assertNotIn('>Schedule a Pickup<', html)
        self.assertNotIn('>Schedule Donation Pickup<', html)
        self.assertIn('Send Pickup Request', html)
        self.assertIn('it does not confirm an appointment', html)
        self.assertIn('SuperThrift must confirm the items, address, and timing.', html)
        shop = re.search(r'<section id="shop".*?</section>', html, re.S).group()
        self.assertEqual(shop.count('href="#locations"'), 1)

    def test_city_hero_and_exact_directions(self):
        expected = {'pearl': '434 N Bierdeman Rd Pearl MS 39208', 'byram': '6787 S Siwell Rd STE D Byram MS 39272'}
        for city, address in expected.items():
            filename = f'{city}-thrift-store.html'
            html = (ROOT / filename).read_text()
            hero = re.search(r'<section class="city-hero.*?</section>', html, re.S).group()
            self.assertIn('href="index.html#schedule-pickup"', hero)
            self.assertIn('Request a Donation Pickup', hero)
            self.assertIn(f'Get {city.title()} Store Directions', hero)
            self.assertIn('Pickup requests require confirmation', hero)
            self.assertIn(f'Choose {city.title()} Area in the form.', html)
            self.assertIn(('index.html#what-we-accept', 'Review accepted items'), self.pages[filename].links)
            for href, label in self.pages[filename].links:
                if urlsplit(href).netloc == 'maps.google.com':
                    self.assertEqual(parse_qs(urlsplit(href).query)['q'], [address])
            self.assertIn(('tel:6017683532', 'Call (601) 768-3532'), self.pages[filename].links)

    def test_form_transport_and_existing_required_fields(self):
        page = self.pages['index.html']
        self.assertEqual(len(page.forms), 1)
        self.assertEqual(page.forms[0]['action'], 'https://formspree.io/f/xzdekbzd')
        self.assertEqual(page.forms[0]['method'], 'POST')
        visible = {attrs['name']: attrs for _, attrs in page.fields if attrs.get('type') != 'hidden'}
        self.assertEqual(set(visible), {'name', 'phone', 'email', 'address', 'location', 'items'})
        self.assertTrue(all('required' in attrs for attrs in visible.values()))
        html = (ROOT / 'index.html').read_text()
        self.assertIn('<option value="pearl">Pearl Area</option>', html)
        self.assertIn('<option value="byram">Byram Area</option>', html)
        self.assertNotIn('signup', html.lower())

    def test_policy_return_navigation_only(self):
        links = self.pages['privacy-policy.html'].links
        self.assertEqual(links.count(('index.html#schedule-pickup', 'Request a Donation Pickup')), 2)
        self.assertEqual(links.count(('index.html#locations', 'Find a Store to Shop')), 2)
        self.assertNotIn(('index.html#donate', 'Donate'), links)
        self.assertIn(('privacy-policy.html', 'Read our Privacy Policy'), self.pages['index.html'].links)


if __name__ == '__main__':
    unittest.main(verbosity=2)
