import re
import os
import urllib.request
from bs4 import BeautifulSoup
from pathlib import Path

host = 'https://www.gutenberg.org/cache/epub/67098'
html_request = 'https://www.gutenberg.org/cache/epub/67098/pg67098-images.html'
response = urllib.request.urlopen(html_request)

soup = BeautifulSoup(response, 'html.parser')
images = soup.find_all('img')

urls = [img['src'] for img in images]
images_path = Path(__file__).parent.resolve() / 'images'

for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png|webp))$', url)

    if not filename:
        print("Regex didn't match with the url: {}".format(url))
        continue

    if 'https' not in url or 'http' not in url:
        url = '{}/{}'.format(host, filename.string)

    with urllib.request.urlopen(url) as url_image:
        with open(os.path.join(images_path, filename.group(1)), 'wb') as file_io:
            file_io.write(url_image.read())
