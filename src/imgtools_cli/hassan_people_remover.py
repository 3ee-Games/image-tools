# Based off of https://github.com/hassan-sd/people-remover/blob/main/hassan.py
import os
import argparse
import cv2
import pathlib

class HassanPeopleRemover(argparse.Action):
    total_files_chunked = 0

    def __init__(self, option_strings, dest, nargs=None, **kwargs):

        super().__init__(option_strings, dest, nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):

        setattr(namespace, self.dest, values)

        input_directory = values[0]
        path_to_haarcascade = values[1]
        extensions_supported = ('.jpg', 'jpeg', 'png', 'webp')
        for file in os.listdir(input_directory):
            if file.endswith(extensions_supported):
                img = cv2.imread(os.path.join(input_directory, file))
                
                # use face detection to count the number of people in the image
                face_cascade = cv2.CascadeClassifier(path_to_haarcascade)

                # check if the image is empty or the cascade classifier failed to load
                if img is None or face_cascade.empty():
                    print("Failed to load image or cascade classifier, skipping...")
                    continue

                faces = face_cascade.detectMultiScale(img, 1.3, 5)

                # if there are more than one person in the image, delete it
                if len(faces) > 1:
                    os.remove(os.path.join(input_directory, file))
                    print(f"Removed {file}")
                else:
                    print(f"{file} has only one person, keeping it")
