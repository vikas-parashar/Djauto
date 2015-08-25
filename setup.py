from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='djauto',
      version='1.0.1',
      description='Django project generator',
      long_description=readme(),
      url='https://github.com/vikas-parashar/django-project-generator',
      author='Vikas Parashar',
      author_email='svnitvikas@gmai.com',
      license='MIT',
      classifiers=[
              'Development Status :: 3 - Alpha',
              'Environment :: Web Environment',
              'Intended Audience :: Developers',
              'Operating System :: OS Independent',
              'Programming Language :: Python',
              'Topic :: Software Development',
              'Natural Language :: English',
              'Programming Language :: Python :: 2.6',
              'Programming Language :: Python :: 2.7',
          ],
      keywords='django, python, django-packages, packages',
      packages=['djauto'],
      entry_points = {
        'console_scripts': ['djauto=djauto.auto:main'],
        },
      zip_safe=False)
