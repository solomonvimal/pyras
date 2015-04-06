.. image:: https://pypip.in/version/PyRAS/badge.svg
   :target: https://pypi.python.org/pypi/QtAwesome/
   :alt: Latest PyPI version

.. image:: https://pypip.in/download/PyRAS/badge.svg
   :target: https://pypi.python.org/pypi/QtAwesome/
   :alt: Number of PyPI downloads

.. image:: https://pypip.in/py_versions/PyRAS/badge.svg
   :target: https://pypi.python.org/pypi/PyRAS/
   :alt: Supported python version
   
.. image:: https://pypip.in/license/PyRAS/badge.svg

   
PyRAS - Python River Analysis System
====================================

Description
-----------

A Python suite for working with river models. Offers an abstraction layer for 
the definition of river models and tools to call controller of different
models.

**Models supported:**

* **HEC-RAS**: Wrapper for the COM interface of the HEC-RAS controller. (windows only)

* **HEC-RAS API**: High level parser API of HEC-RAS input files. (Cross platform)

Requirements
------------

This package depends on pywin32 for accessing the HECRASController interface.

Additionally, you need to have a working version of HEC-RAS installed. 
Current support includes version 4.1.0 and 5.0.0.


Installation
------------
The following would be the eventual way of installing (not working right now): 

**The easy way:**


1. Install the anaconda distribution 


2. On the command line type:

.. code-block:: python

	pip install pyras

**The hard way:**
1. Install python

2. Download pywin32 installer from the `project webpage`_  and install.

3. On the command line type:

.. code-block:: python

	pip install pyras


	
License
-------

MIT License. Copyright 2015 - Gonzalo Peña-Castellanos


Status
------
This is a project under development and is currently in beta testing.

Although the project should be compatible with python versions 2.6, 2.7, 3.1,
3.2, 3.4 and 3.5, the project will only provide testing for 2.7, 3.3 and 3.4

project webpage