from distutils.core import setup
from setuptools import setup, find_packages

setup(
  name = 'test_plus',
  packages = find_packages(), 
  version = '0.1.3',
  description = 'Test analysis tool for Django',
  author = 'Tolgahan Üzün',
  author_email = 'mail@tolgahanuzun.com',
  url = 'https://github.com/tolgahanuzun/test_plus',
  download_url = 'https://github.com/tolgahanuzun/test_plus/tarball/0.1.3',
  keywords = ['django', 'test', 'time'],
  install_requires = [],
  classifiers = [],
)