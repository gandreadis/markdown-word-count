#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys

from mwc.counter import count_words_in_markdown


def main():
    if sys.version_info < (3,):
        print('Python 3 is required. You are using Python 2. You should probably run this script as follows:')
        print('python3 mwc.py')
        sys.exit(1)

    if len(sys.argv) < 2:
        print('Provide the Markdown file to parse as first argument')
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('The file at the given location could not be opened')
        sys.exit(1)

    with open(sys.argv[1], 'r', encoding='utf8') as f:
        print(count_words_in_markdown(f.read()))


if __name__ == '__main__':
    main()
