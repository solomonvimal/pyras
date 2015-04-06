# -*- coding: utf-8 -*-
"""

"""
import pyras

project = r'examples\Steady Examples\BEAVCREK.prj'

rc = pyras.controllers.HECRASController('RAS41')
#rc = pyras.controllers.HECRASController('RAS500')

#rc.ShowRas()

# %% Project
rc.Project_Open(project)
#rc.runtime().pause(5)

#res = rc.Project_Current()
#print('Project_Current', res)

#res = rc.Compute_Cancel()
#print('Compute_Cancel', res)

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

#geo = rc.Geometry()
#
#res = geo.RiverIndex('Beaver Creek')
#print('RiverIndex', res)
#
#res = geo.RiverName(1)
#print('RiverName', res)
#
#res = geo.ReachName(1, 1)
#print('ReachName', res)
#
#res = geo.ReachInvert_nPoints(1, 1)
#print('ReachInvert_nPoints', res)
#
#res = geo.ReachInvert_Points(1, 1)
#print('ReachInvert_Points', res)
#
#res = geo.ReachIndex(1, 'Kentwood')
#print('ReachIndex', res)
#
#res = geo.nRiver()
#print('nRiver', res)
#
#res = geo.nReach(1)
#print('nReach', res)
#
#res = geo.NodeType(1, 1, 1)
#print('NodeType', res)
#
#res = geo.NodeRS(1, 1, 1)
#print('NodeRS', res)
#
#res = geo.NodeIndex(1, 1, '5.99')
#print('NodeIndex', res)
#
#res = geo.NodeCutLine_Points(1, 1, 1)
#print('NodeCutLine_Points', res)
#
#res = geo.NodeCutLine_nPoints(1, 1, 1)
#print('NodeCutLine_nPoints', res)
#
#res = geo.NodeCType(1, 1, 8)
#print('NodeCType', res)

# %% Edit (Controller Class)

#res = rc.Edit_BC('Beaver Creek', 'Kentwood', '5.99')
#print('Edit_BC')
#
#rc.Edit_GeometricData()
#print('Edit_GeometricData')
#
#res = rc.Edit_IW('Beaver Creek', 'Kentwood', '5.99')
#print('Edit_IW', res)
#
#res = rc.Edit_LW('Beaver Creek', 'Kentwood', '5.99')
#print('Edit_LW', res)
#
#res = rc.Edit_MultipleRun()
#print('Edit_MultipleRun', res)
#
#res = rc.Edit_PlanData()
#print('Edit_PlanData', res)
#
#res = rc.Edit_QuasiUnsteadyFlowData()
#print('Edit_QuasiUnsteadyFlowData', res)
#
#res = rc.Edit_SedimentData()
#print('Edit_SedimentData', res)
#
#res = rc.Edit_SteadyFlowData()
#print('Edit_SteadyFlowData', res)
#
#res = rc.Edit_UnsteadyFlowData()
#print('Edit_UnsteadyFlowData', res)
#
#res = rc.Edit_WaterQualityData()
#print('Edit_WaterQualityData', res)
#
#res = rc.Edit_XS('Beaver Creek', 'Kentwood', '5.99')
#print('Edit_XS', res)

# %% Geometry (Controller Class)

# Not tested
#res = rc.Geometery_GISImport(self, title, Filename)
#print('Geometery_GISImport', res)

# Not tested but seems to work
#res = rc.Geometry_GetGateNames(1, 1, '5.39')
#print('Geometry_GetGateNames', res)

# Not working
#res = rc.Geometry_GetGML('Bvr.Cr.+Bridge - P/W: New Le, Lc')
#print('Geometry_GetGML', res)

res = rc.Geometry_GetNode(1, 1, '5.39')
print('Geometry_GetNode', res)

res = rc.Geometry_GetNodes(1, 1)
print('Geometry_GetNodes', res)

res = rc.Geometry_GetReaches(1)
print('Geometry_GetReaches', res)

res = rc.Geometry_GetRivers()
print('Geometry_GetRivers', res)

res = rc.Geometry_SetMann('Beaver Creek', 'Kentwood', '5.99',
                          3, (0.12, 0.13, 0.14), (5, 36, 131))
print('Geometry_SetMann', res)

res = rc.Geometry_SetMann_LChR('Beaver Creek', 'Kentwood', '5.99', 0.15, 0.10,
                               0.16)
print('Geometry_SetMann_LChR', res)

res = rc.Geometry_SetSAArea('test', 1200)
print('Geometry_SetSAArea', res)

#rc.Edit_GeometricData()
#print('Edit_GeometricData')

# %% Get (Controller Class)
res = rc.GetRASVersion()
print('GetRASVersion', res)

res = rc.HECRASVersion()
print('HECRASVersion', res)

# %% Schematic (Controller Class)
res = rc.Schematic_ReachCount()
print('Schematic_ReachCount', res)

res = rc.Schematic_ReachPointCount()
print('Schematic_ReachPointCount', res)

res = rc.Schematic_ReachPoints()
print('Schematic_ReachPoints', res)

res = rc.Schematic_XSCount()
print('Schematic_XSCount', res)

res = rc.Schematic_XSPointCount()
print('Schematic_XSPointCount', res)

res = rc.Schematic_XSPoints()
print('Schematic_XSPointCount', res)

#rc.close()
#pyras.kill_all()
