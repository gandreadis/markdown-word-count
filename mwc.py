import os
import re
import sys


def count_words_in_markdown(markdown):
    text = markdown

    # Footnotes
    text = re.sub(r'^\[[0-9]*\].*', '', text, flags=re.MULTILINE)
    # Indented blocks of code
    text = re.sub(r'^( {4,}).*', '', text, flags=re.MULTILINE)
    # Replace newlines with spaces for uniform handling
    text = text.replace('\n', ' ')
    # Custom header IDs
    text = re.sub(r'{#.*}', '', text)
    # Remove images
    text = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', text)
    # Remove HTML tags
    text = re.sub(r'</?[^>]*>', '', text)
    # Remove special characters
    text = re.sub(r'[#*`~\-^=<>+|/:]', '', text)
    # Remove footnote references
    text = re.sub(r'\[[0-9]*\]', '', text)
    # Remove enumerations
    text = re.sub(r'[0-9#]*\.', '', text)

    return len(text.split())


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Provide the file to parse as first argument')
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('The file at the given location could not be opened')
        sys.exit(1)

    with open(sys.argv[1], 'r', encoding='utf8') as f:
        print(count_words_in_markdown(f.read()))
