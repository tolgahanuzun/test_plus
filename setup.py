from os import path
from distutils.core import setup
from setuptools import setup, find_packages

long_description = """Django Test Plus Extensions is a collection
  of custom extensions for the Django Framework.
  See the project page for more information:
  http://github.com/tolgahanuzun/test_plus"""

if path.isfile("readme.md"):
  with open("readme.md") as f:
      long_description = f.read()

setup(
  name = 'test_plus',
  packages = find_packages(), 
  version = '0.1.12',
  long_description_content_type="text/markdown",
  long_description=long_description,
  description = 'Test analysis tool for Django',
  author = 'Tolgahan Üzün',
  author_email = 'mail@tolgahanuzun.com',
  url = 'https://github.com/tolgahanuzun/test_plus',
  download_url = 'https://github.com/tolgahanuzun/test_plus/tarball/0.1.10',
  keywords = ['django', 'test', 'time'],
  install_requires = [],
  classifiers = [],
)
