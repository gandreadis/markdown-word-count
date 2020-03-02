# ⬇ Markdown Word Count

[![Build Status](https://travis-ci.com/gandreadis/markdown-word-count.svg?branch=master)](https://travis-ci.com/gandreadis/markdown-word-count)

A word counter for raw Markdown files, excluding punctuation, footnotes, and special Markdown or HTML tag syntax.

## 💻 Installation

You will need...

- 🐍 Python 3
- 🐑 A [clone](https://github.com/gandreadis/markdown-word-count.git) of this repo or a [single file download](https://github.com/gandreadis/markdown-word-count/blob/master/mwc.py) of the script.

## ▶ Usage

To run this script, pass the file you want to have analyzed as first parameter:

```
python mwc.py myfile.md
```

Since this script requires version 3, you might need to run that version specifically, depending on your local setup:

```
python3 mwc.py myfile.md
```

## ⛏ Development

Run this to execute all tests:

```
python -m unittest discover
```

## 💬 Ports to Other Programming Languages

* A PHP port can be found [here](https://github.com/Arcesilas/md-word-count), with thanks to [@Arcesilas](https://github.com/Arcesilas)!
