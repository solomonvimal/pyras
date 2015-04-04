
import os

import win32com.client


PYRASVERSION = os.environ['PYRASVERSION']
ras = __import__(PYRASVERSION.lower(), globals(), locals(), [], -1)


class HECRASGeometry(ras.Geometry):
    """
    """
    def __init__(self):
        super(HECRASGeometry, self).__init__()
        self._geometry = win32com.client.Dispatch(
            "{0}.HECRASGeometry".format(PYRASVERSION))
