# ⬇ Markdown Word Count

[![CircleCI status](https://circleci.com/gh/gandreadis/markdown-word-count.svg?style=svg)](https://circleci.com/gh/gandreadis/markdown-word-count)

A word counter for raw Markdown files, excluding punctuation, footnotes, and special Markdown or HTML tag syntax.

## 💻 Installation

You will need...

- 🐍 Python 3
- 🐑 PIP3 or a [clone](https://github.com/gandreadis/markdown-word-count.git) of this repo.

## ▶ Usage

### Through PIP

The easiest way is to run:

```
pip install markdown-word-count
```

Then, you'll be able to analyze any file by passing its name (relative path) to the `mwc` script:

```
mwc yourfile.md
```

You can also pass in multiple files or a blob if your shell supports it. This allows for checking all files in a folder, for example.

```
mwc text1.md text2.md
mwc test/*.md
```

### Manually

If you want to clone the repo and run the Python script manually, run:

```
python mwc/cli.py myfile.md
```

If this doesn't work, try `python3` instead of `python`.

## ⛏ Development

Run this to execute all tests:

```
python -m unittest discover
```

## 💬 Ports to Other Programming Languages

- A PHP port can be found [here](https://github.com/Arcesilas/md-word-count), with thanks to [@Arcesilas](https://github.com/Arcesilas)!
