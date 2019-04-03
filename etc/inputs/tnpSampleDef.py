from libPython.tnpClassUtils import tnpSample

### qll stat
#eosDir1 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v1/'
#eosDir2 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v2/'
#eosDirREC = 'eos/cms/store/group/phys_egamma/tnp/80X/RecoSF/RECOSFs_2016/'
#eosWinter17 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/Moriond17_v1/'
eosMoriond18_OOTid = '/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_07042018_wOOTid/2017Data_FullJson/'
eosLegacy16_OOTid = '/eos/cms/store/group/phys_susy/razor/zhicaiz/TnP/ntuples_GED_02Apr2019/'
eosMoriond18 = '/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_01292018/Moriond18_V1/'

Moriond18_94X = {
    ### MiniAOD TnP for IDs scale factors
    'DY_madgraph'          : tnpSample('DY_madgraph',
                                       eosMoriond18 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_all.root',
                                       isMC = True, nEvts =  -1 ),
    'DY_madgraph_Moriond18' : tnpSample('DY_madgraph_Moriond18', 
                                       eosMoriond18 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_all.root',
                                       isMC = True, nEvts =  -1 ),
    'DY_amcatnlo_Moriond18' : tnpSample('DY_amcatnlo_Moriond18', 
                                       eosMoriond18 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_all.root',
                                       isMC = True, nEvts =  -1 ),

    'data_Run2017B' : tnpSample('data_Run2017B' , eosMoriond18 + 'data/TnPTree_17Nov2017_RunB.root' , lumi = 4.891 ),
    'data_Run2017C' : tnpSample('data_Run2017C' , eosMoriond18 + 'data/TnPTree_17Nov2017_RunC.root' , lumi = 9.9 ),
    'data_Run2017D' : tnpSample('data_Run2017D' , eosMoriond18 + 'data/TnPTree_17Nov2017_RunD.root' , lumi = 4.36 ),
    'data_Run2017E' : tnpSample('data_Run2017E' , eosMoriond18 + 'data/TnPTree_17Nov2017_RunE.root' , lumi = 9.53 ),
    'data_Run2017F' : tnpSample('data_Run2017F' , eosMoriond18 + 'data/TnPTree_17Nov2017_RunF.root' , lumi = 13.96 ),

    }


Moriond18_94X_OOTid = {
    ### MiniAOD TnP for IDs scale factors
    'DY_madgraph_Moriond18' : tnpSample('DY_madgraph_Moriond18', 
                                       eosMoriond18_OOTid + 'mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_all.root',
                                       isMC = True, nEvts =  -1 ),

    'data_Run2017B' : tnpSample('data_Run2017B' , eosMoriond18_OOTid + 'data/TnPTree_17Nov2017_RunB.root' , lumi = 4.891 ),
    'data_Run2017C' : tnpSample('data_Run2017C' , eosMoriond18_OOTid + 'data/TnPTree_17Nov2017_RunC.root' , lumi = 9.9 ),
    'data_Run2017D' : tnpSample('data_Run2017D' , eosMoriond18_OOTid + 'data/TnPTree_17Nov2017_RunD.root' , lumi = 4.36 ),
    'data_Run2017E' : tnpSample('data_Run2017E' , eosMoriond18_OOTid + 'data/TnPTree_17Nov2017_RunE.root' , lumi = 9.53 ),
    'data_Run2017F' : tnpSample('data_Run2017F' , eosMoriond18_OOTid + 'data/TnPTree_17Nov2017_RunF.root' , lumi = 13.96 ),

    }


Legacy16_OOTid = {
    'DY_madgraph_Legacy16' : tnpSample('DY_madgraph_Legacy16', 
                                       eosLegacy16_OOTid + 'mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_all.root',
                                       isMC = True, nEvts =  -1 ),

    'data_Run2016B' : tnpSample('data_Run2016B' , eosLegacy16_OOTid + 'data/TnPTree_Run2016B.root' , lumi = 5.89 ),
    'data_Run2016C' : tnpSample('data_Run2016C' , eosLegacy16_OOTid + 'data/TnPTree_Run2016C.root' , lumi = 2.646 ),
    'data_Run2016D' : tnpSample('data_Run2016D' , eosLegacy16_OOTid + 'data/TnPTree_Run2016D.root' , lumi = 4.353 ),
    'data_Run2016E' : tnpSample('data_Run2016E' , eosLegacy16_OOTid + 'data/TnPTree_Run2016E.root' , lumi = 4.05 ),
    'data_Run2016F' : tnpSample('data_Run2016F' , eosLegacy16_OOTid + 'data/TnPTree_Run2016F.root' , lumi = 3.16 ),
    'data_Run2016G' : tnpSample('data_Run2016G' , eosLegacy16_OOTid + 'data/TnPTree_Run2016G.root' , lumi = 7.391 ),
    'data_Run2016H' : tnpSample('data_Run2016H' , eosLegacy16_OOTid + 'data/TnPTree_Run2016H.root' , lumi = 8.762 ),
    }


