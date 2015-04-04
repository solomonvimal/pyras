import os

import win32com.client

from .. import hecrasgeometry

RASVERSION = os.environ['RAS_CONTROLLER_VERSION']
ras = __import__(RASVERSION.lower(), globals(), locals(), [], -1)


class HECRASController(ras.Controller, ras.ControllerDeprecated):
    """
    """
    def __init__(self):
        super(HECRASController, self).__init__()
        self._rc = win32com.client.DispatchEx(
            "{0}.HECRASController".format(RASVERSION))
        self._ras_version = RASVERSION
        self._error = 'Not available in version "{}" of controller'.format(
            self._ras_version)

        self._geometry = hecrasgeometry.HECRASGeometry()
