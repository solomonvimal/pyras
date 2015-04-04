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

    def Compute_CurrentPlan(self, nmsg, msg, BlockingModel=True):
        """
        Computes the current plan.

        Parameters
        ----------
        nmsg : int
            The number of returned messages.
        msg : str
            Messages returned from HECRASController during computations
        BlockingMode: bool, optional
            If BlockingMode is set to False, the code will continue to be read
            while HEC-RAS is computing. Otherwise, run-time will be paused. By
            default, the HECRASController sets blocking mode to True.
        """
        rc = self._rc
        rc.Compute_CurrentPlan()

    def Compute_HideComputationWindow(self):
        """
        """

    def Compute_IsStillComputing(self):
        """
        """

    def Compute_ShowComputationWindow(self):
        """
        """

    def Compute_WATPlan(self):
        """
        """

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

    # %% Edit
    def Edit_AddBC(self):
        """
        """

    def Edit_AddIW(self):
        """
        """

    def Edit_AddLW(self):
        """
        """

    def Edit_AddXS(self):
        """
        """

    def Edit_BC(self):
        """
        """

    def Edit_GeometricData(self):
        """
        """

    def Edit_IW(self):
        """
        """

    def Edit_LW(self):
        """
        """

    def Edit_MultipleRun(self):
        """
        """

    def Edit_PlanData(self):
        """
        """

    def Edit_QuasiUnsteadyFlowData(self):
        """
        """

    def Edit_SedimentData(self):
        """
        """
        rc = self._rc

    def Edit_SteadyFlowData(self):
        """
        """
        rc = self._rc

    def Edit_UnsteadyFlowData(self):
        """
        """
        rc = self._rc

    def Edit_WaterQualityData(self):
        """
        """
        rc = self._rc

    def Edit_XS(self):
        """
        """
        rc = self._rc

    # %% Export
    def ExportGIS(self):
        """
        Imports geometry data from an *.sdf import file.

        Parameters
        ----------
        title : str
            The title of the new geometry file to import.

        Returns
        -------
        str
            TODO:
        """
        rc = self._rc
        #title, filename = rc.geometery_gis_import(title)

    # %% Geometry
    def Geometery_GISImport(self):
        """
        """

    def Geometry(self):
        """
        """
        return self._geometry

#    def geometry_breach_param_get_xml(self):
#        """
#        Returns a string listing out the dam breach parameters of current plan
#        in xml format.
#        """
#        rc = self._rc
#        #rc.Geometry_BreachParamGetXML()
#
#    def geometry_breach_param_set_xml(self, xml_text):
#        """
#        Set the dam breach parameters of current plan in xml format.
#
#        Parameters
#        ----------
#        xml_test : str
#            TODO:.
#        """
#        rc = self._rc
#        #rc.Geometry_BreachParamSetXML()

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
        river, reach, station, ngate, gate_names = res

        return list(gate_names)

    def Geometry_GetGML(self, geomfilename):
        """Returns the GML file txt for the current geometry file.

        Parameters
        ----------
        geomfilename : str
            The name of the geometry file.
        """
        rc = self._rc

        return rc.Geometry_GetGML()

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

    def Geometry_GetReaches(self, river_id):
        """
        Returns a list of the reach names in a given river id.

        Parameters
        ----------
        river_id : str
            TODO:

        Returns
        -------
        list of str or None
            TODO:
        """
        rc = self._rc
        res = rc.Geometry_GetReaches(river_id)
        river_id, reach_count, reach_names = res

        if reach_names is not None:
            result = list(reach_names)
        else:
            result = None
        return result

    def Geometry_GetRivers(self):
        """Returns a list of rivers names."""
        rc = self._rc
        res = rc.Geometry_GetRivers(None)
        river_count, river_names = res

        if river_names is not None:
            result = list(river_names)
        else:
            result = None

        return result

    def Geometry_SetMann(self):
        """
        """

    def Geometry_SetMann_LChR(self):
        """
        """

    def Geometry_SetSAArea(self):
        """
        """

#    def Geometry_ratio_manning(self, river_id, reach_up_id, node_upstream,
#                               reach_down_id, node_down, ratio):
#        """
#        Changes Manning's n values over a specified range of cross sections by
#        the input ratio.
#
#        Parameters
#        ----------
#        river_id : int
#            The river id
#        reach_down_id : int
#            The upstream reach id in the range.
#        node_down : int
#            The upstream node id in the range.
#        reach_down_id : int
#            The upstream reach id in the range.
#        node_down : int
#            The upstream node id in the range.
#        ratio : float
#            The ratio to apply to the Manning's n values in the range of cross
#            sections.
#
#        Returns
#        -------
#        str
#            TODO:
#        """
#        rc = self._rc

    # %% Get

    def GetDataLocations_Input(self):
        """
        """

    def GetDataLocations_Input_count(self):
        """
        """

    def GetDataLocations_Output(self):
        """
        """

    def GetDataLocations_Output_count(self):
        """
        """

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
    def Map_Add(self):
        """
        """

    def mGeometry(self):
        """
        """

    # %% Output
    def Output_ComputationLevel_Export(self):
        """
        """

    def Output_GetNode(self):
        """
        """

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
    def Plan_GetFilename(self):
        """
        """

    def Plan_Names(self):
        """
        """

    def Plan_Reports(self):
        """
        """

    def Plan_SetCurrent(self):
        """
        """

    def PlanOutput_IsCurrent(self):
        """
        """

    def PlanOutput_SetCurrent(self):
        """
        """

    def PlanOutput_SetMultiple(self):
        """
        """

    # %% Plot
    def PlotHydraulicTables(self):
        """
        """

    def PlotPF(self):
        """
        """

    def PlotPFGeneral(self):
        """
        """

    def PlotRatingCurve(self):
        """
        """

    def PlotStageFlow(self):
        """
        """

    def PlotStageFlow_SA(self):
        """
        """

    def PlotXS(self):
        """
        """

    def PlotXYZ(self):
        """
        """

    # %% Project
    def Project_Current(self):
        """Returns the file name and path of the current HEC-RAS project."""
        rc = self._rc
        res = rc.Project_Current()
        
        return res

    def Project_New(self, title, filename):
        """Starts a new HEC-RAS project with a given project fullpath and sets
        the title.

        Parameters
        ----------
        title : str
            The title if the new HEC-RAS project.
        filename : str
            Full path of the new HEC-RAS project.
        """
        rc = self._rc

        # Check relative path to script
        dirpath = osp.dirname(osp.abspath(filename))
        if osp.isdir(dirpath):
            # Create directory recursively
            os.makedirs(dirpath)
        else:
            fullpath = osp.abspath(filename)

        rc.Project_Open(title, fullpath)

    def Project_Open(self, project_filename):
        """
        Open a HEC-RAS project with a given project path.

        Parameters
        ----------
        project_filename : str
            Full path of the given HEC-RAS project to open.
        """
        rc = self._rc

        # Check relative path to script
        if osp.isfile(project_filename):
            fullpath = osp.abspath(project_filename)
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

    def Project_SaveAs(self, new_project_name):
        """
        Saves as a new project with a given project file name and path.

        Parameters
        ----------
        new_project_name : str
            Path and file name of the HEC-RAS project to save as.
        """
        rc = self._rc
        fullpath = osp.abspath(new_project_name)
        rc.Project_SaveAs(fullpath)

#    def quit_ras(self):
#        """
#        Closes HEC-RAS.
#
#        Notes
#        -----
#        quit_ras should be called at the end of each session that open a
#        HEC-RAS project. Qithout quit_ras, RAS will remain open as a process
#        after a script is completed.
#        """
#        rc = self._rc
#        rc.QuitRAS()

    # %% Schematic
    def Schematic_ReachCount(self):
        """
        """

    def Schematic_ReachPointCount(self):
        """
        """

    def Schematic_ReachPoints(self):
        """
        """

    def Schematic_XSCount(self):
        """
        """

    def Schematic_XSPointCount(self):
        """
        """

    def Schematic_XSPoints(self):
        """
        """

    # %% Set

    def SetDataLocations(self):
        """
        """

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
        """

    def SteadyFlow_FixedWSBoundary(self):
        """
        """

    def SteadyFlow_nProfile(self):
        """
        """

    def SteadyFlow_SetFlow(self):
        """
        """

    # %% Table
    def TablePF(self):
        """
        """

    def TableXS(self):
        """
        """

    # %% Unsteady
    def UnsteadyFlow_SetGateOpening_Constant(self):
        """
        """
