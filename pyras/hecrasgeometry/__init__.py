
import os

import win32com.client


RASVERSION = os.environ['RAS_CONTROLLER_VERSION']
ras = __import__(RASVERSION.lower(), globals(), locals(), [], -1)


class HECRASGeometry(ras.Geometry):
    """
    """
    def __init__(self):
        super(HECRASGeometry, self).__init__()
        self._geometry = win32com.client.DispatchEx(
            "{0}.HECRASGeometry".format(RASVERSION))
