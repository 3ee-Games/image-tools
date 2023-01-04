import argparse
import argparse_ext
from imgtools_cli.download import DownloadImages
from imgtools_cli.image2chunks import ImageToChunks
from imgtools_cli.hassan_people_remover import HassanPeopleRemover
from imgtools_cli.image2png import ImageConvert
from imgtools_cli.image_resize import ImageResize

prog = 'image-tools'
current_version = '1.0.8'
        
def _parse_args():

    # init arg parser
    parser = argparse.ArgumentParser(
        prog=prog,
        description='a command line interface for image tools',
        formatter_class=argparse_ext.HelpFormatter,
        add_help=False,
    )

    # add help;
    parser.add_argument(
        '-h', '--help',
        action='help',
        help='display help message',
    )

    # add download images;
    parser.add_argument(
        '-D', '--download',
        action=DownloadImages,
        nargs=2,
        help='download all images off a given website: {url}, {input directory}',
    )

    # add image chunker;
    parser.add_argument(
        '-C', '--chunk',
        action=ImageToChunks,
        nargs=3,
        help='chunk an image into squares: {dimesion}, {input directory}, {output directory}',
    )

    # add hassan people remover
    parser.add_argument(
        '-R', '--people-remover',
        action=HassanPeopleRemover,
        nargs=2,
        help='remove images if it contains more than one person: {input directory}, {path to haarcascade_frontalface_default.xml}}',
    )

    # add image converter
    parser.add_argument(
        '-I', '--image-converter',
        action=ImageConvert,
        nargs=1,
        help='Converts all images to png: {input directory}',
    )

    # add image converter
    parser.add_argument(
        '-r', '--image-resize',
        action=ImageResize,
        nargs=5,
        help='Resizes all images with given input: {input directory}, {width}, {height}, {crop_focal_point}, {dnn_model_path} ',
    )

    parser.add_argument(
        '--version', 
        action='version', 
        version='%(prog)s' + ' ' + current_version
    )

    return parser.parse_args()

def main():
    ##  parse args;
    args = _parse_args()

if __name__ == '__main__':
    main()

