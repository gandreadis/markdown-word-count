# ⬇ Markdown Word Count

[![CircleCI status](https://circleci.com/gh/gandreadis/markdown-word-count.svg?style=svg)](https://circleci.com/gh/gandreadis/markdown-word-count)

A word counter for raw Markdown files, excluding punctuation, footnotes, and special Markdown or HTML tag syntax.

## 💻 Installation

You will need...

- 🐍 Python 3
- 🐑 A [clone](https://github.com/gandreadis/markdown-word-count.git) of this repo or a [single file download](https://github.com/gandreadis/markdown-word-count/blob/master/mwc.py) of the script.

## ▶ Usage

To run this script, pass the file you want to have analyzed as the first parameter:

```
./mwc.py myfile.md
```

If that doesn't work, explicitely pass the program to Python:

```
python mwc.py myfile.md
```

If this doesn't work, try `python3` instead of `python`.

## ⛏ Development

Run this to execute all tests:

```
python -m unittest discover
```

## 💬 Ports to Other Programming Languages

* A PHP port can be found [here](https://github.com/Arcesilas/md-word-count), with thanks to [@Arcesilas](https://github.com/Arcesilas)!
