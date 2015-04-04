"""
PyRAS
=====

Provides
"""

import os

from .tools import get_registered_typelibs

__version__ = '0.1.0'

__registered_type_libs__ = get_registered_typelibs()

if len(__registered_type_libs__) > 0:
    os.environ['PYRASVERSION'] = 'RAS41'
    os.environ['PYRASVERSION'] = 'RAS500'

    from .hecrascontroller import HECRASController
    from .hecrasgeometry import HECRASGeometry
    from .pyras import PyRAS

    # Cleaning the namespace
    globals().pop('hecrasgeometry')
    globals().pop('hecrascontroller')
    globals().pop('os')
    globals().pop('pyras')
    globals().pop('tools')
else:
    error = '"HEC River Analysis System" type library not found. Please install HEC-RAS'
    Exception(error)
