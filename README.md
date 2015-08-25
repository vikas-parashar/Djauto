# Django-project-generator
[![PyPI](https://img.shields.io/pypi/v/djauto.svg?style=flat-square)](https://pypi.python.org/pypi/djauto/)
[![PyPI](https://img.shields.io/pypi/pyversions/Djauto.svg?style=flat-square)](https://pypi.python.org/pypi/djauto/)

Create Django projects the easy way. From installing django to creating app for project, One command, that's all!

## Installation
In `virtualenv`simply install using pip.You can setup `virtualenv`+`virtualenvwrapper` environment using [virtualenv-burrito](https://github.com/brainsik/virtualenv-burrito).
```python
  pip install djauto
```
If you are not root user prefix `sudo`
```python
  sudo pip install djauto
```

## How to use it?
```python
  djauto PROJECT_NAME APP_NAME
```
or
```python
  sudo djauto PROJECT_NAME APP_NAME
```

## What script will do?
1. Download latest version of [Django](https://www.djangoproject.com/) using pip
2. Create a django project named "PROJECT_NAME" in current directory.
3. Create and add the app named "APP_NAME" in INSTALLED_APPS in `settings.py`.

## Todo
1. `virtualenv` integration.
1. `git` integration.


## License
[![GitHub license](https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square)](https://pypi.python.org/pypi/djauto/)
