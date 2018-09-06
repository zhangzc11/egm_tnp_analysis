from libPython.tnpClassUtils import tnpSample

### qll stat
#eosDir1 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v1/'
#eosDir2 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v2/'
#eosDirREC = 'eos/cms/store/group/phys_egamma/tnp/80X/RecoSF/RECOSFs_2016/'
#eosWinter17 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/Moriond17_v1/'
eosMoriond18 = '/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_01292018/Moriond18_V1/'
eos2018Data_102X = '/eos/cms/store/group/phys_egamma/micheli/TnP/ntuples_20180831/2018Data_1/'

Data2018_102X = {
    ### MiniAOD TnP for IDs scale 
    'DY_madgraph_part012' : tnpSample('DY_madgraph_part012', 
                                       eos2018Data_102X + 'mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_part012.root',
                                       isMC = True, nEvts =  -1 ),

#    'DY_madgraph_part0' : tnpSample('DY_madgraph_part0', 
#                                       eos2018Data_102X + 'mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_part0.root',
#                                       isMC = True, nEvts =  -1 ),
#    'DY_madgraph_part1' : tnpSample('DY_madgraph_part1', 
#                                       eos2018Data_102X + 'mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_part1.root',
#                                       isMC = True, nEvts =  -1 ),
#    'DY_madgraph_part2' : tnpSample('DY_madgraph_part2', 
#                                       eos2018Data_102X + 'mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_part2.root',
#                                       isMC = True, nEvts =  -1 ),
    'data_Run2018Av1' : tnpSample('data_Run2018Av1' , eos2018Data_102X + 'data/Prompt2018_RunA_v1.root' , lumi = 20),  
    'data_Run2018Av2' : tnpSample('data_Run2018Av2' , eos2018Data_102X + 'data/Prompt2018_RunA_v2.root' , lumi = 0),
    'data_Run2018Av3' : tnpSample('data_Run2018Av3' , eos2018Data_102X + 'data/Prompt2018_RunA_v3.root' , lumi = 0),

    'data_Run2018Bv1' : tnpSample('data_Run2018Bv1' , eos2018Data_102X + 'data/Prompt2018_RunB_v1.root' , lumi = 0),
    'data_Run2018Bv2' : tnpSample('data_Run2018Bv2' , eos2018Data_102X + 'data/Prompt2018_RunB_v2.root' , lumi = 0),

    'data_Run2018Cv1' : tnpSample('data_Run2018Cv1' , eos2018Data_102X + 'data/Prompt2018_RunC_v1.root' , lumi = 0),
    'data_Run2018Cv2' : tnpSample('data_Run2018Cv2' , eos2018Data_102X + 'data/Prompt2018_RunC_v2.root' , lumi = 0),

    'data_Run2018Dv2' : tnpSample('data_Run2018Dv2' , eos2018Data_102X + 'data/Prompt2018_RunD_v2.root' , lumi = 0),


    }



##about lumi: thse ntuples are done with /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-321221_13TeV_PromptReco_Collisions18_JSON.txt = with recorded luminosity : 31.71 /fb but ~20% are crashed. Also we need to update the single runs lumi


 
