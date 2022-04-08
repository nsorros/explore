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

Add a custom way to process documents before displaying

```
# xml_document_processor.py

import xml.etree.ElementTree as ET

from explore import document_processors


@document_processors.register("xml")
def xml_document_processor(document):
    root = ET.fromstring(document)

    texts = []
    for elem in root.iter("span"):
        if isinstance(elem.text, str):
            texts.append(elem.text)
            text_content = " ".join(texts)
    return text_content
```

Then run explore by passing path to your code and name of processor

```
explore data/ \
    --code-path xml_document_processor.py \
    --document-processor-name xml
```

# CLI

```
Usage: explore.py [OPTIONS] DIR_PATH

Arguments:
  DIR_PATH  [required]

Options:
  --snippet-length INTEGER        [default: 2000]
  --split / --no-split            [default: split]
  --code-path TEXT
  --document-processor-name TEXT  [default: txt]
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
