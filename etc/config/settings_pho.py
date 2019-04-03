#############################################################
########## General settings
#############################################################
# flag to be Tested
flags = {
    'passingLoose80X'   : '(passingLoose80X  == 1)',
    'passingMedium80X'  : '(passingMedium80X == 1)',
    'passingTight80X'   : '(passingTight80X  == 1)',
    'passingLooseDelayedPhotonGED'   : '(passingLooseDelayedPhotonGED  == 1)',
    'passingMediumDelayedPhotonGED'  : '(passingMediumDelayedPhotonGED == 1)',
    'passingTightDelayedPhotonGED'   : '(passingTightDelayedPhotonGED  == 1)',
    }

baseOutDir = 'results/Legacy16_OOTid/tnpPhoID/runBCDEFGH/'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
tnpTreeDir = 'tnpPhoIDs'

samplesDef = {
    'data'   : tnpSamples.Legacy16_OOTid['data_Run2016B'].clone(),
    'mcNom'  : tnpSamples.Legacy16_OOTid['DY_madgraph_Legacy16'].clone(),
    'mcAlt'  : tnpSamples.Legacy16_OOTid['DY_madgraph_Legacy16'].clone(),
    'tagSel' : tnpSamples.Legacy16_OOTid['DY_madgraph_Legacy16'].clone(),
}
## can add data sample easily
samplesDef['data'].add_sample( tnpSamples.Legacy16_OOTid['data_Run2016C'] )
samplesDef['data'].add_sample( tnpSamples.Legacy16_OOTid['data_Run2016D'] )
samplesDef['data'].add_sample( tnpSamples.Legacy16_OOTid['data_Run2016E'] )
samplesDef['data'].add_sample( tnpSamples.Legacy16_OOTid['data_Run2016F'] )
samplesDef['data'].add_sample( tnpSamples.Legacy16_OOTid['data_Run2016G'] )
#samplesDef['data'].add_sample( tnpSamples.Legacy16_OOTid['data_Run2016H'] )

## some sample-based cuts... general cuts defined here after
## require mcTruth on MC DY samples and additional cuts
## all the samples MUST have different names (i.e. sample.name must be different for all)
## if you need to use 2 times the same sample, then rename the second one
#samplesDef['data'  ].set_cut('run >= 273726')
samplesDef['data' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_tnpTree(tnpTreeDir)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_tnpTree(tnpTreeDir)

if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_mcTruth()
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_mcTruth()
samplesDef['tagSel'].rename('mcAltSel_DY_madgraph')
samplesDef['tagSel'].set_cut('tag_Ele_pt > 35')

## set MC weight, simple way (use tree weight) 
#weightName = 'totWeight'
#if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)

## set MC weight, can use several pileup rw for different data taking 

weightName = 'weights_2016_runAll.totWeight'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_puTree('/eos/cms/store/group/phys_susy/razor/zhicaiz/TnP/ntuples_GED_02Apr2019/PU/mc/DY_madgraph_Moriond17_pho.pu.puTree.root')
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_puTree('/eos/cms/store/group/phys_susy/razor/zhicaiz/TnP/ntuples_GED_02Apr2019/PU/mc/DY_madgraph_Moriond17_pho.pu.puTree.root')
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_puTree('/eos/cms/store/group/phys_susy/razor/zhicaiz/TnP/ntuples_GED_02Apr2019/PU/mc/DY_madgraph_Moriond17_pho.pu.puTree.root')


#############################################################
########## bining definition  [can be nD bining]
#############################################################
biningDef = [
   { 'var' : 'ph_sc_eta' , 'type': 'float', 'bins': [-1.4442, -0.8, 0.0, 0.8, 1.4442] },
   { 'var' : 'ph_et' , 'type': 'float', 'bins': [20,35,50,100,200,500] },
]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut
cutBase   = 'tag_Ele_pt > 30 && abs(tag_sc_eta) < 2.17'

# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
additionalCuts = { 
   0 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   1 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   2 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   3 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   4 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   5 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   6 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   7 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   8 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   9 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
}

#### or remove any additional cut (default)
#additionalCuts = None

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",
    ]

tnpParAltSigFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    ]
     
tnpParAltBkgFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "alphaP[0.,-5.,5.]",
    "alphaF[0.,-5.,5.]",
    ]
        
