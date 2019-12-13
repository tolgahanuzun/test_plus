import os
from distutils.core import setup
from setuptools import setup, find_packages

BASE_DIR = os.path.dirname(__file__)
f = open(os.path.join(BASE_DIR, "readme.md"))
readme = f.read()
f.close()

setup(
  name = 'test_plus',
  packages = find_packages(), 
  version = '0.1.10',
  long_description=readme,
  long_description_content_type="text/markdown",
  description = 'Test analysis tool for Django',
  author = 'Tolgahan Üzün',
  author_email = 'mail@tolgahanuzun.com',
  url = 'https://github.com/tolgahanuzun/test_plus',
  download_url = 'https://github.com/tolgahanuzun/test_plus/tarball/0.1.10',
  keywords = ['django', 'test', 'time'],
  install_requires = [],
  classifiers = [],
)