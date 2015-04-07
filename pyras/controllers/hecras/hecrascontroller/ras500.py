
from . import ras41


class Controller(ras41.Controller):
    """HECRAS Controller version RAS500"""

    def __init__(self):
        super(Controller, self).__init__()

    def Compute_Cancel(self):
        """ """
        error = self._error
        raise NotImplementedError(error)

    def Compute_Complete(self):
        """
        Returns a True value once computations have completed.

        Notes
        -----
        Can be called during computations if Blocking Mode in
        Compute_CurrentPlan is set to False.
        """
        rc = self._rc
        return rc.Compute_Complete()

    def Compute_CurrentPlan(self, BlockingModel=True):
        """
        Computes the current plan.

        Parameters
        ----------
        nmsg : int
            The number of returned messages.
        Msg : str
            Messages returned from HECRASController during computations
        BlockingMode: bool, optional
            If BlockingMode is set to False, the code will continue to be read
            while HEC-RAS is computing. Otherwise, run-time will be paused. By
            default, the HECRASController sets blocking mode to True.
        """
        rc = self._rc
        nmsg = None
        Msg = None
        res = rc.Compute_CurrentPlan(nmsg, Msg, BlockingModel)
        print(res)
        success, nmsg, Msg, other = res
        return success

    def Compute_IsStillComputing(self):
        """ """
        error = self._error
        raise NotImplementedError(error)

    def Compute_StartedFromController(self):
        """
        Indicates if computations started from HECRASController.

        Returns
        -------
        bool

        Notes
        -----
        Must set BlockingMode to False in the Compute_CurrentPlan function for
        this to work.
        """
        rc = self._rc
        res = rc.Compute_StartedFromController
        return res

    # %% Geometry
    def Geometry_BreachParamGetXML(self):
        """
        Returns a string variable listing out the dam breach parameters of the
        current plan in XML format.

        Returns
        -------
        str
        """
        rc = self._rc
        res = rc.Geometry_BreachParamGetXML()
        return res

    def Geometry_BreachParamSetXML(self, xmlText):
        """
        Sets the dam breach parameters of the current plan using XML.

        Parameters
        ----------
        xmlText : str
        """
        rc = self._rc
        rc.Geometry_BreachParamSetXML(xmlText)

    def Geometry_RatioMann(self, riv, rchUp, nUp, rchDn, nDn, ratio):
        """
        Changes Manning's Values over a specified range of cross sections by
        the input ratio.

        Parameters
        ----------
        riv : int
            The River ID.
        rchUp : int
            The upstream reach ID in the range.
        nUp : int
            The upstream node ID in the range.
        rchDn : int
            The downstream reach ID in the range.
        nDn : int
            The downstream node ID in the range.
        ratio : float
            The ratio ti apply to the Manning's n values in the range of cross
            sections.
        """
        rc = self._rc
        errmsg = ''
        res = rc.Geometry_RatioMann(riv, rchUp, nUp, rchDn, nDn, ratio, errmsg)

        return errmsg

    # %% Get
    def GetDataLocations_Input(self):
        """ """
        error = self._error
        raise NotImplementedError(error)

    def GetDataLocations_Input_count(self):
        """ """
        error = self._error
        raise NotImplementedError(error)

    def GetDataLocations_Output_count(self):
        """ """
        error = self._error
        raise NotImplementedError(error)

    # %%
    @property
    def mGeometry(self):
        """ """
        error = self._error
        raise NotImplementedError(error)

    # %% Plans
    def Plan_GetParameterUncertaintyXML(self):
        """
        Not available. Will be for Monte Carlo Analysis in future versions of
        HEC-RAS.

        Returns
        -------
        str
        """
        error = self._error
        raise NotImplementedError(error)

    def Plan_InformationXML(self):
        """
        Not available. Will be for Monte Carlo Analysis in future versions of
        HEC-RAS.

        Returns
        -------
        str
        """
        error = self._error
        raise NotImplementedError(error)

    def Plan_SetParameterUncertaintyXML(self, xmlText):
        """
        Not available. Will be for Monte Carlo Analysis in future versions of
        HEC-RAS.

        Parameters
        ----------
        xmlText : str

        Returns
        -------
        str
        """
        error = self._error
        raise NotImplementedError(error)

    # %%
    def QuitRas(self):
        """
        Closes HEC-RAS.

        Notes
        -----
        QuitRAS should be called at the end of each procedure that opens a
        HEC-RAS project. Without QuitRAS, RAS will remain open as a process
        after the main module completely executes.
        """
        rc = self._rc
        rc.QuitRas()

    def SetDataLocations(self):
        """ """
        error = self._error
        raise NotImplementedError(error)

    # %% WAT, CAVI, FRA
    def wcf_ComputePlan(self):
        """
        This function only works with WAT, CAVI, and FRA. These three HEC
        applications use the HECRASController to communicate with HEC-RAS.
        """
        raise NotImplementedError

    def wcf_CreateNewPlan(self):
        """
        This function only works with WAT, CAVI, and FRA. These three HEC
        applications use the HECRASController to communicate with HEC-RAS.
        """
        raise NotImplementedError

    def wcf_InputDataLocations_Get(self):
        """
        This function only works with WAT, CAVI, and FRA. These three HEC
        applications use the HECRASController to communicate with HEC-RAS.
        """
        raise NotImplementedError

    def wcf_InputDataLocations_Set(self):
        """
        This function only works with WAT, CAVI, and FRA. These three HEC
        applications use the HECRASController to communicate with HEC-RAS.
        """
        raise NotImplementedError

    def wcf_OutputDataLocations(self):
        """
        This function only works with WAT, CAVI, and FRA. These three HEC
        applications use the HECRASController to communicate with HEC-RAS.
        """
        raise NotImplementedError

    def wcf_SetOutputPlans(self):
        """
        This function only works with WAT, CAVI, and FRA. These three HEC
        applications use the HECRASController to communicate with HEC-RAS.
        """
        raise NotImplementedError


class ControllerDeprecated(object):
    """ """
    pass


class RASEvents:
    """Not working"""
    def HECRASController_ComputeProgressBar(self, Progress):
        """ """
        print(Progress)

    def ComputeProgressMessage(self, msg):
        """ """
        print(msg)
