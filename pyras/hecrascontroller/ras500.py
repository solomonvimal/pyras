
from . import ras41


class Controller(ras41.Controller):
    """HECRAS Controller vesrsion RAS500"""
    def __init__(self):
        super(Controller, self).__init__()

    def QuitRas(self):
        """
        """
        rc = self._rc
        rc.QuitRas()
