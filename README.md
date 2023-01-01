# Image Tools CLI

Command line interface for working processing images for model training.


## Installation

create a virtual environment and imgtools-cli through pip:

```bash

python3 -m venv venv

source venv/bin/activate

pip install imgtools-cli
```

## Usage

**Download all images from a website**

```bash
python -m imgtools_cli -D https://www.gutenberg.org/cache/epub/67098/pg67098-images.html
```

**Convert HEIC to PNG**

```bash
python -m imgtools_cli -P /Users/ootie/heic_files
```

**Chunk large images into squares**

Easily take large images and split them into smaller squares for training.

```bash
python -m imgtools_cli -C 512 /Users/ootie/input /Users/ootie/output
```