# Explore

Explore is a minimal CLI tool to explore files within data folders

# Quickstart

Install explore

```
pip install git+https://github.com/nsorros/explore.git
```

Explore a data folder

```
explore data/
```

the tool will start to pring segments of documents with the
data folder until you press q or ESC

# CLI

```
Usage: explore [OPTIONS] DIR_PATH

Arguments:
  DIR_PATH  [required]

Options:
  --snippet-length INTEGER        [default: 2000]
  --split / --no-split            [default: split]
  --help                          Show this message and exit.
```

# Contribute

Clone the project and install in develop mode, probably
after creating a virtualenv

```
git clone git@github.com:nsorros/explore.git
pip install -e .
```

Install pre commit
```
pip install pre-commit
pre-commit install
```
