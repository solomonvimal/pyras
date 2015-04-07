# -*- coding: utf-8 -*-
"""

"""
from pyras.controllers.hecras import HECRASController, kill_all

project = r'examples\Steady Examples\BEAVCREK.prj'
#project = r'examples\Unsteady Examples\NavigationDam\ROCK_TEST.prj'


#rc = HECRASController('RAS41')
rc = HECRASController('RAS500')

#rc.ShowRas()

# %% Project
rc.Project_Open(project)

res = rc.Project_Current()
print('Project_Current:')
print(res)
print('')

#rc.Compute_HideComputationWindow()
#rc.Compute_ShowComputationWindow()
res = rc.Compute_CurrentPlan()
print('Compute_CurrentPlan:')
print(res)
print('')

#res = rc.Compute_Cancel()
#print('\nCompute_Cancel', res)

#res = rc.Compute_Complete()
#print('Compute_Complete')
#print(res)
#print('')

# %% Curent (Controller Class)
#res = rc.CurrentGeomFile()
#print('CurrentGeomFile')
#print(res)
#print('')
#
#res = rc.CurrentPlanFile()
#print('CurrentPlanFile')
#print(res)
#print('')
#
#res = rc.CurrentProjectFile()
#print('CurrentProjectFile')
#print(res)
#print('')
#
#res = rc.CurrentProjectTitle()
#print('CurrentProjectTitle')
#print(res)
#print('')
#
#res = rc.CurrentSteadyFile()
#print('CurrentSteadyFile')
#print(res)
#print('')
#
#res = rc.CurrentUnSteadyFile()
#print('CurrentUnSteadyFile')
#print(res)
#print('')

# %% Geometry (Geometry Class)

#geo = rc.Geometry()
#
#res = geo.RiverIndex('Beaver Creek')
#print('RiverIndex')
#print(res)
#print('')
#
#res = geo.RiverName(1)
#print('RiverName')
#print(res)
#print('')
#
#res = geo.ReachName(1, 1)
#print('ReachName')
#print(res)
#print('')
#
#res = geo.ReachInvert_nPoints(1, 1)
#print('ReachInvert_nPoints')
#print(res)
#print('')
#
#res = geo.ReachInvert_Points(1, 1)
#print('ReachInvert_Points')
#print(res)
#print('')
#
#res = geo.ReachIndex(1, 'Kentwood')
#print('ReachIndex')
#print(res)
#print('')
#
#res = geo.nRiver()
#print('nRiver')
#print(res)
#print('')
#
#res = geo.nReach(1)
#print('nReach')
#print(res)
#print('')
#
#res = geo.NodeType(1, 1, 1)
#print('NodeType')
#print(res)
#print('')
#
#res = geo.NodeRS(1, 1, 1)
#print('NodeRS')
#print(res)
#print('')
#
#res = geo.NodeIndex(1, 1, '5.99')
#print('NodeIndex')
#print(res)
#print('')
#
#res = geo.NodeCutLine_Points(1, 1, 1)
#print('NodeCutLine_Points')
#print(res)
#print('')
#
#res = geo.NodeCutLine_nPoints(1, 1, 1)
#print('NodeCutLine_nPoints')
#print(res)
#print('')
#
#res = geo.NodeCType(1, 1, 8)
#print('NodeCType')
#print(res)
#print('')

# %% Edit (Controller Class)

#rc.Edit_BC('Beaver Creek', 'Kentwood', '5.99')
#print('Edit_BC')
#print('')
#
#rc.Edit_GeometricData()
#print('Edit_GeometricData')
#print('')
#
#rc.Edit_IW('Beaver Creek', 'Kentwood', '5.99')
#print('Edit_IW')
#print('')
#
#rc.Edit_LW('Beaver Creek', 'Kentwood', '5.99')
#print('Edit_LW')
#print('')
#
#rc.Edit_MultipleRun()
#print('Edit_MultipleRun')
#print('')
#
#rc.Edit_PlanData()
#print('Edit_PlanData')
#print('')
#
#rc.Edit_QuasiUnsteadyFlowData()
#print('Edit_QuasiUnsteadyFlowData')
#print('')
#
#rc.Edit_SedimentData()
#print('Edit_SedimentData')
#print('')
#
#rc.Edit_SteadyFlowData()
#print('Edit_SteadyFlowData')
#print('')
#
#rc.Edit_UnsteadyFlowData()
#print('Edit_UnsteadyFlowData')
#print('')
#
#rc.Edit_WaterQualityData()
#print('Edit_WaterQualityData')
#print('')
#
#rc.Edit_XS('Beaver Creek', 'Kentwood', '5.99')
#print('Edit_XS')
#print('')

# %% Geometry (Controller Class)

# Not tested
#res = rc.Geometery_GISImport(self, title, Filename)
#print('Geometery_GISImport')
#print(res)
#print('')

# Not tested but seems to work
#res = rc.Geometry_GetGateNames(1, 1, '5.39')
#print('Geometry_GetGateNames')
#print(res)
#print('')

# Not working
#res = rc.Geometry_GetGML('Bvr.Cr.+Bridge - P/W: New Le, Lc')
#print('Geometry_GetGML')
#print(res)
#print('')

#res = rc.Geometry_GetNode(1, 1, '5.39')
#print('Geometry_GetNode')
#print(res)
#print('')
#
#res = rc.Geometry_GetNodes(1, 1)
#print('Geometry_GetNodes')
#print(res)
#print('')
#
#res = rc.Geometry_GetReaches(1)
#print('Geometry_GetReaches')
#print(res)
#print('')
#
#res = rc.Geometry_GetRivers()
#print('Geometry_GetRivers')
#print(res)
#print('')
#
#res = rc.Geometry_SetMann('Beaver Creek', 'Kentwood', '5.99',
#                          3, (0.12, 0.13, 0.14), (5, 36, 131))
#print('Geometry_SetMann')
#print(res)
#print('')
#
#res = rc.Geometry_SetMann_LChR('Beaver Creek', 'Kentwood', '5.99', 0.15, 0.10,
#                               0.16)
#print('Geometry_SetMann_LChR')
#print(res)
#print('')
#
#res = rc.Geometry_SetSAArea('test', 1200)
#print('Geometry_SetSAArea')
#print(res)
#print('')

# %% Get (Controller Class)
res = rc.GetRASVersion()
#print('GetRASVersion')
#print(res)
#print('')
#
#res = rc.HECRASVersion()
#print('HECRASVersion', res)
#print(res)
#print('')

# %% Schematic (Controller Class)
#res = rc.Schematic_ReachCount()
#print('Schematic_ReachCount')
#print(res)
#print('')
#
#res = rc.Schematic_ReachPointCount()
#print('Schematic_ReachPointCount')
#print(res)
#print('')
#
#res = rc.Schematic_ReachPoints()
#print('Schematic_ReachPoints')
#print(res)
#print('')
#
#res = rc.Schematic_XSCount()
#print('Schematic_XSCount')
#print(res)
#print('')
#
#res = rc.Schematic_XSPointCount()
#print('Schematic_XSPointCount')
#print(res)
#print('')
#
#res = rc.Schematic_XSPoints()
#print('Schematic_XSPointCount')
#print(res)
#print('')

rc.close()
kill_all()
