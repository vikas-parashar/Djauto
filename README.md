# Django-project-generator
[![PyPI](https://img.shields.io/pypi/v/djauto.svg?style=flat-square)](https://pypi.python.org/pypi/djauto/)
[![PyPI](https://img.shields.io/pypi/pyversions/Djauto.svg?style=flat-square)](https://pypi.python.org/pypi/djauto/)

Create Django projects the easy way. From installing django to creating github repository for project, One command, that's all!

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

### What does above command do?
1. Downloads latest version of [Django](https://www.djangoproject.com/) using pip
2. Creates a django project named "PROJECT_NAME" in current directory.
3. Creates and add the app named "APP_NAME" in INSTALLED_APPS in `settings.py`.
4. Asks if you want to create github repository. If yes, then
	1. Asks for github username.
	2. Creates repo named PROJECT_NAME.
	3. Asks for short description.
	4. Asks for password.
	5. Adds all file and push it on github.
5. We're done!

## Todo
- ~~`git` integration.~~
- `virtualenv` integration.
- ~~python 3.x support.~~


## License
[![GitHub license](https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square)](https://pypi.python.org/pypi/djauto/)
