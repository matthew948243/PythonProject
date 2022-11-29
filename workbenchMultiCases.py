totalheight = [1393.4, 1493.4, 1593.4]
rocketMoveHeight = [100.0, 200.0, 300.0]
rotationDeg= [5.0, 15.0, 25.0]

cmd="""
/scoped-sizing/create \"control-1\" boi object-faces yes yes *boi* 3 1.2
/scoped-sizing/compute
/file/write-size-field \"D:/WorkBench/SimpleModel/tempTestPro/tempsize.sf\" ok
/file/import/cad-options/tessellation  cfd-surface-mesh yes \"D:/WorkBench/SimpleModel/tempTestPro/tempsize.sf\"
/file/import/cad yes \"D:/WorkBench/SimpleModel/tempTestPro/rocket2_files/dp0/Geom/DM/Geom.scdoc\" no yes 40 yes mm ok
/objects/volumetric-regions/compute *myfluideeclosuretobecuted* no
/objects/volumetric-regions/rename * *myfluideeclosuretobecuted* *myfluideeclosuretobecuted* myfluid
/objects/volumetric-regions/change-type *myfluideeclosuretobecuted* * () fluid
/boundary/manage/type inlet* () velocity-inlet
/boundary/manage/type outlet* () pressure-outlet
/objects/volumetric-regions/scoped-prism/set/create "control-1" aspect-ratio 8 5 1.2 myfluideeclosuretobecutedcomponent:myfluideeclosuretobecutedcomponent-myfluideeclosuretobecuted1 fluid-regions selected-labels *wall*
/mesh/auto-mesh * no  scoped  pyramids hexcore  yes
/report/cell-quality-limits *()
/switch-to-solution-mode yes
/define/models/viscous/ke-realizable? yes
/define/models/viscous/near-wall-treatment enhanced-wall-treatment? yes quit
/define/boundary-conditions/fluid myfluid no no no no no 0 no 0 no 0 no 0 no 0 no 0 no no no no no
/define/boundary-conditions/set/velocity-inlet *inlet_velocity* () vmag no 30 quit
/define/models/energy? yes no no no yes
/define/boundary-conditions/set/velocity-inlet *inlet_velocity* () temperature no 290 quit
/define/boundary-conditions/set/pressure-outlet *outlet_pressure* () gauge-pressure no 100 quit
/solve/report-definitions/add out-vel-rdef surface-areaavg surface-names *outlet_pressure* () field velocity-magnitude quit
/solve/report-plots/add out-vel-rplot report-defs out-vel-rdef () quit
/display/surface/plane-surface xz-plane-0 zx-plane 0
/file/write-case-data "D:/WorkBench/SimpleModel/tempTestPro/rocket2.cas.h5" ok
/solve/iterate 50
/display/objects/create contour vel-mid surfaces-list xz-plane-0 () field velocity-magnitude quit
"""
template1 = GetTemplate(TemplateName="Geometry")
system1 = template1.CreateSystem()
template2 = GetTemplate(TemplateName="FLTG")
system2 = template2.CreateSystem(Position="Right",RelativeTo=system1)

geometryComponent1 = system1.GetComponent(Name="Geometry")
meshComponent1 = system2.GetComponent(Name="Mesh")
geometryComponent1.TransferData(TargetComponent=meshComponent1)
Save(FilePath=GetAbsoluteUserPathName("D:/WorkBench/SimpleModel/tempTestPro/rocket2.wbpj"),Overwrite=True)

geometry1 = system1.GetContainer(ComponentName="Geometry")
geometry1.SetFile(FilePath="D:/WorkBench/SimpleModel/rocket2.scdoc")
geometry1.Edit(IsSpaceClaimGeometry=True)
geometry1.Exit()

Save(FilePath="D:/WorkBench/SimpleModel/tempTestPro/rocket2.wbpj",Overwrite=True)

tGridCADImportOptions1 = GetDataEntity("/Mesh/TGridCADImportOptions:TGridCADImportOptions")
tGridData1 = GetDataEntity("/Mesh/TGridData:TGridData")
tGridData1.RunParallel = True
tGridData1.NumberOfProcs = 6
tGridCADImportOptions1.UseWorkflow = False
tGridCADImportOptions1.FeatureAngle = 40
tGridCADImportOptions1.Units = "mm"
tGridCADImportOptions1.TessellationOption = "CFD surface mesh"
tGridCADImportOptions1.CT_UseSizeFieldFile = False
tGridCADImportOptions1.CT_Min = 5
tGridCADImportOptions1.CT_Max = 50
tGridCADImportOptions1.CT_Angle = 18
tGridCADImportOptions1.CT_SaveSizeField = False


setup1 = system2.GetContainer(ComponentName="Setup")
fluentLauncherSettings1 = setup1.GetFluentLauncherSettings()
fluentLauncherSettings1.SetEntityProperties(Properties=Set(Precision="Double",EnvPath={}))
tGridData1.SetEntityProperties(Properties=Set(RunParallel=True, NumberOfProcs=6))
mesh1 = system2.GetContainer(ComponentName="Mesh")
Fluent.Edit(Container=mesh1)


meshComponent1 = system2.GetComponent(Name="Mesh")
meshComponent1.Refresh()


setup1.SendCommand(Command=cmd)


setup1.SendCommand(Command="/close-fluent")

setupComponent1 = system2.GetComponent(Name="Setup")
setupComponent1.Update(AllDependencies=True)
solutionComponent1 = system2.GetComponent(Name="Solution")
solutionComponent1.Update(AllDependencies=True)





rocketMoveHeight_param = Parameters.GetParameter(Name="P2")

rotationDeg_param = Parameters.GetParameter(Name="P3")

from itertools import product
index = 0

for height, deg in product(rocketMoveHeight, rotationDeg):  
    try:     
        dp = Parameters.GetDesignPoint("%s"%index)
    except: 
        dp = Parameters.CreateDesignPoint()  
    dp.Retained = True
    dp.SetParameterExpression(Parameter=rocketMoveHeight_param,
                            Expression="%s"%height)
    dp.SetParameterExpression(Parameter=rotationDeg_param,
                            Expression="%s"%deg)
    index += 1


designPointUpdateSettings1 = GetDesignPointUpdateSettings()
designPointUpdateSettings1.DesignPointRetainedOrExportedUpdate = "FullProject"

UpdateAllDesignPoints()
Parameters.ExportAllDesignPointsData(FileName="D:/WorkBench/SimpleModel/tempTestPro/rocket2.csv")
Save(Overwrite=True)














