import os
from PIL import Image
import argparse
from imgtools_cli import autocrop

class ImageResize(argparse.Action):

    def __init__(self, option_strings, dest, nargs=None, **kwargs):

        super().__init__(option_strings, dest, nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):

        setattr(namespace, self.dest, values)
        
        input_directory = values[0]
        resize_width = int(values[1])
        resize_height = int(values[2])
        crop_focal_point = bool(values[3])
        dnn_model_path = values[4]
        
        if values[4] is not None:
            dnn_model_path = values[4]

        extensions_supported = ('jpg', 'jpeg', 'webp', 'png')
        total_supported_files = 0

        for files in os.listdir(input_directory):
            if files.lower().endswith(extensions_supported):
                image = Image.open(os.path.join(input_directory, files))
                width = resize_width
                height = resize_height
                dnn_model_path = None 

                if crop_focal_point and image.height != image.width:
                    try:
                        dnn_model_path = autocrop.download_and_cache_models(os.path.join(dnn_model_path, "opencv"))
                    except Exception as e:
                        print("Unable to load face detection model for auto crop selection. Falling back to lower quality haar method.", e)


                if crop_focal_point:
                    autocrop_settings = autocrop.Settings(
                        crop_width = width,
                        crop_height = height,
                        face_points_weight = 0.9,
                        entropy_points_weight = 0.3,
                        corner_points_weight = 0.5,
                        annotate_image = False,
                        dnn_model_path = dnn_model_path,
                    )

                    image = autocrop.crop_image(image, autocrop_settings)[0]
                    print("* Cropped: " + str(files) + " at: " + str(width) + " x " + str(height))
                else:
                    image = image.resize((width, height), Image.Resampling.LANCZOS)
                    print("* Resized: " + str(files) + " at: " + str(width) + " x " + str(height))
 
                image.save(os.path.join(input_directory, files))
                total_supported_files += 1

        if files is None or len(files) == 0 or total_supported_files == 0:
            print("No image files found in: {}".format(input_directory))