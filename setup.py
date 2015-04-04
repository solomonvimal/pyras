#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from .pyras import __version__


def readme():
    return str(open('README.rst').read())

# Check that pywin32 is installed otherwise raise error.
install_requires = []

setup(
    name='pyras',
    version=__version__,
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    keywords=["HEC-RAS HEC RAS controller windows"],
    url='https://github.com/goanpeca/raspy',
    license='MIT',
    author='Gonzalo Peña-Castellanos',
    author_email='goanpeca@gmail.com',
    maintainer='Gonzalo Peña-Castellanos',
    maintainer_email='goanpeca@gmail.com',
    description='Python Wrapper of HEC RAS COM interface',
    long_description=readme(),
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Win32 (MS Windows)',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Widget Sets'])
