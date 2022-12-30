import os
from PIL import Image
from itertools import product

extensions_supported = ('.jpg', 'jpeg', 'png', 'webp')

def tile(filename, input_directory, output_directory, square_dimension):
    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(input_directory, filename))
    width, height = img.size

    grid = product(range(0, height - height % square_dimension, square_dimension), range(0, width - width % square_dimension, square_dimension))

    for i, j in grid:
        box = (j, i, j + square_dimension, i + square_dimension)
        out = os.path.join(output_directory, f'{name}_{i}_{j}.png')
        img.crop(box).save(out, format="png")


tile('long_shot.jpg', 'images', 'tiles', 512)
