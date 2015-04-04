import os

import win32com.client

from .. import hecrasgeometry

PYRASVERSION = os.environ['PYRASVERSION']
ras = __import__(PYRASVERSION.lower(), globals(), locals(), [], -1)


class HECRASController(ras.Controller):
    """
    """
    def __init__(self):
        super(HECRASController, self).__init__()
        self._rc = win32com.client.Dispatch(
            "{0}.HECRASController".format(PYRASVERSION))

        self._geometry = hecrasgeometry.HECRASGeometry()
