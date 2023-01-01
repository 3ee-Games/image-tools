# Based off of https://github.com/hassan-sd/people-remover/blob/main/hassan.py
import os
import argparse
import cv2
import logging
import pathlib


class HassanPeopleRemover(argparse.Action):
    total_files_chunked = 0

    def __init__(self, option_strings, dest, nargs=None, **kwargs):

        super().__init__(option_strings, dest, nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):

        print('%r %r %r %r' % (namespace, values, option_string, self.nargs))
        setattr(namespace, self.dest, values)

        logging.basicConfig(filename='hassan.log', filemode='w',
                            format='%(name)s - %(levelname)s - %(message)s')

        input_directory = values[0]
        extensions_supported = ('.jpg', 'jpeg', 'png', 'webp')
        for file in os.listdir(input_directory):
            if file.endswith(extensions_supported):
                img = cv2.imread(os.path.join(input_directory, file))
                
                
                current_path = pathlib.Path(__file__).parent.resolve()
                haarcascade_xml = str(current_path) + '/haarcascade_frontalface_default.xml'
                # use face detection to count the number of people in the image
                face_cascade = cv2.CascadeClassifier(haarcascade_xml)

                # check if the image is empty or the cascade classifier failed to load
                if img is None or face_cascade.empty():
                    print("Failed to load image or cascade classifier, skipping...")
                    continue

                faces = face_cascade.detectMultiScale(img, 1.3, 5)

                # if there are more than one person in the image, delete it
                if len(faces) > 1:
                    os.remove(os.path.join(input_directory, file))
                    print(f"Removed {file}")
                    logging.warning(f"Removed {file}")
                else:
                    print(f"{file} has only one person, keeping it")
