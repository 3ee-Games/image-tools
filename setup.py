#!/usr/bin/env python3

'''
setuptools-based setup module; see:

-   https://packaging.python.org/guides/distributing-packages-using-setuptools/
-   https://github.com/pypa/sampleproject
'''

from setuptools import find_packages
from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='imgtools-cli',
    version='1.0.8',
    url='https://github.com/3ee-Games/image-tools',
    author='3ee Games',
    author_email='ryguy@3ee.com',
    packages=find_packages(),
    description='a command line interface for preparing image models',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development',
    ],
    keywords='image-downloader, image-scraper, heic, hypernetwork, heic-to-png, stable-diffusion, textual-inversion, dreambooth, image-chunks, image-chunker ',
    package_data={
    },
    install_requires=[
        'beautifulsoup4==4.11.1',
        'urllib3==1.26.13',
        'Pillow==9.3.0',
        'argparse-ext',
        'pillow-heif==0.9.0',
        'opencv-python',
        'requests'
    ],

    extras_require={
    },
    entry_points={
        'console_scripts': [
            'imgtools=imgtools_cli.__main__:main',
        ],
    },
    project_urls={
        'Homepage': 'https://3ee.com',
        'Suppport': 'https://ko-fi.com/3eegames',
        'Source':  'https://github.com/3ee-Games/image-tools',
        'Tracker': 'https://github.com/3ee-Games/image-tools/issues',
    },
)

