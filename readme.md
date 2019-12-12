# Django Test Plus Extensions
[![License](https://img.shields.io/pypi/l/django-extensions.svg)](https://raw.githubusercontent.com/tolgahanuzun/test_plus/master/LICENSE) [![](https://img.shields.io/pypi/v/test-plus.svg)](https://pypi.org/project/test_plus/)

Django Test Plus Extensions is a collection of custom extensions for the Django Framework.

## Getting Started

Django Test Plus Extension is an advanced tool for Django tests. Motivation; This is a detailed analysis of the atomic parts of Django tests. In short, each running test understands how long it runs.

## Requirements

- Django > 1.11

## Getting

You can get Django Extensions by using pip:

```
$ pip install test_plus
```

If you want to install it from source, grab the git repository from GitHub and run setup.py:

```
$ git clone git://github.com/tolgahanuzun/test_plus.git
$ cd test_plus
$ python setup.py install
```

## Installing

To enable django_extensions in your project you need to add it to INSTALLED_APPS in your projects settings.py file:

```
INSTALLED_APPS = (
    ...
    'test_plus',
    ...
)
```
## Using

It takes the same parameter in Django tests.

```
python manage.py test_plus
```

or

```
python manage.py test_plus app_name.test.test_file -k -v 2
```

### Result

![](https://raw.githubusercontent.com/tolgahanuzun/test_plus/master/test.png)

## Support

Inspired by the Django Extensions package. It is free and open to improvement. I can improve if you tell me your needs. You can also support the development.