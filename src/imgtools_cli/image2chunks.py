import argparse
import os

from PIL import Image
from itertools import product

class ImageToChunks(argparse.Action):
    total_files_chunked = 0
    def __init__(self, option_strings, dest, nargs=None, **kwargs):

        super().__init__(option_strings, dest, nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):

        setattr(namespace, self.dest, values)

        extensions_supported = ('jpg', 'jpeg', 'png', 'webp')
        total_supported_files = 0
        
        square_dimension = int(values[0])
        input_directory = values[1]
        output_directory = values[2]

        for files in os.listdir(input_directory):
            if files.lower().endswith(extensions_supported):
                print("Loading: " + files)
                self.chunk(square_dimension, files, input_directory, output_directory)
                total_supported_files += 1

        if files is None or len(files) == 0 or total_supported_files == 0:
            print("No image files found in: {}".format(input_directory))

        print("Total files chunked: {} at {} x {}.  Files saved to: {}".format(self.total_files_chunked, square_dimension, square_dimension, output_directory))

    def chunk(self, square_dimension, filename, input_directory, output_directory ):
            name, ext = os.path.splitext(filename)
            img = Image.open(os.path.join(input_directory, filename))
            width, height = img.size

            grid = product(range(0, height - height % square_dimension, square_dimension), range(0, width - width % square_dimension, square_dimension))

            for i, j in grid:
                box = (j, i, j + square_dimension, i + square_dimension)
                out = os.path.join(output_directory, f'{name}_{i}_{j}.png')
                img.crop(box).save(out, format="png")
                self.total_files_chunked += 1