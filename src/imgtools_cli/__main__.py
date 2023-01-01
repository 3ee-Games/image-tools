import argparse
import argparse_ext
from imgtools_cli.download import DownloadImages
from imgtools_cli.heic2png import HeicToPng
from imgtools_cli.image2chunks import ImageToChunks

##  program name;
prog = 'image-tools'
current_version = '1.0.3'
        
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
        action=DownloadImages,
        nargs=2,
        help='download all images off a given website: {url}, {input directory};',
    )

    ##  add heic to png converter;
    parser.add_argument(
        '-P', '--heicpng',
        action=HeicToPng,
        nargs=1,
        help='convert heic to png format: {input directory};',
    )

    ##  add image chunker;
    parser.add_argument(
        '-C', '--chunk',
        action=ImageToChunks,
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

