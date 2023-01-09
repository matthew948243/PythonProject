
#在该版本中/file/write-size-field "D:/WorkBench/SimpleModel/tempsize.sf" 没有OK 并且文件不需要加引号
cmdCommand="""
/file/import/cad-options/tessellation  cfd-surface-mesh no 0.5 5 18 no no
/file/import/cad yes "D:/WorkBench/SimpleModel/rocket.scdoc" yes 40 yes mm
/scoped-sizing/create "control-1" boi object-faces yes yes *boi* 8 1.2
/scoped-sizing/compute
/file/write-size-field "D:/WorkBench/SimpleModel/tempsize.sf" 
/file/import/cad-options/tessellation  cfd-surface-mesh yes "D:/WorkBench/SimpleModel/tempsize.sf"
/file/import/cad yes "D:/WorkBench/SimpleModel/rocket.scdoc" no yes 40 yes mm ok
/objects/volumetric-regions/compute *myfluideeclosuretobecuted* no
/objects/volumetric-regions/rename * *myfluideeclosuretobecuted* *myfluideeclosuretobecuted* myfluid
/objects/volumetric-regions/change-type *myfluideeclosuretobecuted* * () fluid
/boundary/manage/type inlet* () velocity-inlet
/boundary/manage/type outlet* () pressure-outlet
/objects/volumetric-regions/scoped-prism/set/create "control-1" aspect-ratio 5 1 1.2 myfluideeclosuretobecutedcomponent:myfluideeclosuretobecutedcomponent-myfluideeclosuretobecuted1 fluid-regions selected-labels *wall*
/mesh/auto-mesh * no  scoped  pyramids hexcore  yes
/report/cell-quality-limits *()
/switch-to-solution-mode yes
/define/models/viscous/ke-realizable? yes
/define/models/viscous/near-wall-treatment enhanced-wall-treatment? yes quit
/define/boundary-conditions/fluid myfluid no no no no no 0 no 0 no 0 no 0 no 0 no 0 no no no no no 
/define/boundary-conditions/set/velocity-inlet *inlet_velocity* () vmag no 3 quit
/define/models/energy? yes no no no yes
/define/boundary-conditions/set/velocity-inlet *inlet_velocity* () temperature no 290 quit
/define/boundary-conditions/set/pressure-outlet *outlet_pressure* () gauge-pressure no 100 quit 
/solve/report-definitions/add out-vel-rdef surface-areaavg surface-names *outlet_pressure* () field velocity-magnitude quit 
/solve/report-plots/add out-vel-rplot report-defs out-vel-rdef () quit
/display/surface/plane-surface xz-plane-0 zx-plane 0
/file/write-case-data "D:/WorkBench/SimpleModel/rocket1.cas.h5" ok
/solve/iterate 100 
/display/objects/create contour vel-mid surfaces-list xz-plane-0 () field velocity-magnitude quit
"""
