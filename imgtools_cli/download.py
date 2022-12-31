import argparse
import re
import os
import urllib.request
from bs4 import BeautifulSoup
from pathlib import Path
from urllib.parse import urljoin

from urllib.parse import unquote, urlparse
from pathlib import PurePosixPath


class DownloadImages(argparse.Action):

    def __init__(self, option_strings, dest, nargs=None, **kwargs):

        super().__init__(option_strings, dest, nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):

        print('%r %r %r %r' % (namespace, values, option_string, self.nargs))
        setattr(namespace, self.dest, values)

        # html_request = 'https://www.gutenberg.org/cache/epub/67098/pg67098-images.html'
        response = urllib.request.urlopen(values[0])

        soup = BeautifulSoup(response, 'html.parser')
        images = soup.find_all('img')

        urls = [img['src'] for img in images]
        images_path = Path(__file__).parent.parent.resolve() / 'images'

        for url in urls:
            filename = re.search(r'/([\w_-]+[.](jpg|gif|png|webp))$', url)

            if not filename:
                print("Regex didn't match with the url: {}".format(url))
                continue

            if 'https' not in url or 'http' not in url:
                print(url)
                absolute_uri = values[0]
                has_extension = os.path.splitext(values[0])[1].count('.') > 0

                if has_extension:
                    print('yes')
                    #remove the last part of the url:
                    absolute_uri = '/'.join(absolute_uri.split('/')[:-1])
                   

                url = '{}/{}'.format(absolute_uri, filename.string)

            with urllib.request.urlopen(url) as url_image:
                with open(os.path.join(images_path, filename.group(1)), 'wb') as file_io:
                    file_io.write(url_image.read())

        print('Downloaded {} images to: {}'.format(len(images), images_path))
