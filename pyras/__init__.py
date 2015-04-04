"""
PyRAS
=====


"""

import os
import win32com.client

from .tools import get_registered_typelibs

__version__ = '0.1.0'

__registered_type_libs__ = get_registered_typelibs()
__supported_versions__ = ['RAS41', 'RAS500']
__available_versions__ = []

if len(__registered_type_libs__) > 0:

    for ras_version in __supported_versions__:
        try:
            win32com.client.Dispatch("{0}.HECRASFlow".format(ras_version))
            __available_versions__.append(ras_version)
        except Exception:
            pass

    os.environ['RAS_CONTROLLER_VERSION'] = __available_versions__[-1]

    from .hecrascontroller import HECRASController
    from .hecrasgeometry import HECRASGeometry
    from .pyras import PyRAS

    # Cleaning the namespace
    globals().pop('hecrasgeometry')
    globals().pop('hecrascontroller')
    globals().pop('os')
    globals().pop('pyras')
    globals().pop('tools')
    globals().pop('win32com')
else:
    error = '"HEC River Analysis System" type library not found. ' \
            'Please install HEC-RAS'
    raise Exception(error)
