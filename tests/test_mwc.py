import textwrap
from unittest import TestCase

from mwc import count_words_in_markdown


class TestMWC(TestCase):
    def test_simple_text(self):
        text = textwrap.dedent("""
        test a b    c
        """)
        self.assertEqual(count_words_in_markdown(text), 4)

    def test_headings(self):
        text = textwrap.dedent("""
        # H1
        ## H2
        ### H3
        
        H1
        -----
        
        H1
        =====
        
        ### My Great Heading {#custom-id}
        """)
        self.assertEqual(count_words_in_markdown(text), 8)

    def test_inline(self):
        text = textwrap.dedent("""
        **bold text**
        *italicized text*
        `test`
        ~~test~~
        """)
        self.assertEqual(count_words_in_markdown(text), 6)

    def test_quote(self):
        text = textwrap.dedent("""
        > blockquote
        """)
        self.assertEqual(count_words_in_markdown(text), 1)

    def test_enumeration(self):
        text = textwrap.dedent("""
        1. foo
        2. bar
        """)
        self.assertEqual(count_words_in_markdown(text), 2)

    def test_bullet_points(self):
        text = textwrap.dedent("""
        - foo
        - bar
        """)
        self.assertEqual(count_words_in_markdown(text), 2)

    def test_code_block(self):
        text = textwrap.dedent("""
        ```
        test
        ```
        """)
        self.assertEqual(count_words_in_markdown(text), 1)

    def test_link(self):
        text = textwrap.dedent("""
        Some [linked text](https://google.com/).
        """)
        self.assertEqual(count_words_in_markdown(text), 3)

    def test_image(self):
        text = textwrap.dedent("""
        test
        
        ![test](images1)
        
        ![blah](images2)
        
        test
        """)
        self.assertEqual(count_words_in_markdown(text), 2)

    def test_footnote(self):
        text = textwrap.dedent("""
        MWC is great [1].
        
        [1] source footnote
        
        Followup text
        """)
        self.assertEqual(count_words_in_markdown(text), 5)

    def test_html_tags(self):
        text = textwrap.dedent("""
        test
        
        <br>
        <span>test</span>
        
        test
        """)
        self.assertEqual(count_words_in_markdown(text), 3)
