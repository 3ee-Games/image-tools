import os
from PIL import Image
import argparse
import pillow_heif
import cv2
import numpy as np

class ImageConvert(argparse.Action):

    def __init__(self, option_strings, dest, nargs=None, **kwargs):

        super().__init__(option_strings, dest, nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):

        setattr(namespace, self.dest, values)
        
        input_directory = values[0]
        extensions_supported = ('jpg', 'jpeg', 'webp')
        total_supported_files = 0
        
        for files in os.listdir(input_directory):
            new_file_name = files + ".png"

            if files.lower().endswith(extensions_supported):
                image = Image.open(os.path.join(input_directory, files))
                rgb_image = image.convert('RGB')
                rgb_image.save(os.path.join(input_directory, new_file_name), format="png")

                print("* Converted: " + str(files) + " to: " + new_file_name)
                total_supported_files += 1

            elif files.endswith('heic'):
                heif_file = pillow_heif.open_heif(os.path.join(input_directory, files), convert_hdr_to_8bit=False)
                heif_file.convert_to("BGRA;16" if heif_file.has_alpha else "BGR;16")
                np_array = np.asarray(heif_file)
                cv2.imwrite(os.path.join(input_directory, new_file_name), np_array)

                print("* Converted: " + str(files) + " to: " + new_file_name)
                total_supported_files += 1


        if files is None or len(files) == 0 or total_supported_files == 0:
            print("No image files found in: {}".format(input_directory))