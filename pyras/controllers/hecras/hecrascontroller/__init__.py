import os

import win32com.client

from .. import hecrasgeometry
from .... import tools


def HECRASController(ras_version=None):
    """ """
    if ras_version is None:
        ras_version = os.environ['RAS_CONTROLLER_VERSION']
    elif ras_version not in tools.get_supported_versions():
        error = 'ras_version "{}" not supported.'.format(ras_version)
        raise Exception(error)

    ras = __import__(ras_version.lower(), globals(), locals(), [], -1)

    class RASController(ras.Controller, ras.ControllerDeprecated):
        """
        """
        def __init__(self, ras_version):
            super(RASController, self).__init__()
            self._rc = win32com.client.DispatchEx(
                "{0}.HECRASController".format(ras_version))
            self._ras_version = ras_version
            self._error = 'Not available in version "{}" of controller'.format(
                self._ras_version)

            self._geometry = hecrasgeometry.HECRASGeometry(ras_version)
            self._runtime = tools.Runtime(self)

        def runtime(self):
            """ """
            return self._runtime

        def close(self):
            self._runtime.close()

    return RASController(ras_version)
