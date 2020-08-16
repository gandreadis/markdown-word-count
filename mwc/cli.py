#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os.path import join, isfile, isdir, exists
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

    if not exists(sys.argv[1]):
        print('File or folder not found.')
        sys.exit(1)

    if isdir(sys.argv[1]):
        allfiles = [join(sys.argv[1], f) for f in listdir(sys.argv[1]) if isfile(join(sys.argv[1], f)) and f.endswith('.md')]
        allfiles.sort()
        response = str()
        for file in allfiles:
            with open(file, 'r', encoding='utf8') as f:
                r = '{0} - {1}\n'.format(file, count_words_in_markdown(f.read()))
                response += r
        print(response)
        return response

    with open(sys.argv[1], 'r', encoding='utf8') as f:
        if not sys.argv[1].endswith('.md'):
            print('The file provided in the first argument is not a Markdown file.')
            sys.exit(1)
        response = '{0} - {1}'.format(sys.argv[1], count_words_in_markdown(f.read()))
        print(response)
        return response


if __name__ == '__main__':
    main()
