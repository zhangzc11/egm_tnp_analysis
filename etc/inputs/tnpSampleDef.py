from libPython.tnpClassUtils import tnpSample

### qll stat
eosDir1 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v1/'
eosDir2 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v2/'
eosDirREC = 'eos/cms/store/group/phys_egamma/tnp/80X/RecoSF/RECOSFs_2016/'
eosWinter17 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/Moriond17_v1/'
eosMoriond18 = '/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_01122018/Moriond18_V1/'

Moriond18_94X = {
    ### MiniAOD TnP for IDs scale factors
    'DY_madgraph'          : tnpSample('DY_madgraph',
                                       eosMoriond18 + 'mc/TnPTree_DYToLLM-50_TuneCUETP8M1_13TeV-madgraphMLM.root',
                                       isMC = True, nEvts = -1 ),
    'DY_madgraph_Moriond18' : tnpSample('DY_madgraph_Moriond18', 
                                       eosMoriond18 + 'mc/TnPTree_DYToLLM-50_TuneCUETP8M1_13TeV-madgraphMLM.root',
                                       isMC = True, nEvts = -1 ),
    'DY_amcatnlo_Moriond18' : tnpSample('DY_amcatnlo_Moriond18', 
                                       eosMoriond18 + 'mc/TnPTree_DYToLLM-50_TuneCUETP8M1_13TeV-madgraphMLM.root',
                                       isMC = True, nEvts = -1 ),

    'data_Run2017Bv1' : tnpSample('data_Run2017Bv1' , eosMoriond18 + 'data/TnPTree_SingleElectron_2017_RunBv1.root' , lumi = 2.396 ),
    'data_Run2017Bv2' : tnpSample('data_Run2017Bv2' , eosMoriond18 + 'data/TnPTree_SingleElectron_2017_RunBv2.root' , lumi = 2.396 ),
    'data_Run2017Cv1' : tnpSample('data_Run2017Cv1' , eosMoriond18 + 'data/TnPTree_SingleElectron_2017_RunCv1.root' , lumi = 3.3 ),
    'data_Run2017Cv2' : tnpSample('data_Run2017Cv2' , eosMoriond18 + 'data/TnPTree_SingleElectron_2017_RunCv2.root' , lumi = 3.3 ),
    'data_Run2017Cv3' : tnpSample('data_Run2017Cv3' , eosMoriond18 + 'data/TnPTree_SingleElectron_2017_RunCv3.root' , lumi = 3.3 ),
    'data_Run2017Dv1' : tnpSample('data_Run2017Dv1' , eosMoriond18 + 'data/TnPTree_SingleElectron_2017_RunDv1.root' , lumi = 4.36 ),
    'data_Run2017Ev1' : tnpSample('data_Run2017Ev1' , eosMoriond18 + 'data/TnPTree_SingleElectron_2017_RunEv1.root' , lumi = 9.53 ),

    }
