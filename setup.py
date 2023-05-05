#!/usr/bin/python

from os import path
from setuptools import setup

from bitoptions import __version__

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-bitoptions',
    version=__version__,
    description='This project replaces several related BooleanFields with a'
                'single field and a few eye candy features.',
    long_description=long_description,
    url='https://github.com/amateja/django-bitoptions',
    author='Andrzej Mateja',
    author_email='mateja.and@gmail.com',
    license='Public Domain',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.2',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development'
    ],
    keywords='django bit options bitoptions',
    packages=['bitoptions'],
    platforms='Posix; MacOS X; Windows',
    install_requires=['django>=1.8'],
)
