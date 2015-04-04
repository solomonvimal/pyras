# -*- coding: utf-8 -*-
"""

"""
import pyras


project = r'examples\Steady Examples\BEAVCREK.prj'
rc = pyras.HECRASController()

rc.ShowRas()

# %% Project
rc.Project_Open(project)

res = rc.Project_Current()
print('Project_Current', res)

#res = rc.Compute_Complete()
#print('ComputeComplete', res)

# %% Curent
res = rc.CurrentGeomFile()
print('CurrentGeomFile', res)

res = rc.CurrentPlanFile()
print('CurrentPlanFile', res)

res = rc.CurrentProjectFile()
print('CurrentProjectFile', res)

res = rc.CurrentProjectTitle()
print('CurrentProjectTitle', res)

res = rc.CurrentSteadyFile()
print('CurrentSteadyFile', res)

res = rc.CurrentUnSteadyFile()
print('CurrentUnSteadyFile', res)

# %% Geometry (Geometry Class)

geo = rc.Geometry()

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

#res = rc.Geometry_GetGML()
#print('Geometry_GetGML', res)

#res = rc.Geometry_GetRivers()
#print('Geometry_GetRivers', res)

res = rc.Geometry_GetNode(1, 1, '5.39')
print('Geometry_GetNode', res)

res = rc.Geometry_GetNodes(1, 1)
print('Geometry_GetNodes', res)

#res = rc.Geometry_GetReaches(1)
#print('Geometry_GetReaches', res)

# %% Get (Controller Class)
res = rc.GetRASVersion()
print('GetRASVersion', res)

res = rc.HECRASVersion()
print('HECRASVersion', res)

rc.QuitRas()
