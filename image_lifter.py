import re
import os
import requests
from bs4 import BeautifulSoup
from pathlib import Path

html_request = 'https://www.gutenberg.org/cache/epub/67098/pg67098-images.html'
response = requests.get(html_request)

soup = BeautifulSoup(response.text, 'html.parser')
images = soup.find_all('img')

urls = [img['src'] for img in images]
images_path = Path(__file__).parent.resolve() / 'images'

for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)

    if not filename:
        print("Regex didn't match with the url: {}".format(url))
        continue

    with open(os.path.join(images_path, filename.group(1)), 'wb') as file_io:
        # If the url is relative, make it absolute by joining the base url
        if 'https' not in url or 'http' not in url:
            url = '{}{}'.format(html_request, url)

        response = requests.get(url)
        file_io.write(response.content)
