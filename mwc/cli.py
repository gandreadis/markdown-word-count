#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys

from mwc.counter import count_words_in_markdown


def get_count(files):
    count = 0
    for file in files:
        if not os.path.isfile(file):
            print('The file at the given location {file} could not be opened')
            sys.exit(1)
        with open(file, 'r', encoding='utf8') as f:
            count += count_words_in_markdown(f.read())

    return count


def main():
    if sys.version_info < (3,):
        print(
            'Python 3 is required. You are using Python 2. You should probably run this script as follows:')
        print('python3 mwc.py')
        sys.exit(1)

    if len(sys.argv) < 2:
        print('Provide the Markdown file to parse as first argument')
        sys.exit(1)

    files = sys.argv[1:]

    count = get_count(files)

    if len(files) == 1:
        print(f"Number of words in file {files[0]}")
        print(count)
    else:
        print(f"Words across {len(files)} files")
        print(count)

    return count


if __name__ == '__main__':
    main()
