
import os

import win32com.client


def HECRASGeometry(ras_version=None):
    """ """
    if ras_version is None:
        ras_version = os.environ['RAS_CONTROLLER_VERSION']

    ras = __import__(ras_version.lower(), globals(), locals(), [], -1)

    class RASGeometry(ras.Geometry):
        """
        """
        def __init__(self, ras_version):
            super(RASGeometry, self).__init__()
            self._geometry = win32com.client.DispatchEx(
                "{0}.HECRASGeometry".format(ras_version))

    return RASGeometry(ras_version)
