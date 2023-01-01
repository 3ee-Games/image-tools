import os
from PIL import Image
import pillow_heif
import argparse

class HeicToPng(argparse.Action):

    def __init__(self, option_strings, dest, nargs=None, **kwargs):

        super().__init__(option_strings, dest, nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):

        print('%r %r %r %r' % (namespace, values, option_string, self.nargs))
        setattr(namespace, self.dest, values)
        
        images_path = values[0]
        extensions_supported = ('.heic', 'heica')
        total_supported_files = 0

        for files in os.listdir(images_path):
            if files.endswith(extensions_supported):
                print("Loading: " + files)
                heif_file = pillow_heif.read_heif(os.path.join(images_path, files))
                image = Image.frombytes(
                    heif_file.mode,
                    heif_file.size,
                    heif_file.data,
                    "raw",
                )
                new_file_name = files + ".png"
                image.save(os.path.join(images_path, files), format="png")
                print("Converted: " + new_file_name)
                total_supported_files += 1

        if files is None or len(files) == 0 or total_supported_files == 0:
            print("No HEIC files found in: {}".format(images_path))