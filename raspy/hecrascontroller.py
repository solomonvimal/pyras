"""
"""
import os
import os.path as osp

import win32com.client

from .hecrasgeometry import HECRASGeometry


class HECRASController(object):
    """Main object containing all functionality of the HECRAS Controller"""

    def __init__(self):
        self._rc = win32com.client.Dispatch("RAS41.HECRASController")
        self._geometry = HECRASGeometry()

    def compute_complete(self):
        """Returns a true value once computations have completed"""
        rc = self._rc
        rc.Compute_Complete()

    def compute_current_plan(self):
        """Returns a true value once computations have completed"""
        rc = self._rc
        rc.Compute_CurrentPlan()

    # %% Geometry
    def geometry(self):
        """
        """
        return self._geometry

    def geometry_breach_param_get_xml(self):
        """
        Returns a string listing out the dam breach parameters of current plan
        in xml format.
        """
        rc = self._rc
        #rc.Geometry_BreachParamGetXML()

    def geometry_breach_param_set_xml(self, xml_text):
        """
        Set the dam breach parameters of current plan in xml format.

        Parameters
        ----------
        xml_test : str
            TODO:.
        """
        rc = self._rc
        #rc.Geometry_BreachParamSetXML()

    def geometry_get_gate_names(self, river, reach, station):
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

    def geometry_get_gml(self, geomfilename):
        """Returns the GML file txt for the current geometry file.

        Parameters
        ----------
        geomfilename : str
            The name of the geometry file.
        """
        rc = self._rc

        return rc.Geometry_GetGML()

    def geometry_get_node(self, river_id, reach_id, station):
        """Returns the node ID of a selected node.

        Parameters
        ----------
        river_id : int
            TODO:
        reach_id : int
            TODO:
        station : str
            TODO:
        
        Notes
        -----
        """
        rc = self._rc
        res = rc.Geometry_GetNode(river_id, reach_id, station)
        node_id, river_id, reach_id, station = res

        if node_id == 0:
            node_id = None

        return node_id

    def geometry_get_nodes(self, river_id, reach_id):
        """
        Returns a dictionary of nodes and node types in a specified river id
        reach id.

        Parameters
        ----------
        river_id : str
            TODO:
        reach_id : str
            TODO:

        Returns
        -------
        dict or None
            TODO:
        """
        rc = self._rc
        res = rc.Geometry_GetNodes(river_id, reach_id)
        river_id, reach_id, node_count, river_stations, node_types = res

        if river_stations is not None and node_types is not None:
            result = dict(zip(river_stations, node_types))
        else:
            result = None
        return result

    def geometry_get_reaches(self, river_id):
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

    def geometry_get_rivers(self):
        """Returns a list of rivers names."""
        rc = self._rc
        res = rc.Geometry_GetRivers()
        river_count, river_names = res

        if river_names is not None:
            result = list(river_names)
        else:
            result = None

        return result

    def geometry_gis_import(self, title):
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

    def geometry_ratio_manning(self, river_id, reach_up_id, node_upstream,
                               reach_down_id, node_down, ratio):
        """
        Changes Manning's n values over a specified range of cross sections by
        the input ratio.

        Parameters
        ----------
        river_id : int
            The river id
        reach_down_id : int
            The upstream reach id in the range.
        node_down : int
            The upstream node id in the range.
        reach_down_id : int
            The upstream reach id in the range.
        node_down : int
            The upstream node id in the range.
        ratio : float
            The ratio to apply to the Manning's n values in the range of cross
            sections.

        Returns
        -------
        str
            TODO:
        """
        rc = self._rc

    # %% Project
    def project_current(self):
        """Returns the file name and path of the current HEC-RAS project."""
        rc = self._rc
        res = rc.Project_Current()
        
        return res

    def project_new(self, title, filename):
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

    def project_open(self, project_filename):
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

    def project_save(self):
        """
        Save the current HEC-RAS project.
        """
        rc = self._rc
        rc.Project_Save()

    def project_save_as(self, new_project_name):
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

    def quit_ras(self):
        """
        Closes HEC-RAS.

        Notes
        -----
        quit_ras should be called at the end of each session that open a
        HEC-RAS project. Qithout quit_ras, RAS will remain open as a process
        after a script is completed.
        """
        rc = self._rc
#        rc.QuitRAS()

    def show_ras(self):
        """ """
        rc = self._rc
        self._show = True
        rc.ShowRas()
