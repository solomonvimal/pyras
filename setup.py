#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from .raspy import __version__


def readme():
    return str(open('README.rst').read())

install_requires = ['pywin32']

setup(
    name='raspy',
    version=__version__,
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    keywords=["HEC-RAS HEC RAS controller windows"],
    url='https://github.com/goanpeca/raspy',
    license='MIT',
    author='Gonzalo Peña-Castellanos',
    author_email='goanpeca@gmail.com',
    maintainer='Gonzalo Peña-Castellanos',
    maintainer_email='goanpeca@gmail.com',
    description='A pythonic interface to the HECRASController using pywin32',
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
