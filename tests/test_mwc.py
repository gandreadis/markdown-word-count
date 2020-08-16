import os
import sys
import shutil

import textwrap
from unittest import TestCase

from mwc.counter import count_words_in_markdown
from mwc.cli import main

try:
    # Python 3.4+ should use builtin unittest.mock not mock package
    from unittest.mock import patch
except ImportError:
    from mock import patch


class TestMWC(TestCase):

    def test_single_markdown_file(self):
        # Test single markdown file
        with open("test.md", "w+") as f:
            f.write("this is a markdown file!")
        testargs = ["mwc.cli", "test.md"]
        with patch.object(sys, 'argv', testargs):
            test = main()
            self.assertEqual(test, "test.md - 5")
        os.remove("test.md")

    def test_single_python_file(self):
        # Test when user passes a file that isn't markdown
        with open("test.py", "w+") as f:
            f.write("print('hello world')")
        testargs = ["mwc.cli", "test.py"]
        with patch.object(sys, 'argv', testargs):
            with self.assertRaises(SystemExit):
                test = main()
        os.remove("test.py")

    def test_folder_with_markdown_files(self):
        # Test multiple files in folder
        if os.path.exists("test"):
            shutil.rmtree("test")
        os.mkdir("test")
        with open("test/test1.md", "w+") as f:
            f.write("this is a markdown file!")
        with open("test/test2.md", "w+") as f:
            f.write("this is a markdown file number 2!")
        testargs = ["mwc.cli", "test"]
        with patch.object(sys, 'argv', testargs):
            test = main()
            self.assertEqual(test, "test/test1.md - 5\ntest/test2.md - 7\n")
        shutil.rmtree("test")

    def test_file_does_not_exist(self):
        # Test if program works when file or folder doesn't exist
        testargs = ["mwc.cli", "something.md"]
        with patch.object(sys, 'argv', testargs):
            with self.assertRaises(SystemExit):
                test = main()

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

    def test_comments(self):
        text = textwrap.dedent("""
        <!-- Test -->
        <!-- > Test -->
        <!-- 
        
        Test
        
        -->
        
        Test
        """)
        self.assertEqual(count_words_in_markdown(text), 1)

    def test_quote(self):
        text = textwrap.dedent("""
        > blockquote
        """)
        self.assertEqual(count_words_in_markdown(text), 1)

    def test_enumeration(self):
        text = textwrap.dedent("""
        1. foo
        2. bar
        #. smart item
        """)
        self.assertEqual(count_words_in_markdown(text), 4)

    def test_bullet_points(self):
        text = textwrap.dedent("""
        - foo
        - bar
        """)
        self.assertEqual(count_words_in_markdown(text), 2)

    def test_nested_bullet_points(self):
        text = textwrap.dedent("""
        - foo
        - bar
            - test
        """)
        self.assertEqual(count_words_in_markdown(text), 3)

    def test_nested_star_bullet_points(self):
        text = textwrap.dedent("""
        - foo
        - bar
            * test
                * baz
        """)
        self.assertEqual(count_words_in_markdown(text), 4)

    def test_indented_code_block(self):
        text = textwrap.dedent("""
        foo bar
        
            test code
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
        [1](do count this one please)
        
        Followup text
        """)
        self.assertEqual(count_words_in_markdown(text), 10)

    def test_html_tags(self):
        text = textwrap.dedent("""
        test
        
        <br>
        <span>test</span>
        
        test
        """)
        self.assertEqual(count_words_in_markdown(text), 3)

    def test_custom_header_tags(self):
        text = textwrap.dedent("""
        ## header1 {#header1}
        foo bar
        ## header2 {#header2}
        """)
        self.assertEqual(count_words_in_markdown(text), 4)
