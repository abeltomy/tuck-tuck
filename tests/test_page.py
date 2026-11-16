import unittest
from html.parser import HTMLParser
from pathlib import Path


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.paper_text = []
        self.header_titles = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.stack.append((tag, attrs))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        if any(a.get('id') == 'paper' for _, a in self.stack):
            if not any(a.get('id') == 'probe' for _, a in self.stack):
                self.paper_text.append(data.strip())
        if any(t == 'header' for t, _ in self.stack) and any(t == 'h1' for t, _ in self.stack):
            self.header_titles.append(data.strip())


class PlainPaperTest(unittest.TestCase):
    def test_blank_paper_with_title_in_toolbar(self):
        page = PageParser()
        page.feed((Path(__file__).resolve().parents[1] / 'index.html').read_text())
        self.assertEqual(''.join(page.paper_text), '', 'Paper must contain no preprinted text')
        self.assertEqual(page.header_titles, ['Tuck Tuck'])


if __name__ == '__main__':
    unittest.main()
