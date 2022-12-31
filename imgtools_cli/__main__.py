import argparse
import argparse_ext
import download
import heic2png
import image2chunks

##  program name;
prog = 'image-tools'
current_version = '1.0.0'
download_images = download.DownloadImages
heic_to_png = heic2png.HeicToPng
image_to_chunks = image2chunks.ImageToChunks
        
def _parse_args():

    ##  init arg parser;
    parser = argparse.ArgumentParser(
        prog=prog,
        description='a command line interface for image tools;',
        formatter_class=argparse_ext.HelpFormatter,
        add_help=False,
    )

    ##  add help;
    parser.add_argument(
        '-h', '--help',
        action='help',
        help='display help message;',
    )

    ##  add download images;
    parser.add_argument(
        '-D', '--download',
        action=download_images,
        nargs=1,
        help='download all images off a given website: {url};',
    )

    ##  add heic to png converter;
    parser.add_argument(
        '-P', '--heicpng',
        action=heic_to_png,
        nargs=1,
        help='convert heic to png format: {input directory};',
    )

    ##  add image chunker;
    parser.add_argument(
        '-C', '--chunk',
        action=image_to_chunks,
        nargs=3,
        help='chunk an image into squares: {dimesion}, {input directory}, {output directory};',
    )

    parser.add_argument(
        '--version', 
        action='version', 
        version='%(prog)s' + ' ' + current_version
    )

    ##  parse args;
    args = parser.parse_args()

    return args

def main():
    ##  parse args;
    args = _parse_args()

if __name__ == '__main__':
    main()

