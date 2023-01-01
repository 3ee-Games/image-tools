import argparse
import re
import os
import urllib.request
from bs4 import BeautifulSoup

class DownloadImages(argparse.Action):

    def __init__(self, option_strings, dest, nargs=None, **kwargs):

        super().__init__(option_strings, dest, nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):

        print('%r %r %r %r' % (namespace, values, option_string, self.nargs))
        setattr(namespace, self.dest, values)

        response = urllib.request.urlopen(values[0])
        input_directory = values[1]

        soup = BeautifulSoup(response, 'html.parser')
        images = soup.find_all('img')

        urls = [img['src'] for img in images]

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
                    #remove the last part of the url:
                    absolute_uri = '/'.join(absolute_uri.split('/')[:-1])

                url = '{}/{}'.format(absolute_uri, filename.string)

            with urllib.request.urlopen(url) as url_image:
                with open(os.path.join(input_directory, filename.group(1)), 'wb') as file_io:
                    file_io.write(url_image.read())

        print('Downloaded {} images to: {}'.format(len(images), input_directory))
