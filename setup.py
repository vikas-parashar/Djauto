from setuptools import setup

setup(name='djauto',
      version='0.1',
      description='Django project generator',
      url='https://github.com/vikas-parashar/django-project-automator',
      author='Vikas Parashar',
      author_email='svnitvikas@gmai.com',
      license='MIT',
      packages=['djauto'],
      entry_points = {
        'console_scripts': ['djauto=djauto.auto:main'],
        },
      zip_safe=False)
