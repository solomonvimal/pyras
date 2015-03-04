# -*- coding: utf-8 -*-
"""

"""
import raspy


project = r'examples\Steady Examples\BEAVCREK.p01'
rc = raspy.HECRASController()

rc.show_ras()

# %% Project
rc.project_open(project)

res = rc.project_current()
print(res)

# %% Geometry (Geometry Class)

geo = rc.geometry()

res = geo.RiverIndex('Beaver Creek')
print('RiverIndex', res)

res = geo.RiverName(1)
print('RiverName', res)

res = geo.ReachName(1, 1)
print('ReachName', res)

res = geo.ReachInvert_nPoints(1, 1)
print('ReachInvert_nPoints', res)

res = geo.ReachInvert_Points(1, 1)
print('ReachInvert_Points', res)

res = geo.ReachIndex(1, 'Kentwood')
print('ReachIndex', res)

res = geo.nRiver()
print('nRiver', res)

res = geo.nReach(1)
print('nReach', res)

res = geo.NodeType(1, 1, 1)
print('NodeType', res)

res = geo.NodeRS(1, 1, 1)
print('NodeRS', res)

res = geo.NodeIndex(1, 1, '5.99')
print('NodeIndex', res)

res = geo.NodeCutLine_Points(1, 1, 1)
print('NodeCutLine_Points', res)

res = geo.NodeCutLine_nPoints(1, 1, 1)
print('NodeCutLine_nPoints', res)

res = geo.NodeCType(1, 1, 8)
print('NodeCType', res)

# %% Geometry (Controller Class)
#res = rc.geometry_get_gate_names()
#print(res)

#res = rc.geometry_get_gml()
#print(res)

#res = rc.geometry_get_rivers()
#print(res)
#
#res = rc.geometry_get_node(1, 1, '5.39')
#print(res)
#
#res = rc.geometry_get_nodes(1, 1)
#print(res)
#
#res = rc.geometry_get_reaches(1)
#print(res)
