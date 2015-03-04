"""
"""
import math

import win32com.client


class HECRASGeometry(object):
    """ """
    def __init__(self):
        self._geometry = win32com.client.Dispatch("RAS41.HECRASGeometry")

    def nNode(self, riv, rch):
        """
        Returns the number of nodes in a reach.

        Parameters
        ----------
        riv : int
            The river ID.
        rch : int
            The reach ID.

        Returns
        -------
        int
        """
        geo = self._geometry
        res = geo.nNode(riv, rch)

        n, river, reach = res

        return n

    def NodeCType(self, riv, rch, n):
        """
        Returns the crossing type of a given node.

        Parameters
        ----------
        riv : int
            The river ID.
        rch : int
            The reach ID.
        n : int
            The node ID.

        Returns
        -------
        str

        Notes
        -----
        '' = Cross Section
        'BR' = Bridge
        'Culv' = Culvert
        'IS' = Inline Structure
        'LS' = Lateral Structure
        'MO' = Multiple Opening
        """
        geo = self._geometry
        res = geo.NodeCType(riv, rch, n)
        node_type, river_id, reach_id, node_id = res
        return node_type

    def NodeCutLine_nPoints(self, riv, rch, n):
        """
        Returns the number of coordinate points for a given cross section's
        cutline.

        Parameters
        ----------
        riv : int
            The river ID.
        rch : int
            The reach ID.
        n : int
            The node ID.

        Returns
        -------
        int
        """
        geo = self._geometry
        res = geo.NodeCutLine_nPoints(riv, rch, n)
        n_count, river_id, reach_id, node_id = res
        return n_count

    def NodeCutLine_Points(self, riv, rch, n):
        """
        Returns an array of cutline coordinate points.

        Parameters
        ----------
        riv : int
            The river ID.
        rch : int
            The reach ID.
        n : int
            The node ID.

        Returns
        -------
        x : tuple of floats

        y : tuple of floats
        """
        # FIXME:
        n = self.NodeCutLine_nPoints(riv, rch, n)
        x = (float('nan'),)*(n + 1)
        y = (float('nan'),)*(n + 1)
        geo = self._geometry
        res = geo.NodeCutLine_Points(riv, rch, n, x, y)
        river_id, reach_id, node_id, point_x, point_y = res
        x = tuple([x for x in point_x if not math.isnan(x)])
        y = tuple([y for y in point_y if not math.isnan(y)])
        return x, y

    def NodeIndex(self, riv, rch, RS):
        """
        Returns the node ID for a given river station.

        Parameters
        ----------
        riv : int
            The river ID.
        rch : int
            The reach ID.
        RS : str
            The node river station.

        Returns
        -------
        int
        """
        geo = self._geometry
        res = geo.NodeIndex(riv, rch, RS)
        node_index, river_id, reach_id, station = res
        return node_index

    def NodeRS(self, riv, rch, n):
        """
        Returns the river station of a node, given its node ID.

        Parameters
        ----------
        riv : int
            The river ID.
        rch : int
            The reach ID.
        n : int
            The node ID.

        Returns
        -------
        str
        """
        geo = self._geometry
        res = geo.NodeRS(riv, rch, n)
        station, river_id, reach_id, n = res
        return station

    def NodeType(self, riv, rch, n):
        """
        Returns the node type, given its node ID.

        Parameters
        ----------
        riv : int
            The river ID.
        rch : int
            The reach ID.
        n : int
            The node ID.

        Returns
        -------
        int

        Notes
        -----
        1 = Cross section
        2 = Culvert
        3 = Bridge
        4 = Multiple Opening
        5 = Inline Structure
        6 = Lateral Structure
        """
        geo = self._geometry
        res = geo.NodeType(riv, rch, n)
        node_type, river_id, reach_id, node = res

        return node_type

    def nReach(self, riv):
        """
        Returns the number of reaches for a given river ID.

        Parameters
        ----------
        riv : int
            The river ID.
        """
        geo = self._geometry
        res = geo.nReach(riv)
        n_reach, river_id = res
        return n_reach

    def nRiver(self):
        """
        Returns the number of rivers in the active geometry.
        """
        geo = self._geometry
        n_river = geo.nRiver()
        return n_river

    def ReachIndex(self, riv, ReachName):
        """
        Returns the ID of a reach, given its name.

        Parameters
        ----------
        riv : int
            The river ID.
        ReachName : str
            The reach name.

        Returns
        -------
        int
        """
        geo = self._geometry
        res = geo.ReachIndex(riv, ReachName)
        reach_id, river_id, reach_name = res
        return reach_id

    def ReachInvert_nPoints(self, riv, rch):
        """
        Returns the number of points that make up the stream centerline of a
        reach, given the river and reach IDs.

        Parameters
        ----------
        riv : int
            The river ID.
        rch : int
            The reach ID.

        Returns
        -------
        int
        """
        geo = self._geometry
        res = geo.ReachInvert_nPoints(riv, rch)
        n, river, reach = res
        return n

    def ReachInvert_Points(self, riv, rch):
        """
        Gets an array of coordinate points that make up a reach stream
        centerline.

        Parameters
        ----------
        riv : int
            The river ID.
        rch : int
            The reach ID.

        Returns
        -------
        x : tuple of floats
            X coordinates of invert in reach
        y : tuple of floats
            Y coordinates of invert in reach
        """
        n = self.ReachInvert_nPoints(riv, rch)
        x = (float('nan'),)*(n + 1)
        y = (float('nan'),)*(n + 1)
        geo = self._geometry
        res = geo.ReachInvert_Points(riv, rch, x, y)

        river, reach, point_x, point_y = res
        x = tuple([x for x in point_x if not math.isnan(x)])
        y = tuple([y for y in point_y if not math.isnan(y)])

        return x, y

    def ReachName(self, riv, rch):
        """
        Returns the name of the reach, given a reach ID.

        Parameters
        ----------
        riv : int
            The river ID.
        """
        geo = self._geometry
        res = geo.ReachName(riv, rch)

        reach_name, river_id, river_reach = res

        return reach_name

    def RiverIndex(self, RiverName):
        """
        Returns the id of the river, given a river name.

        Parameters
        ----------
        river_name : str
            The river name.

        Returns
        -------
        int
            The river id
        """
        geo = self._geometry
        res = geo.RiverIndex(RiverName)

        river_id, river_name = res

        return river_id

    def RiverName(self, riv):
        """
        Returns the name of the river, given a river ID.

        Parameters
        ----------
        riv : int
            The river ID.

        Returns
        -------
        str
            The river name.
        """
        geo = self._geometry
        res = geo.RiverName(riv)

        river_name, river_id = res

        return river_name

    def Save(self):
        """
        Saves the geometry.
        """
        geo = self._geometry
        geo.Save()
