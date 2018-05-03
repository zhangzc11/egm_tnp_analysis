from libPython.tnpClassUtils import tnpSample

### qll stat
#eosDir1 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v1/'
#eosDir2 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v2/'
#eosDirREC = 'eos/cms/store/group/phys_egamma/tnp/80X/RecoSF/RECOSFs_2016/'
#eosWinter17 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/Moriond17_v1/'
#eosMoriond18 = '/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_01292018/Moriond18_V1/'
eosLegacy2016 = '/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_04162018-Legacy2016/Legacy16_V1/'

Legacy2016_94X = {
    ### MiniAOD TnP for IDs scale factors
#    'DY_madgraph_Moriond17' : tnpSample('DY_madgraph_Moriond17', 
#                                        eosLegacy2016 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_all.root',
#                                        isMC = True, nEvts =  -1 ),
    'DY_amcatnlo_Moriond17' : tnpSample('DY_amcatnlo_Moriond17', 
                                        eosLegacy2016 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia_all.root',
                                        isMC = True, nEvts =  -1 ),

    'data_Run2016Bv2' : tnpSample('data_Run2017Bv2' , eosLegacy2016 + 'data/TnPTree_07Aug17_Run2016Bv2.root' , lumi = 5.89 ),
    'data_Run2016C' : tnpSample('data_Run2017C' , eosLegacy2016 + 'data/TnPTree_07Aug17_Run2016C.root' , lumi = 2.646 ),
    'data_Run2016D' : tnpSample('data_Run2017D' , eosLegacy2016 + 'data/TnPTree_07Aug17_Run2016D.root' , lumi = 4.353 ),
    'data_Run2016E' : tnpSample('data_Run2017E' , eosLegacy2016 + 'data/TnPTree_07Aug17_Run2016E.root' , lumi = 4.05 ),
    'data_Run2016F' : tnpSample('data_Run2017F' , eosLegacy2016 + 'data/TnPTree_07Aug17_Run2016F.root' , lumi = 3.16 ),
    'data_Run2016G' : tnpSample('data_Run2017G' , eosLegacy2016 + 'data/TnPTree_07Aug17_Run2016F.root' , lumi = 7.391 ),
    'data_Run2016H' : tnpSample('data_Run2017H' , eosLegacy2016 + 'data/TnPTree_07Aug17_Run2016F.root' , lumi = 8.762 ),

    }
