from libPython.tnpClassUtils import tnpSample

### qll stat
#eosDir1 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v1/'
#eosDir2 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v2/'
#eosDirREC = 'eos/cms/store/group/phys_egamma/tnp/80X/RecoSF/RECOSFs_2016/'
#eosWinter17 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/Moriond17_v1/'
eosMoriond18 = '/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_01292018/Moriond18_V1/'
eos2018Data_102X = '/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_20180920/2018Data_1/'
eos2017Data_94X = '/eos/cms/store/group/phys_egamma/swmukher/ntuple_2017_v2/' #this is needed b/c we want to study the SF of 2018 data w.r.t. 2017 94X MC
eos2017Data_94X_ForRecoSF = '/eos/cms/store/group/phys_egamma/swmukher/tnp/ID_V2_2017/'
eos2018Data_102X_EcalNoiseFix_200kRelVal = '/eos/cms/store/group/phys_egamma/swmukher/ecal_noise/ECAL_NOISE/'

Data2018_102X = {
    ### MiniAOD TnP for IDs scale 

    'DY_RelValZEE'              : tnpSample('DY_RelValZEE',
                                            eos2018Data_102X_EcalNoiseFix_200kRelVal + 'mc/RelValZEE_13.root',
                                            isMC = True, nEvts =  -1 ),
    

    'data_Run2018Av123' : tnpSample('data_Run2018Av123' , eos2018Data_102X_EcalNoiseFix_200kRelVal + 'data/Prompt2018_RunA_v123.root' , lumi = 12.77),  

    'data_Run2018Bv12' : tnpSample('data_Run2018Bv12' , eos2018Data_102X_EcalNoiseFix_200kRelVal + 'data/Prompt2018_RunB_v12.root' , lumi = 6.78),

    'data_Run2018Cv123' : tnpSample('data_Run2018Cv12' , eos2018Data_102X_EcalNoiseFix_200kRelVal + 'data/Prompt2018_RunC_v123.root' , lumi = 6.61),

    'data_Run2018Dv2' : tnpSample('data_Run2018Dv2' , eos2018Data_102X_EcalNoiseFix_200kRelVal + 'data/Prompt2018_RunD_v2.root' , lumi = 24.1), 


    }



##about lumi: thse ntuples are done with /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-321221_13TeV_PromptReco_Collisions18_JSON.txt = with recorded luminosity : 31.71 /fb but ~20% are crashed. Also we need to update the single runs lumi


 
