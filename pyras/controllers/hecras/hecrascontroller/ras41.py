"""
"""
import os
import os.path as osp


class Controller(object):
    """HECRAS Controller vesrsion RAS41"""

    # %% Compute
    def Compute_Cancel(self):
        """
        """
        rc = self._rc
        rc.Compute_Cancel()

    def Compute_CurrentPlan(self):
        """
        Computes the current plan.

        Parameters
        ----------
        nmsg : int
            The number of returned messages.
        msg : str
            Messages returned from HECRASController during computations
        """
        rc = self._rc
        nmsg = None
        msg = None
        res = rc.Compute_CurrentPlan(nmsg, msg)
        print(res, nmsg, msg)
        return res

    def Compute_HideComputationWindow(self):
        """
        Set the computation window to be hidden during computations.

        Notes
        -----
        This should be called before Compute_CurrentPlan.
        """
        rc = self._rc
        rc.Compute_HideComputationWindow()

    def Compute_IsStillComputing(self):
        """
        Returns True if a computation is still in execution.

        Returns
        -------
        bool
        """
        rc = self._rc
        res = rc.Compute_IsStillComputing()
        return res

    def Compute_ShowComputationWindow(self):
        """
        Sets the computation window to be visible during computations.

        Notes
        -----
        This hould be called before Compute_CurrentPlan. Because by default the
        RAS Controller shows the Computation Window, this is not necessary
        unless the Computation Window was already hidden in a previous line of
        code.
        """
        rc = self._rc
        rc.Compute_ShowComputationWindow()

    def Compute_WATPlan(self):
        """
        Computes a WAT plan.

        Returns
        -------
        bool

        Notes
        -----
        For WAT only.
        """
        rc = self._rc
        res = rc.Compute_WATPlan()
        return res

    # %% Create
    def Create_WATPlanName(self, HECRASBasePlanName, SimulationName):
        """
        Returns a WAT Plan Name, based i the RAS base plan name and the
        simulation.

        Parameters
        ----------
        HECRASBasePlanName : str

        SimulationName : str

        Notes
        -----
        For WT only.
        """
        rc = self._rc
        res = rc.Create_WATPlanName(HECRASBasePlanName, SimulationName)
        return res

    # %% Current
    def CurrentGeomFile(self):
        """
        Indicates the current HEC-RAS geometry file and its path.

        Returns
        -------
        str
        """
        rc = self._rc
        res = rc.CurrentGeomFile()
        return res

    def CurrentPlanFile(self):
        """
        Indicates the current HEC-RAS plan file and its path.

        Returns
        -------
        str
        """
        rc = self._rc
        res = rc.CurrentPlanFile()
        return res

    def CurrentProjectFile(self):
        """
        Indicates the current HEC-RAS project file and its path.

        Returns
        -------
        str
        """
        rc = self._rc
        res = rc.CurrentProjectFile()
        return res

    def CurrentProjectTitle(self):
        """
        Indicates the current HEC-RAS project title.

        Returns
        -------
        str
        """
        rc = self._rc
        res = rc.CurrentProjectTitle()
        return res

    def CurrentSteadyFile(self):
        """
        Indicates the current HEC-RAS steady flow file and its path.

        Returns
        -------
        str
        """
        rc = self._rc
        res = rc.CurrentSteadyFile()
        return res

    def CurrentUnSteadyFile(self):
        """
        Indicates the current HEC-RAS unstead flow file and its path.

        Returns
        -------
        str
        """
        rc = self._rc
        res = rc.CurrentUnSteadyFile()
        return res

    # %% Edit Add
    def Edit_AddBC(self, river, reach, rs):
        """
        Add a bridge/culvert.

        Parameters
        ----------
        river : str
            The river name to add the bridge/culvert section to.
        reach : str
            The reach name  to add the bridge/culvert to.
        rs : str
            The river station of the new bridge/culvert .

        Notes
        -----
        The Edit_BC method must be included in the code after Edit_AddBC, and
        must cal the newly bridge/culvertin order for it to be saved to the
        geometry file. Edit_BC brings up the Bridge/Culvert editor. No edits
        are necessary to save the new bridge/culvert, the editor has to just
        open and close. Without Edit_BC, once the code has been completed and
        the HECRASController closes, HEC-RAS will close and the newly added
        cross section will be lost.
        """
        rc = self._rc
        errmsg = ''
        res = rc.Edit_AddBC(river, reach, rs, errmsg)
        river, reach, rs, errmsg = res

    def Edit_AddIW(self, river, reach, rs):
        """
        Add a inline structure section.

        Parameters
        ----------
        river : str
            The river name to add the inline structure to.
        reach : str
            The reach name  to add the inline structure to.
        rs : str
            The river station of the new inline structure.

        Notes
        -----
        The Edit_IW method must be included in the code after Edit_AddIW, and
        must cal the newly added inline structure in order for it to be saved
        to the geometry file. Edit_IW brings up the Inline Structure Editor.
        No edits are necessary to save the new inline structure, the editor
        has to just open and close. Without Edit_IW, once the code has been
        completed and the HECRASController closes, HEC-RAS will close and the
        newly added cross section will be lost.
        """
        rc = self._rc
        errmsg = ''
        res = rc.Edit_AddIW(river, reach, rs, errmsg)
        river, reach, rs, errmsg = res

    def Edit_AddLW(self, river, reach, rs):
        """
        Add a lateral structure.

        Parameters
        ----------
        river : str
            The river name to add the lateral structure to.
        reach : str
            The reach name  to add the lateral structure to.
        rs : str
            The river station of the new lateral structure.

        Notes
        -----
        The Edit_LW method must be included in the code after Edit_AddLW, and
        must cal the newly added lateral structure in order for it to be saved
        to the geometry file. Edit_LW brings up the Lateral Structure Editor.
        No edits are necessary to save the new lateral structure, the editor
        has to just open and close. Without Edit_LW, once the code has been
        completed and the HECRASController closes, HEC-RAS will close and the
        newly added cross section will be lost.
        """
        rc = self._rc
        errmsg = ''
        res = rc.Edit_AddLW(river, reach, rs, errmsg)
        river, reach, rs, errmsg = res

    def Edit_AddXS(self, river, reach, rs):
        """
        Add a cross section.

        Parameters
        ----------
        river : str
            The river name to add the cross section to.
        reach : str
            The reach name  to add the cross section to.
        rs : str
            The river station of the new cross setion.

        Notes
        -----
        The Edit_XS method must be included in the code after Edit_AddXS, and
        must cal the newly added cross section in order for it to be saved to
        the geometry file. Edit_XS brings up the cross section editor. No edits
        are necessary to save the new cross section, the editor has to just
        open and close. Without Edit_XS, once the code has been completed and
        the HECRASController closes, HEC-RAS will close and the newly added
        cross section will be lost.
        """
        rc = self._rc
        errmsg = ''
        res = rc.Edit_AddXS(river, reach, rs, errmsg)
        river, reach, rs, errmsg = res

    # %% Edit
    def Edit_BC(self, river, reach, rs):
        """
        Opens the Bridge/Culvert Editor and displays the selected river
        station.

        Parameters
        ----------
        river : str
            The river name of the bridge/culvert structure to edit.
        reach : str
            The reach name of the bridge/culvert to edit.
        rs : str
            The river station of the bridge/culvert to edit.

        Notes
        -----
        Run-time is paused while edits are made in the Bridge/Culvert Editor.
        editor. Once the Bridge/Culvert Editor is closed, run-time resumes.
        """
        rc = self._rc
        rc.Edit_BC(river, reach, rs)
        self._runtime.pause_bc()

    def Edit_GeometricData(self):
        """
        Opens the Geometry Data window.

        Notes
        -----
        Run-time is paused while edits are made in the Geometry Data Window.
        Once the Geometry Data Window is closed, run-time resumes.
        """
        rc = self._rc
        rc.Edit_GeometricData()
        self._runtime.pause_geo()

    def Edit_IW(self, river, reach, rs):
        """
        Opens the Inline Structure Editor and displays the selected river
        station.

        Parameters
        ----------
        river : str
            The river name of the inline structure to edit.
        reach : str
            The reach name of the inline structure to edit.
        rs : str
            The river station of the inline structure to edit.

        Notes
        -----
        Run-time is paused while edits are made in the inline structure
        editor. Once the Lateral Structure Editor is closed, run-time resumes.
        """
        rc = self._rc
        rc.Edit_LW(river, reach, rs)
        self._runtime.pause_iw()

    def Edit_LW(self, river, reach, rs):
        """
        Opens the Lateral Structure Editor and displays the selected river
        station.

        Parameters
        ----------
        river : str
            The river name of the lateral structure to edit.
        reach : str
            The reach name of the lateral structure to edit.
        rs : str
            The river station of the lateral structure to edit.

        Notes
        -----
        Run-time is paused while edits are made in the lateral structure
        editor. Once the Lateral Structure Editor is closed, run-time resumes.
        """
        rc = self._rc
        rc.Edit_LW(river, reach, rs)
        self._runtime.pause_lw()

    def Edit_MultipleRun(self):
        """
        Opens the Run Multiple Plans Dialog.

        Notes
        -----
        Run-time does not pause while the Run Multiple Plans Dialog is open, so
        it is suggested that a message box be added after Edit_MultipleRun,
        so that the method does not end and close the window before the user
        can check plans.
        """
        rc = self._rc
        rc.Edit_MultipleRun()
        self._runtime.pause_multiple()

    def Edit_PlanData(self):
        """
        Opens the Steady or Unsteady Flow Analysis windows for edits (whichever
        is current).

        Notes
        -----
        Run-time does not pause while the Unsteady Flow Editor is open, so it
        is suggested that a message box be added after Edit_UnsteadyFlowData,
        so that the method does not end and close the window before the user
        can make edits.
        """
        rc = self._rc
        rc.Edit_PlanData()
        self._runtime.pause_plan()

    def Edit_QuasiUnsteadyFlowData(self):
        """
        Opens the Unsteady Flow Editor

        Notes
        -----
        Run-time does not pause while the Quasi-Unsteady Flow Editor is open,
        so it is suggested that a message box be added after
        Edit_QuasiUnsteadyFlowData, so that the method does not end and close
        the window before the user can make edits.
        """
        rc = self._rc
        rc.Edit_QuasiUnsteadyFlowData()
        self._runtime.pause_quasi()

    def Edit_SedimentData(self):
        """
        Opens the Sediment Data Editor.

        Notes
        -----
        Run-time does not pause while the Sediment Data Editor is open, so it
        is suggested that a message box be added after Edit_SedimentData, so
        that the method does not end and close the window before the user can
        make edits.
        """
        rc = self._rc
        rc.Edit_SedimentData()
        self._runtime.pause_sediment()

    def Edit_SteadyFlowData(self):
        """
        Opens the Steady Flow Editor.

        Notes
        -----
        Run-time does not pause while the Steady Flow Editor is open, so it
        is suggested that a message box be added after Edit_SteadyFlowData,
        so that the method does not end and close the window before the user
        can make edits.
        """
        rc = self._rc
        rc.Edit_SteadyFlowData()
        self._runtime.pause_steady()

    def Edit_UnsteadyFlowData(self):
        """
        Opens the Unsteady Flow Editor.

        Notes
        -----
        Run-time does not pause while the Unsteady Flow Editor is open, so it
        is suggested that a message box be added after Edit_UnsteadyFlowData,
        so that the method does not end and close the window before the user
        can make edits.
        """
        rc = self._rc
        rc.Edit_UnsteadyFlowData()
        self._runtime.pause_unsteady()

    def Edit_WaterQualityData(self):
        """
        Opens the UWater Quality Data Editor.

        Notes
        -----
        Run-time does not pause while the Water Quality Data Editor is open, so
        it is suggested that a message box be added after Edit_WaterQualityData
        so that the method does not end and close the window before the user
        can make edits.
        """
        rc = self._rc
        rc.Edit_WaterQualityData()
        self._runtime.pause_quality()

    def Edit_XS(self, river, reach, rs):
        """
        Opens the Cross Section Editor and displays the selected cross section.

        Parameters
        ----------
        river : str
            The river name of the cross section.
        reach : str
            The reach name of the cross section.
        rs : str
            The river station of the cross section.

        Notes
        -----
        Run-time is paused while edits are made in the Cross Section Editor.
        Once the Cross Section Editor is closed, run-time resumes.
        """
        rc = self._rc
        res = rc.Edit_XS(river, reach, rs)
        self._runtime.pause_xs()

    # %% Export
    def ExportGIS(self):
        """
        Export HEC-RAS results to an *.sdf export file that can be read into
        GIS using HEC-GeoRAS.

        Notes
        -----
        The Export GIS Editos does NOT open when this subroutine is called.
        HECRASController uses whatever user inputs (i.e. profiles to export,
        results to export, types of geometric data to export, etc.) have
        already been set in the Editor and only wirtes the *.sdf export file.
        """
        rc = self._rc
        rc.ExportGIS()

    # %% Geometry
    def Geometry(self):
        """
        Returs the HECRASGeometry instance.

        Notes
        -----
        See HECRASGeometry class for specific methods.
        """
        return self._geometry

    def Geometery_GISImport(self, title, Filename):
        """
        Imports geometry data from a *.sdf import file.

        Parameters
        ----------
        title : str
            The title of the new geometry file to import.
        Filename : str
            The path and filename of the sdf file.

        Notes
        -----
        The Import Geometry Data from GIS Editor does NOT open when this method
        is called. HECRASController uses default settings for importing. A new
        geometry file is created with this subroutine and al streams and nodes
        are imported. Note the misspelling "Geometerey"in the name of this
        method.
        """
        rc = self._rc
        rc.Geometery_GISImport(title, Filename)

    def Geometry_GetGateNames(self, river, reach, station):
        """Returns a list of gates names.

        Parameters
        ----------
        river : str
            The river name of the inline structure.
        reach : str
            The reach name of the inline structure.
        station : str
            The river station of the inline structure.
        """
        rc = self._rc
        res = rc.Geometry_GetGateNames(river, reach, station)
        river, reach, station, ngate, GateNames, errmsg = res

        # Return an empty list or return None?
        if GateNames is None:
            GateNames = []

        result = (ngate, list(GateNames))

        if errmsg != '':
            raise Exception(errmsg)

        return result

    def Geometry_GetGML(self, geomfilename):
        """Returns the GML file txt for the current geometry file.

        Parameters
        ----------
        geomfilename : str
            The name of the geometry file.
        """
        # FIXME: Not working
        rc = self._rc
        res = rc.Geometry_GetGML(geomfilename)
        return 

    def Geometry_GetNode(self, riv, rch, rs):
        """Returns the node ID of a selected node.

        Parameters
        ----------
        riv : int
            The river ID of the node.
        rch : int
            The reach ID of the node.
        rs : str
            The river station of the node.

        Notes
        -----
        Node can be any geometric component with a River Station (i.e. cross
        section, bridge/culvert, inline structure, lateral structure, multiple
        opening).
        """
        # Input check
        if not isinstance(riv, int) or riv <= 0:
            raise Exception
        if not isinstance(rch, int) or rch <= 0:
            raise Exception
        if not isinstance(rs, str):
            raise Exception

        rc = self._rc
        res = rc.Geometry_GetNode(riv, rch, rs)
        node_id, riv, rch, rs = res

        if node_id == 0:
            node_id = None

        return node_id

    def Geometry_GetNodes(self, riv, rch):
        """
        Returns a tuple of nodes and node types in a specified river and reach.

        Parameters
        ----------
        riv : int
            The river ID.
        rch : int
            The reach ID.

        Returns
        -------
        rs : tuple of str
            The tuple of river stations representing nodes on the selected
            river/reach.
        NodeType : tuple str
            The tuple of node types on the selected
            river/reach.
        """
        rc = self._rc
        geo = self.Geometry()
        nRS = geo.nNode(riv, rch)
        rs = (float('nan'),)*(nRS + 1)
        NodeType = (float('nan'),)*(nRS + 1)
        res = rc.Geometry_GetNodes(riv, rch, nRS, rs, NodeType)
        riv, rch, nRS, rs, NodeType = res

        return rs, NodeType

    def Geometry_GetReaches(self, riv):
        """
        Returns a list of the reach names in a given river id.

        Parameters
        ----------
        riv : int
            The river ID.

        Returns
        -------
        nReach : int
            The number of reaches in tge selected river.
        reach : str
            The names of the reaches on the selected river
        """
        # Input check
        if not isinstance(riv, int):
            raise Exception

        nReach, reach = 0, tuple()
        rc = self._rc
        res = rc.Geometry_GetReaches(riv, nReach, reach)
        riv, nReach, reach = res

        # Return an empty list or return None?
        if reach is None:
            reach = []

        result = (nReach, list(reach))

        return result

    def Geometry_GetRivers(self):
        """
        Returns a list of rivers names.

        Returns
        ----------
        nRiver : int
            The number of rivers.
        river : list of str
            The list of the names of the rivers.
            """
        rc = self._rc
        nRiver, river = 0, tuple()
        res = rc.Geometry_GetRivers(nRiver, river)
        nRiver, river = res

        if river is not None:
            result = nRiver, list(river)
        else:
            result = 0, []

        return result

    def Geometry_SetMann(self, river, reach, rs, nMann, Mann_n, Station):
        """
        Set the Manning's Values, by stationing, for a cross section.

        Parameters
        ----------
        river : str
            The river to set Manning's n Values.
        reach : str
            The reach to set Manning's n Values.
        rs : str
            The river station of the cross section to set Manning's n values.
        nMann : int
            The number of Manning's n values to add.
        Mann_n : list/tuple of float
            A list of the Manning's n values to add.
        Station : list/tuple of float
            A list of the stationing values of the Manning's n breakpoints.

        Notes
        -----
        If station values don't exist in the station elevation table,
        HECRASCntroller will use the closest station to apply the n value to.

        Python: This method takes care of 0-based indexing.
        """
        rc = self._rc
        errmsg = ''

        # Adjust to 0-based indexing and force the use of tuples
        Mann_n = tuple([0] + list(Mann_n))
        Station = tuple([0] + list(Station))

        res = rc.Geometry_SetMann(river, reach, rs, nMann, Mann_n, Station,
                                  errmsg)

        flag, river, reach, rs, nMann, Mann_n, Station, errmsg = res

        if errmsg != '':
            raise Exception(errmsg)

        return flag

    def Geometry_SetMann_LChR(self, river, reach, rs, MannLOB, MannChan,
                              MannROB):
        """
        Sets the Manning's n Values, by left verbank, main channel, and right
        overbank, for a cross section.

        Parameters
        ----------
        river : str
            The river to set Manning's n Values.
        reach : str
            The reach to set Manning's n Values.
        rs : str
            The river station of the cross section to set Manning's n Values.
        MannLOB : float
            Manning's n Value for the Left Overbank,
        MannChan : float
            Manning's n Value for the Main Channel.
        MannROB : float
            Manning's n Value for the Right Overbank.
        """
        rc = self._rc
        errmsg = ''
        res = rc.Geometry_SetMann_LChR(river, reach, rs, MannLOB, MannChan,
                                       MannROB, errmsg)
        return res

    def Geometry_SetSAArea(self, SAName, Area):
        """
        Set the Area of a Storage Area.

        Parameters
        ----------
        SAName : str
            The name of the Storage Area.
        Area : float
            The area to set the Storage Area with.

        Notes
        -----
        The Geometry_SetSAArea method works in runtime, sets the area, and
        returns a True value. But, you must ShowRAS and then save the geometry.
        Otherwise changes to SA area are not saved. Also, make sure to NOT
        close RAS during run time. The area ust already exists!

        Python: this method handles the save automatically.
        """
        # TODO: using the parsed filed, look for valid areas and check
        # against this
        rc = self._rc
        errmsg = ''
        res = rc.Geometry_SetSAArea(SAName, Area, errmsg)
        geo = self.Geometry()
        geo.Save()

        return res

    # %% Get

    def GetDataLocations_Input(self, PlanTitle):
        """

        Parameters
        ----------
        PlanTitle : str
            The name of the plan.

        Returns
        -------
        LocationDesciptions : list of str

        DSSFiles : list of str

        DSSPathnames : list of str
        """
        rc = self._rc
        errmsg = ''
        LocationDesciptions = []
        DSSFiles = []
        DSSPathnames = []
        res = rc.GetDataLocations_Input(PlanTitle, LocationDesciptions,
                                        DSSFiles, DSSPathnames, errmsg)

        return res

    def GetDataLocations_Input_count(self, PlanTitle):
        """

        Parameters
        ----------
        PlanTitle : str
            The name of the plan.

        Returns
        -------
        int
        """
        rc = self._rc
        errmsg = ''
        res = rc.GetDataLocations_Input_count(PlanTitle, errmsg)

        return res

    def GetDataLocations_Output(self, planTitle):
        """
        Gets all stage and flow hydrograh output locations, including their dss
        file names and dss paths.

        Parameters
        ----------
        planTitle : str
            The name of the plan.

        Returns
        -------
        DSSFiles : list of str
            The list of DSS filenames.
        DSSPathnames : list of str
            The list of DSS Pathnames.
        """
        rc = self._rc
        errmsg = ''
        DSSFiles = []
        DSSPathnames = []
        res = rc.Geometry_SetSAArea(planTitle, DSSFiles, DSSPathnames, errmsg)

        return res

    def GetDataLocations_Output_count(self, PlanTitle):
        """

        Parameters
        ----------
        PlanTitle : str
            The name of the plan.

        Returns
        -------
        int
        """
        rc = self._rc
        errmsg = ''
        res = rc.GetDataLocations_Output_count(PlanTitle, errmsg)

        return res


    # %% Versions
    def GetRASVersion(self):
        """
        Returns the version number and date of HEC-RAS.

        Notes
        -----
        Works the same as HECRASVersion.
        """
        rc = self._rc
        version = rc.GetRASVersion()
        return version

    def HECRASVersion(self):
        """
        Returns the version number and date of HEC-RAS.

        Notes
        -----
        Works the same as GetRASVersion.
        """
        rc = self._rc
        version = rc.HECRASVersion()
        return version

    # %% Map
    def Map_Add(self, Filename):
        """
        Adds a map to the Geometry Schematic.

        Parameters
        ----------
        Filename : str
            The path and filename of the image to add.
        Notes
        -----
        This adds a map, but does not turn it on.
        """
        rc = self._rc
        rc.Map_Add(Filename)

    # %% Output
    def Output_ComputationLevel_Export(self):
        """
        """

    def Output_GetNode(self, riv, reach, rs):
        """
        Returns the Node ID, for a given River Station.

        Parameters
        ----------
        riv : int
            The river ID number.
        rch : int
            Tge reach ID number.
        rs : str
            The river station of the desired node ID.

        Returns
        -------
        int
            Node ID.

        Notes
        -----
        Works like the Geometry_GetNode method, only this function read from
        the output file, so a *.O## file is requires (i.e. run computations
        first).
        """
        rc = self._rc
        res = rc.Output_GetNode(riv, reach, rs)

        return res

    def Output_GetNodes(self):
        """
        """

    def Output_GetProfiles(self):
        """
        """

    def Output_GetReach(self):
        """
        """

    def Output_GetReaches(self):
        """
        """

    def Output_GetRiver(self):
        """
        """

    def Output_GetRivers(self):
        """
        """

    def Output_Initialize(self):
        """
        """

    def Output_NodeOutput(self):
        """
        """

    def Output_ReachOutput(self):
        """
        """

    def Output_Variables(self):
        """
        """

    def Output_VelDist(self):
        """
        """

    def OutputDSS_GetStageFlow(self):
        """
        """

    def OutputDSS_GetStageFlowSA(self):
        """
        """

    # %% Plan
    def Plan_GetFilename(self, planName):
        """
        Given a plan name, returns the plan file, including path.

        Parameters
        ----------
        planName : str
            The name of the plan.

        Returns
        -------
        str
            Plan file and path
        """
        rc = self._rc
        res = rc.Plan_GetFilename(planName)
        return res

    def Plan_Names(self, PlanCount, PlanNames,
                   IncludeOnlyPlansInBaseDirectory):
        """
        Gets a list of all the Plan Names in the active HEC-RAS project.

        Parameters
        ----------
        IncludeOnlyPlansInBaseDirectory : bool

        Returns
        -------
        PlanCount : int
            The number of plans.
        PlanNames : list of str
            The list of plan names.
        """
        rc = self._rc
        res = rc.Plan_GetFilename(PlanCount, PlanNames,
                                  IncludeOnlyPlansInBaseDirectory)
        return res

    def Plan_Reports(self):
        """
        List out the output plan "reports".

        Returns
        -------
        ReportCount : int
            The number of plan reports.
        ReportNames : list of str
            The list of plan reports.
        """
        rc = self._rc
        ReportCount, ReportNames = [], []
        res = rc.Plan_GetFilename(ReportCount, ReportNames)
        return res

    def Plan_SetCurrent(self, PlanTitleToSet):
        """
        Changes the current plan in the HEC-RAS project to the supplied Plan
        Name.

        Parameters
        ----------
        PlanTitleToSet : str
            The name of the plan to set.

        Return
        ------
        bool
        """
        rc = self._rc
        res = rc.Plan_SetCurrent(PlanTitleToSet)

        return res

    def PlanOutput_IsCurrent(self, PlanTitleToCheck, ShowMessageList):
        """
        Checks to see if a plan has an output file associated with it.

        Parameters
        ----------
        PlanTitleToCheck : str
            The name of the plan to check.
        ShowMessageList : bool
            Whether or not to display a message box showing the plans.

        Returns
        -------
        bool

        errmsg : str

        Notes
        -----
        Displays a RAS window that shows a list of all the current plans in the
        RAS Project, and indicates the name and index number of the plan to
        check if it has been computed. If it does not have an output file (i.e.
        hasn't been computed), a message box will ask if you want to run the
        plan. A message box pops up that requires the user to cick OK to
        continue with run-time. Otherwise the RAS "Current Plan"window opens
        and closes quickly.
        """
        rc = self._rc
        errmsg = ''
        res = rc.Plan_SetCurrent(PlanTitleToCheck, ShowMessageList, errmsg)

        return res

    def PlanOutput_SetCurrent(self, PlanTitleToSet):
        """
        Sets the plan output to the selected plan.

        Parameters
        ----------
        PlanTitleToSet : str
            The plan whose output to set as active.

        Returns
        -------
        bool

        Notes
        -----
        This only works if an output file exists for the selected plan. Does
        not change the current plan, nly changes the output file that is
        displayed in the output tables and plots.
        """
        rc = self._rc
        res = rc.Plan_SetCurrent(PlanTitleToSet)

        return res

    def PlanOutput_SetMultiple(self, nPlanTitleToSet, PlanTitleToSet_0,
                               ShowMessageList):
        """
        Sets which pan to set to view in putput plots and tables.

        Parameters
        ----------
        nPlanTitleToSet : int

        PlanTitleToSet_0 : str
            0-based array of plan titles to set.
        ShowMessageList : bool
            Whether to have RAS display a message box showing the plan names.

        Returns
        -------
        int
            Number of plans to set

        Notes
        -----
        Sets the multiple plan outputs. Only works if output file exist for the
        selected plan. Does not change the current plan, only changes the
        output files that are displayed in the output table and plots.
        PlanOutput_SetMultiple requires a 0-based array for plan_titleToSet_0.
        The method plan_Naes returns a 1-based array so it must be converted to
        0-based, prior to calling PlanOutput_SetMultiple.
        """

    # %% Plot
    def PlotHydraulicTables(self, river, reach, rs):
        """
        Displays the Hydraulic Property Plot for a given River, Reach, and
        River Station.

        Parameters
        ----------
        river : str
            The river name.
        reach : str
            The reach name.
        rs : str
            The river station.
        """
        rc = self._rc
        rc.PlotHydraulicTables(river, reach, rs)

    def PlotPF(self, river, reach):
        """
        Displays the Water Surface Profile Plot for a given River and Reach.

        Parameters
        ----------
        river : str
            The river name.
        reach : str
            The reach name.

        Notes
        -----
        Must have an output file for this to work.
        """
        rc = self._rc
        rc.PlotPF(river, reach)

    def PlotPFGeneral(self, river, reach):
        """
        Displays the General Profile Plot for a given River and Reach.

        Parameters
        ----------
        river : str
            The river name.
        reach : str
            The reach name.

        Notes
        -----
        Must have an output file for this to work.
        """
        rc = self._rc
        rc.PlotPFGeneral(river, reach)

    def PlotRatingCurve(self, river, reach):
        """
        Displays the Rating Curve for a given River, Reach and River Station.

        Parameters
        ----------
        river : str
            The river name.
        reach : str
            The reach name.
        rs : str
            The river station.

        Notes
        -----
        Must have an output file for this to work.
        """
        rc = self._rc
        rc.PlotRatingCurve(river, reach)

    def PlotStageFlow(self, river, reach, rs):
        """
        Displays the Stage and Flow Hydrograh for a given River, Reach and
        River Station.

        Parameters
        ----------
        river : str
            The river name.
        reach : str
            The reach name.
        rs : str
            The river station.

        Notes
        -----
        For unsteady plans only. Must have an output file for this to work.
        """
        rc = self._rc
        rc.PlotStageFlow(river, reach, rs)

    def PlotStageFlow_SA(self, SAName):
        """
        Displays the Stage and Flow Hydrograph for a given Storage Area.

        Notes
        -----
        For unsteady flow only. Must have an output file for this to work.
        Names for storage areas cannot be read using the HECRASController,
        therefore the storage area name has to be hard coded, read from a file,
        or retrieved interactively during run-time.
        """
        rc = self._rc
        rc.PlotStageFlow_SA(SAName)

    def PlotXS(self, river, reach, rs):
        """
        Displays the Cross Section Plot for a given River, Reach and River
        Station.

        Parameters
        ----------
        river : str
            The river name.
        reach : str
            The reach name.
        rs : str
            The river station.
        """
        rc = self._rc
        rc.PlotXS(river, reach, rs)

    def PlotXYZ(self, river, reach):
        """
        Displays the XYZ Plot for given River and Reach.

        Parameters
        ----------
        river : str
            The river name.
        reach : str
            The reach name.
        """
        rc = self._rc
        rc.PlotXYZ(river, reach)

    # %% Project
    def Project_Current(self):
        """Returns the file name and path of the current HEC-RAS project."""
        rc = self._rc
        res = rc.Project_Current()

        return res

    def Project_New(self, title, Filename):
        """Starts a new HEC-RAS project with a given project fullpath and sets
        the title.

        Parameters
        ----------
        title : str
            The title if the new HEC-RAS project.
        Filename : str
            Full path of the new HEC-RAS project.
        """
        rc = self._rc

        # Check relative path to script
        dirpath = osp.dirname(osp.abspath(Filename))
        if osp.isdir(dirpath):
            # Create directory recursively
            os.makedirs(dirpath)
        else:
            fullpath = osp.abspath(Filename)

        rc.Project_Open(title, fullpath)

    def Project_Open(self, ProjectFileName):
        """
        Open a HEC-RAS project with a given project path.

        Parameters
        ----------
        ProjectFileName : str
            Full path of the given HEC-RAS project to open.
        """
        rc = self._rc

        # Check relative path to script
        if osp.isfile(ProjectFileName):
            fullpath = osp.abspath(ProjectFileName)
        else:
            error = 'File "{}" not found'.format(fullpath)
            raise IOError(error)

        rc.Project_Open(fullpath)

    def Project_Save(self):
        """
        Save the current HEC-RAS project.
        """
        rc = self._rc
        rc.Project_Save()

    def Project_SaveAs(self, newProjectName):
        """
        Saves as a new project with a given project file name and path.

        Parameters
        ----------
        newProjectName : str
            Path and file name of the HEC-RAS project to save as.
        """
        rc = self._rc
        fullpath = osp.abspath(newProjectName)
        rc.Project_SaveAs(fullpath)

    # %% Schematic
    def Schematic_ReachCount(self):
        """
        Returns the number of reaches in the current HEC-RAS project's active
        geometry.

        Returns
        -------
        int
            Number of Reaches.
        """
        rc = self._rc
        res = rc.Schematic_ReachCount()
        return res

    def Schematic_ReachPointCount(self):
        """
        Returns the total number of reach vertex points that make up all of the
        schematic reach lines in the active geometry.

        Returns
        -------
        int
            Number of reach vertex points.

        """
        rc = self._rc
        res = rc.Schematic_ReachPointCount()
        return res

    def Schematic_ReachPoints(self):
        """
        Returns rivers, reaches and x-y coordinates for each reach.

        Returns
        -------
        RiverName_0 : list of str
            The list of river names.
        ReachName_0 : list of str
            The list of reach names.
        ReachStartIndex_0 : list of int
            The list of starting index numbers for coordinate points.
        ReachPointCount_0 : list of int
            The list of the number of reach points for each reach
        ReachPointX_0 : list of float
            The list of x coordinate points.
        ReachPointY_0 : list of float
            The list of y coordinate points.

        Notes
        -----
        All array parameters are 0-based for this method and must be
        redimensioned.

        Python:  0-based is handled, so the user does not need to account for.
        """
        rc = self._rc
        geo = self.Geometry()
        # FIXME:
        n_rivers = geo.nRiver()
        n_reaches = self.Schematic_ReachCount()
        n_points = self.Schematic_ReachPointCount()
        RiverName_0 = ('',)*(n_rivers)
        ReachName_0 = ('',)*(n_reaches)
        ReachStartIndex_0 = (0,)*(n_reaches)
        ReachPointCount_0 = (0,)*(n_reaches)
        ReachPointX_0 = (0.0,)*(n_points)
        ReachPointY_0 = (0.0,)*(n_points)

        res = rc.Schematic_ReachPoints(RiverName_0, ReachName_0,
                                       ReachStartIndex_0, ReachPointCount_0,
                                       ReachPointX_0, ReachPointY_0)
        (RiverName_0, ReachName_0, ReachStartIndex_0, ReachPointCount_0,
         ReachPointX_0, ReachPointY_0) = res

        return res

    def Schematic_XSCount(self):
        """
        Returns the number of cross sections in the current HEC-RAS project's
        active geometry.

        Returns
        -------
        int
            Number of Cross Sections
        """
        rc = self._rc
        res = rc.Schematic_XSCount()
        return res

    def Schematic_XSPointCount(self):
        """
        Returns the total number of cross secton vertex points that make up all
        of the cross sections in the active geometry.

        Returns
        -------
        int
            Number of cross section points.
        """
        rc = self._rc
        res = rc.Schematic_XSPointCount()
        return res

    def Schematic_XSPoints(self):
        """
        Returns river stations, their reaches and x-y coordinates for each
        river station.

        Returns
        -------
        RSName_0 : list of str
            The list of river stations.
        ReachIdex_0 : list of int
            The list of reach IDs.
        XSStartIndex_0 : list of int
            The list of starting index numbers for coordinate points.
        XSPointCount_0 : list of int
            The list of the number of cross section points for each reach cross
            section.
        XSPointX_0 : list of float
            The list of cross section x coordinate points.
        ReachPointY_0 : list of float
            The list of cross section y coordinate points.

        Notes
        -----
        All array parameters are 0-based for this method and must be
        redimensioned.
        """
        rc = self._rc
        n_xs = self.Schematic_XSCount()
        n_points = self.Schematic_XSPointCount()
        RSName_0 = ('',)*(n_xs)
        ReachIndex_0 = (-1,)*(n_xs)
        XSStartIndex_0 = (-1,)*(n_xs)
        XSPointCount_0 = (-1,)*(n_xs)
        XSPointX_0 = (float('nan'),)*(n_points)
        XSPointY_0 = (float('nan'),)*(n_points)
        res = rc.Schematic_XSPoints(RSName_0, ReachIndex_0, XSStartIndex_0,
                                    XSPointCount_0, XSPointX_0, XSPointY_0)
        (RSName_0, ReachIndex_0, XSStartIndex_0, XSPointCount_0,
         XSPointX_0, XSPointY_0) = res

        return res

    # %% Set TODO:
    def SetDataLocations(self, PlanTitle, count, LocationDesciptions, DSSFiles,
                         DSSPathnames):
        """
        PlanTitle : str

        count : int

        LocationDesciptions : str

        DSSFiles : str

        DSSPathnames : str

        """
        rc = self._rc
        errmsg = ''
        res = rc.SetDataLocations(PlanTitle, count, LocationDesciptions,
                                  DSSFiles, DSSPathnames, errmsg)

    # %% Show
    def ShowRas(self):
        """
        Displays the main HEC-RAS window

        Notes
        -----
        Once a RAS project has been open, ShowRAS will display it. Just opening
        a RAS project, only opens it as a process running in the background.
        You have to ShowRAS to see it on your monitor. Run-time must be paused
        in some way to be able to see HEC-RAS though. If the RAS Controller is
        called within a function, as soon as that function has been executed
        and completed, the instance of HECRASController will close (thus
        closing the HEC-RAS application). To keep HEC-RASS open throw out a
        message box that requires user interaction to close, which effectively
        pauses the run-time.
        """
        rc = self._rc
        rc.ShowRas()

    # %% Steady
    def SteadyFlow_ClearFlowData(self):
        """
        Clears the flow data in the current plan's steady flow file.

        Notes
        -----
        Fr steady flow plans only.
        """
        rc = self._rc
        rc.SteadyFlow_ClearFlowData()

    def SteadyFlow_FixedWSBoundary(self, river, reach, Downstream, WSElev):
        """
        Sets fixed water surface boundary conditions.

        Parameters
        ----------
        river : str
            The River name.
        reach : str
            The Reach name.
        Downstream : bool
            True if this is a downstream boundary. Otherwise False.
        WSElev : float
            The list of water surface elevations to set as fixed water surface
            boundary conditions..

        Notes
        -----
        For steady flow plans only. The WSElev list contains fixed water
        surface elevations for each profile in the active plan's flow file.
        """
        rc = self._rc
        rc.SteadyFlow_FixedWSBoundary(river, reach, Downstream, WSElev)

    def SteadyFlow_nProfile(self):
        """
        Returns the number of setady flow profiles in the current plan's active
        steady flow file.

        Notes
        -----
        For steady flow plans only.
        """
        rc = self._rc
        res = rc.SteadyFlow_nProfile()
        return res

    def SteadyFlow_SetFlow(self, river, reach, rs, Flow):
        """
        For a given River Station, sets the flows for each profile in the
        active plan's steady flow file.

        Parameters
        ----------
        river : str
            The river name.
        reach : str
            The reach name.
        rs : str
            The river station.
        Flow : float
            The list/tuple of flow values to add.

        Notes
        -----
        For steady flow plans only. If the River Station currently is not in
        the flow table, it will added. Need to first determine the number of
        profiles to set up the item count in the Flow array.
        """
        rc = self._rc
        res = rc.SteadyFlow_SetFlow(river, reach, rs, Flow)

    # %% Table
    def TablePF(self, river, reach):
        """
        Displays the Profile Output Table for a given river, reach.

        Parameters
        ----------
        river : str
            The river name.
        reach : str
            The reach name.
        """
        rc = self._rc
        res = rc.TablePF(river, reach)

    def TableXS(self, river, reach, rs):
        """
        Displays the Cross Section Output Table for a given river, reach and
        river station.

        Parameters
        ----------
        river : str
            The river name.
        reach : str
            The reach name.
        rs : str
            The river station.
        """
        rc = self._rc
        res = rc.TableXS(river, reach, rs)

    # %% Unsteady
    def UnsteadyFlow_SetGateOpening_Constant(self, river, reach, rs, GateName,
                                             OpenHeight):
        """
        Sets the gate opening for a specified gate group to a constant value in
        the Time Series Gate Opening boundary condition.

        Parameters
        ----------
        river : str
            The river name.
        reach : str
            The reach name.
        rs : str
            The river station.
        GateName : str
            The gate group name to set a new gate opening height.
        OpenHeight : float
            The gate opening height to set.

        Notes
        -----
        The time interval in the TS Gate Opening boundary condition is set to 1
        year.
        """
        rc = self._rc
        errmsg = ''
        res = rc.UnsteadyFlow_SetGateOpening_Constant(river, reach, rs,
                                                      GateName, OpenHeight)
        river, reach, rs, GateName, OpenHeight, errmsg = res
        return errmsg


class ControllerDeprecated(object):
    """ """
    pass


class RASEvents:
    """Not working"""
    def HECRASController_ComputeProgressBar(self, Progress):
        """
        Repeatedly returns a single value between 0 and 1, indicating the
        progress of the computations.

        Parameters
        ----------
        Progress : float
            Progress of computations [0, 1]

        Notes
        -----
        Must instantiate the HECRASController "With Events". Then the event
        rc.ComputeProgressBar becomes available for code. rc being the variable
        name for the instanciated HECRASController. rc_ComputeProgressBar is
        called repeatedly once Compute_CurrentPlan is called and thorugh the
        duration of the HEC-RAS Computations.

        Python: this events do not work with win32com
        """
        print(Progress)
        return Progress

    def ComputeProgressMessage(self, msg):
        """
        Repeatedly returns computations messages during computations.

        Parameters
        ----------
        Msg : str
            Computation message.

        Notes
        -----
        Must instantiate the HECRASController "With Events". Then the method
        rc_ComputeProgressBar becomes available for code. rc being the variable
        name for the instanciated HECRASController. rc_ComputeProgressMessage
        is called repeatedly once Compute_CurrentPlan is called and thorugh the
        duration of the HEC-RAS Computations.

        Python: this events do not work with win32com
        """
        print(msg)
        return msg
