# Image Tools CLI 🖼️
    
[![PyPI version](https://badge.fury.io/py/imgtools-cli.svg)](https://badge.fury.io/py/imgtools-cli)
[![Downloads](https://pepy.tech/badge/imgtools-cli)](https://pepy.tech/project/imgtools-cli)
[![Downloads](https://pepy.tech/badge/imgtools-cli/month)](https://pepy.tech/project/imgtools-cli)
[![Downloads](https://pepy.tech/badge/imgtools-cli/week)](https://pepy.tech/project/imgtools-cli)

Command line interface for pre-processing images for model training.

## Features

- Download all images from a url
- Convert HEIC images to PNG
- Chunk large images into smaller squares

_Example:_ You may want to train on this image but need to split it into smaller squares for training.
![Chunk Images](https://github.com/3ee-Games/image-tools/blob/main/images/long.jpg) 

Put it through the chunker and you get this:

| chunk 1                                                                                              | chunk 2                                                                                                | chunk 3                                                                                                 |   |   |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|---|---|
| ![ Chunked Image Example ]( https://github.com/3ee-Games/image-tools/blob/main/images/long_0_0.png ) | ![ Chunked Image Example ]( https://github.com/3ee-Games/image-tools/blob/main/images/long_0_512.png ) | ![ Chunked Image Example ]( https://github.com/3ee-Games/image-tools/blob/main/images/long_0_1024.png ) |   |   |


- Remove images with more than one person

_Example:_ If your input images have more than one person, the image will be deleted:

![ Chunked Image Example ]( https://github.com/3ee-Games/image-tools/blob/main/images/sample%20(6).jpg )

## Installation

create a virtual environment and imgtools-cli through pip:

```bash

python3 -m venv venv

source venv/bin/activate

pip install imgtools-cli
```

## Usage

**Help**

```bash
python -m imgtools_cli -h
```

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

**Hassa People Remover**

Uses face detection to remove images with more than one person. Helpful for cleaning source images to be used for Stable Diffusion training.

Sample images: 
- https://github.com/hassan-sd/people-remover/blob/main/images/sample%20(5).jpg
- https://github.com/hassan-sd/people-remover/blob/main/images/sample%20(7).jpg
- https://github.com/hassan-sd/people-remover/blob/main/images/sample%20(3).jpg

```bash
python -m imgtools_cli -R /Users/ryguy/Documents/github/image-tools/images/
```

Ported from: https://github.com/hassan-sd/people-remover
