cmd="""
/file/import/cad-options/tessellation  cfd-surface-mesh no 5 50 18 no no
/file/import/cad yes  D:/WorkBench/SimpleModel/rocket.scdoc yes 40 yes mm
/scoped-sizing/delete-size-field
/scoped-sizing/create control-1 boi object-faces yes yes *boi* 3 1.2
/scoped-sizing/compute
/file/write-size-field D:/WorkBench/SimpleModel/tempsize.sf
/file/import/cad-options/tessellation  cfd-surface-mesh yes D:/WorkBench/SimpleModel/tempsize.sf
/file/import/cad yes D:/WorkBench/SimpleModel/rocket.scdoc no yes 40 yes mm ok
/objects/volumetric-regions/compute *myfluideeclosuretobecuted* no
/objects/volumetric-regions/rename * *myfluideeclosuretobecuted* *myfluideeclosuretobecuted* myfluid
/objects/volumetric-regions/change-type *myfluideeclosuretobecuted* * () fluid
/boundary/manage/type inlet* () mass-flow-inlet
/boundary/manage/type outlet* () pressure-outlet
/objects/volumetric-regions/scoped-prism/set/create control-1 aspect-ratio 8 5 1.2 myfluideeclosuretobecutedcomponent:myfluideeclosuretobecutedcomponent-myfluideeclosuretobecuted1 fluid-regions selected-labels *wall*
/mesh/auto-mesh * no  scoped  pyramids hexcore  yes
/report/cell-quality-limits *()
/file/write-mesh D:/WorkBench/SimpleModel/rocket.msh
/switch-to-solution-mode yes






/file/read-case D:/WorkBench/SimpleModel/rocket.msh
/define/models/solver/density-based-implicit yes
/define/units length mm
/define/models/energy? yes
/define/models/viscous/ke-realizable? yes
/define/models/viscous/near-wall-treatment enhanced-wall-treatment? yes quit


/define/materials/copy fluid air gas
define/materials/change-create gas gas yes ideal-gas yes piecewise-linear 3 286.2 64.2 296.2 74.2 312.2 96.6 yes  kinetic-theory yes  sutherland three-coefficient-method 1.75e-5 273.11 110.56 no no no
/define/boundary-conditions/set/fluid myfluid () material yes gas quit quit

/define/operating-conditions/operating-pressure 0

/define/boundary-conditions/set/mass-flow-inlet *inlet_mass_flow_rate* () flow-spec yes mass-flow no 50 supersonic-or-initial-gauge-pressure no 1  ke-spec no yes  turb-intensity 2 turb-length-scale 1000 t0 no 299 quit
/define/boundary-conditions/set/pressure-outlet *outlet_pressure* () ke-spec no yes gauge-pressure no 98000 p-profile-multiplier 2 turb-intensity 2 turb-length-scale 50000 t0 no 298 quit

report/reference-values/pressure 9800


/solve/set/flux-type 1
/solve/set/gradient-scheme no yes
/solve/set/discretization-scheme/k 0
/solve/set/discretization-scheme/amg-c 0
/solve/set/discretization-scheme/epsilon 0

/solve/monitors/residual/convergence-criteria 0.000001 0.000001 0.000001 0.000001 0.000001 0.000001 0.000001

/solve/report-definitions/add mass-flow-rate  flux-massflow zone-names  *outlet_pressure*  *inlet_mass* () average-over 3 report-type flux-massflow quit
/solve/report-files/add mass-flow-rate frequency 2 report-defs mass-flow-rate () quit
/solve/report-plots/add mass-flow-rate frequency 2 report-defs mass-flow-rate () quit

/solve/report-definitions/add surface-facetmax-pressure surface-facetmax surface-names *wall* () average-over 3 field pressure quit
/solve/report-files/add surface-facetmax-pressure frequency 2 report-defs surface-facetmax-pressure () quit
/solve/report-plots/add surface-facetmax-pressure frequency 2 report-defs surface-facetmax-pressure () quit



/solve/report-definitions/add surface-facetmin-pressure surface-facetmin surface-names *wall* () average-over 3 field pressure quit
/solve/report-files/add surface-facetmin-pressure frequency 2 report-defs surface-facetmin-pressure () quit
/solve/report-plots/add surface-facetmin-pressure frequency 2 report-defs surface-facetmin-pressure () quit

/solve/report-definitions/add surface-facetmax-temperature surface-facetmax surface-names *wall* () average-over 3 field temperature quit
/solve/report-files/add surface-facetmax-temperature frequency 2 report-defs surface-facetmax-temperature () quit
/solve/report-plots/add surface-facetmax-temperature frequency 2 report-defs surface-facetmax-temperature () quit

/solve/report-definitions/add surface-facetmin-temperature surface-facetmin surface-names *wall* () average-over 3 field temperature quit
/solve/report-files/add surface-facetmin-temperature frequency 2 report-defs surface-facetmin-temperature () quit
/solve/report-plots/add surface-facetmin-temperature frequency 2 report-defs surface-facetmin-temperature () quit


/file/auto-save/data-frequency 2 retain-most-recent-files yes max-files 10 root-name D:/WorkBench/SimpleModel/rocket

solve/initialize/hyb-initialization

/solve/set/number-of-iterations 1000 
solve/set/reporting-interval 10
/define/profiles/update-interval 10

/solve/set/solution-steering yes transonic yes yes
/solve/set/set-solution-steering 100 0 20 5 200 0.75 4 100 200 400 500 0.75 yes
/file/write-case D:/WorkBench/SimpleModel/rocket.cas.h5





/define/models/species/species-transport? yes mixture-template
/define/materials/change-create mixture-template mixture-template yes 2 air gas 0 0 yes incompressible-ideal-gas yes mixing-law yes ideal-gas-mixing-law yes mass-weighted-mixing-law no no
/define/boundary-conditions/set/mass-flow-inlet *inlet_mass_flow* () mf no 1 quit
/solve/monitors/residual/convergence-criteria 0.000001 0.000001 0.000001 0.000001 0.000001 0.000001 0.000001

/solve/set/number-of-iterations 1000
/solve/set/reporting-interval 10
/define/profiles/update-interval 10

"""


"""
/switch-to-solution-mode yes
/define/models/solver/density-based-implicit yes
/define/units length mm
/define/models/energy? yes
/define/models/viscous/ke-realizable? yes
/define/models/viscous/near-wall-treatment enhanced-wall-treatment? yes quit

/define/materials/copy fluid air gas
/define/boundary-conditions/set/fluid myfluid () material yes gas quit quit
/define/materials/change-create gas gas yes ideal-gas yes constant 1000.43 yes  kinetic-theory yes  sutherland three-coefficient-method 1.75e-5 273.11 110.56 no no no

/define/operating-conditions/operating-pressure 0

/define/boundary-conditions/set/mass-flow-inlet *inlet_mass_flow_rate* () flow-spec yes mass-flow no 50 supersonic-or-initial-gauge-pressure no 1  ke-spec no yes  turb-intensity 2 turb-length-scale 1000 t0 no 299 quit
/define/boundary-conditions/set/pressure-outlet *outlet_pressure* () ke-spec no yes gauge-pressure no 98000 p-profile-multiplier 2 turb-intensity 2 turb-length-scale 50000 t0 no 298 quit

/report/reference-values/pressure 9800

/solve/set/flux-type 1
/solve/set/gradient-scheme no yes
/solve/set/discretization-scheme/k 0
/solve/set/discretization-scheme/amg-c 0
/solve/set/discretization-scheme/epsilon 0

/solve/monitors/residual/convergence-criteria 0.000001 0.000001 0.000001 0.000001 0.000001 0.000001 0.000001

/solve/report-definitions/add mass-flow-rate  flux-massflow zone-names  *outlet_pressure*  *inlet_mass* () average-over 3 report-type flux-massflow quit
/solve/report-files/add report-file-0 frequency 2 report-defs mass-flow-rate () quit
/solve/report-plots/add mass-flow-rate frequency 2 report-defs mass-flow-rate () quit


/file/auto-save/data-frequency 2 retain-most-recent-files yes max-files 10 root-name D:/WorkBench/SimpleModel/rocket

/solve/initialize/hyb-initialization

/solve/set/number-of-iterations 1000 
/solve/set/reporting-interval 10
/define/profiles/update-interval 10

/solve/set/solution-steering yes transonic yes yes
/solve/set/set-solution-steering 100 0 20 5 200 0.75 4 100 200 400 500 0.75 yes
/file/write-case D:/WorkBench/SimpleModel/rocket.cas.h5




/define/models/species/species-transport? yes mixture-template
/define/materials/change-create mixture-template mixture-template yes 2 air gas 0 0 yes incompressible-ideal-gas yes mixing-law yes ideal-gas-mixing-law yes mass-weighted-mixing-law no no
/define/boundary-conditions/set/mass-flow-inlet *inlet_mass_flow* () mf no 1 quit
/solve/monitors/residual/convergence-criteria 0.000001 0.000001 0.000001 0.000001 0.000001 0.000001 0.000001

/solve/set/number-of-iterations 1000
/solve/set/reporting-interval 10
/define/profiles/update-interval 10
"""


def createparameter():
    cmd="""
define/named-expressions/add cp_specific_heat definition "1006.43 [J kg^-1 K^-1]" input-parameter yes  quit
define/named-expressions/add mass_flow_rate definition "1 [kg s^-1]" input-parameter yes  quit
define/named-expressions/add initial_guage_pressure_inlet definition "0 [Pa]" input-parameter yes  quit
define/named-expressions/add turbulent_intensity_inlet definition "0.05" input-parameter yes  quit
define/named-expressions/add thermal_inlet definition "300 [K]" input-parameter yes  quit
define/named-expressions/add guage_pressure definition "0 [Pa]" input-parameter yes  quit
define/named-expressions/add initial_guage_pressure_outlet definition "0 [Pa]" input-parameter yes  quit
define/named-expressions/add turbulent_intensity_outlet definition "0.05" input-parameter yes  quit
define/named-expressions/add thermal_outlet definition "300 [K]" input-parameter yes  quit

(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Materials|Fluid|gas"))
(cx-gui-do cx-list-tree-right-click "NavigationPane*List_Tree1" )
(cx-gui-do cx-activate-item "MenuBar*PopupMenuTree-gas*Edit...")
(cx-gui-do cx-set-list-selections "Create/Edit Materials*Table2*Table1(Properties)*DropDownList5(Cp (Specific Heat))" '( 7))
(cx-gui-do cx-activate-item "Create/Edit Materials*Table2*Table1(Properties)*DropDownList5(Cp (Specific Heat))")
(cx-gui-do cx-activate-item "Create/Edit Materials*PanelButtons*PushButton3(Change/Create)")
(cx-gui-do cx-activate-item "Create/Edit Materials*PanelButtons*PushButton1(Close)")


(cx-gui-do cx-set-list-tree-selections "NavigationPane*List_Tree1" (list "Setup|Boundary Conditions|Inlet|inlet_mass_flow_rate:rocketneedtomove:upperfaceonrocket:myfluideeclosuretobecutedcomponent:myfluideeclosuretobecutedcomponent- (mass-flow-inlet, id=6)"))
(cx-gui-do cx-list-tree-right-click "NavigationPane*List_Tree1" )
(cx-gui-do cx-activate-item "MenuBar*PopupMenuTree-inlet_mass_flow:rocketneedtomove:upperfaceonrocket:myfluideeclosuretobecutedcomponent:myfluideeclosuretobecutedcomponent- (mass-flow-inlet, id=6)*Edit...")
(cx-gui-do cx-enable-apply-button "Mass-Flow Inlet")
(cx-gui-do cx-set-expression-entry "Mass-Flow Inlet*Frame2*Frame2*Frame1(Momentum)*Table1*Table8*ExpressionEntry1(Mass Flow Rate)" '("mass_flow_rate" . 1))
(cx-gui-do cx-activate-item "Mass-Flow Inlet*PanelButtons*PushButton1(OK)")
(cx-gui-do cx-activate-item "Mass-Flow Inlet*PanelButtons*PushButton2(Cancel)")
/display/objects/create contour vel-mid surfaces-list xz-plane-0 () field velocity-magnitude quit
    """