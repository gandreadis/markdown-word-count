#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os.path import join, isfile, isdir
from os import listdir
import os
import sys

from mwc.counter import count_words_in_markdown


def main():
    if sys.version_info < (3,):
        print('Python 3 is required. You are using Python 2. You should probably run this script as follows:')
        print('python3 mwc.py')
        sys.exit(1)

    if len(sys.argv) < 2:
        print('Provide the Markdown file or folder to parse as first argument')
        sys.exit(1)

    if isdir(sys.argv[1]):
        allfiles = [join(sys.argv[1], f) for f in listdir(sys.argv[1]) if isfile(join(sys.argv[1], f)) and f.endswith(".md")]
        for file in allfiles:
            with open(file, 'r', encoding='utf8') as f:
                print(file, count_words_in_markdown(f.read()))
        return 0

    with open(sys.argv[1], 'r', encoding='utf8') as f:
        print(count_words_in_markdown(f.read()))


if __name__ == '__main__':
    main()
