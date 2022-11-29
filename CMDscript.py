cmdCommand="""
/file/import/cad-options/tessellation  cfd-surface-mesh no {minSzie} {maxSzie} {curvature_Normal_Angle} no no
/file/import/cad yes "{rocketPath}" yes {feature_Angle} yes mm
/scoped-sizing/create "control-1" boi object-faces yes yes *boi* {boiSize} 1.2
/scoped-sizing/compute
/file/write-size-field "{rockettempsizepath}" ok
/file/import/cad-options/tessellation  cfd-surface-mesh yes "{rockettempsizepath}"
/file/import/cad yes "{rocketPath}" no yes 40 yes mm ok
/objects/volumetric-regions/compute *myfluideeclosuretobecuted* no
/objects/volumetric-regions/rename * *myfluideeclosuretobecuted* *myfluideeclosuretobecuted* myfluid
/objects/volumetric-regions/change-type *myfluideeclosuretobecuted* * () fluid
/boundary/manage/type inlet* () velocity-inlet
/boundary/manage/type outlet* () pressure-outlet
/objects/volumetric-regions/scoped-prism/set/create "control-1" aspect-ratio {firstAspectRatio} {boundaryNum} 1.2 myfluideeclosuretobecutedcomponent:myfluideeclosuretobecutedcomponent-myfluideeclosuretobecuted1 fluid-regions selected-labels *wall*
/mesh/auto-mesh * no  scoped  pyramids hexcore  yes
/report/cell-quality-limits *()
/switch-to-solution-mode yes
/define/models/viscous/ke-realizable? yes
/define/models/viscous/near-wall-treatment enhanced-wall-treatment? yes quit
/define/boundary-conditions/fluid myfluid no no no no no 0 no 0 no 0 no 0 no 0 no 0 no no no no no
/define/boundary-conditions/set/velocity-inlet *inlet_velocity* () vmag no {inletVelocity} quit
/define/models/energy? yes no no no yes
/define/boundary-conditions/set/velocity-inlet *inlet_velocity* () temperature no {inletTemp} quit
/define/boundary-conditions/set/pressure-outlet *outlet_pressure* () gauge-pressure no {outPressurelineEdit} quit
/solve/report-definitions/add out-vel-rdef surface-areaavg surface-names *outlet_pressure* () field velocity-magnitude quit
/solve/report-plots/add out-vel-rplot report-defs out-vel-rdef () quit
/display/surface/plane-surface xz-plane-0 zx-plane 0
/file/write-case "{rocketWriteCasePath}" ok
/solve/iterate {iterNum}
/file/write-case-data "{rocketWriteCasePath}" ok
/display/objects/create contour vel-mid surfaces-list xz-plane-0 () field velocity-magnitude quit
"""
