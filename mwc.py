#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys


def count_words_in_markdown(markdown):
    text = markdown

    # Comments
    text = re.sub(r'<!--(.*?)-->', '', text, flags=re.MULTILINE)
    # Tabs to spaces
    text = text.replace('\t', '    ')
    # More than 1 space to 4 spaces
    text = re.sub(r'[ ]{2,}', '    ', text)
    # Footnotes
    text = re.sub(r'^\[[^]]*\][^(].*', '', text, flags=re.MULTILINE)
    # Indented blocks of code
    text = re.sub(r'^( {4,}[^-*]).*', '', text, flags=re.MULTILINE)
    # Custom header IDs
    text = re.sub(r'{#.*}', '', text)
    # Replace newlines with spaces for uniform handling
    text = text.replace('\n', ' ')
    # Remove images
    text = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', text)
    # Remove HTML tags
    text = re.sub(r'</?[^>]*>', '', text)
    # Remove special characters
    text = re.sub(r'[#*`~\-–^=<>+|/:]', '', text)
    # Remove footnote references
    text = re.sub(r'\[[0-9]*\]', '', text)
    # Remove enumerations
    text = re.sub(r'[0-9#]*\.', '', text)

    return len(text.split())


if __name__ == '__main__':
    if sys.version_info < (3,):
        print("Python 3 is required. You are using Python 2. You should probably run this script as follows:\npython3 mwc.py")
        sys.exit(1)

    if len(sys.argv) < 2:
        print('Provide the file to parse as first argument')
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('The file at the given location could not be opened')
        sys.exit(1)

    with open(sys.argv[1], 'r', encoding='utf8') as f:
        print(count_words_in_markdown(f.read()))
