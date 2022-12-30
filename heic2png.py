#Description: Convert HEIC to PNG

import os
from PIL import Image
from pathlib import Path
import pillow_heif

images_path = Path(__file__).parent.resolve() / 'images'
extensions_supported = ('.heic', 'heica')

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

