import ROOT as rt
import numpy as np
import sys
import argparse
import os

print '** puReweighter requires root_numpy.'
print '** To install on lxplus: '
print 'pip install --user root_numpy'
from root_numpy import  tree2array, array2tree


puMC = {
    'Spring2016MC_PUscenarioV1' : [ 0.000829312873542, 0.00124276120498, 0.00339329181587, 0.00408224735376, 0.00383036590008, 
                                    0.00659159288946,  0.00816022734493, 0.00943640833116, 0.0137777376066,  0.017059392038,
                                    0.0213193035468,   0.0247343174676,  0.0280848773878,  0.0323308476564,  0.0370394341409,  
                                    0.0456917721191,   0.0558762890594,  0.0576956187107,  0.0625325287017,  0.0591603758776,
                                    0.0656650815128,   0.0678329011676,  0.0625142146389,  0.0548068448797,  0.0503893295063,  
                                    0.040209818868,    0.0374446988111,  0.0299661572042,  0.0272024759921,  0.0219328403791,
                                    0.0179586571619,   0.0142926728247,  0.00839941654725, 0.00522366397213, 0.00224457976761, 
                                    0.000779274977993, 0.000197066585944,7.16031761328e-05,0.0             , 0.0,
                                    0.0,        0.0,        0.0,        0.0,        0.0,    
                                    0.0,        0.0,        0.0,        0.0,        0.0],
    
    'Moriond17MC_mix_2016'      : [ 1.78653e-05 ,2.56602e-05 ,5.27857e-05 ,8.88954e-05 ,0.000109362 ,0.000140973 ,0.000240998 ,
                                    0.00071209  , 0.00130121 ,0.00245255  ,0.00502589  ,0.00919534  ,0.0146697   ,0.0204126   ,
                                    0.0267586   ,0.0337697   ,0.0401478   ,0.0450159   ,0.0490577   ,0.0524855   ,0.0548159   ,
                                    0.0559937   ,0.0554468   ,0.0537687   ,0.0512055   ,0.0476713   ,0.0435312   ,0.0393107   ,
                                    0.0349812   ,0.0307413   ,0.0272425   ,0.0237115   ,0.0208329   ,0.0182459   ,0.0160712   ,
                                    0.0142498   ,0.012804    ,0.011571    ,0.010547    ,0.00959489  ,0.00891718  ,0.00829292  , 
                                    0.0076195   ,0.0069806   ,0.0062025   ,0.00546581  ,0.00484127  ,0.00407168  ,0.00337681  ,
                                    0.00269893  ,0.00212473  ,0.00160208  ,0.00117884  ,0.000859662 ,0.000569085 ,0.000365431 ,
                                    0.000243565 ,0.00015688  ,9.88128e-05 ,6.53783e-05 ,3.73924e-05 ,2.61382e-05 ,2.0307e-05  ,
                                    1.73032e-05 ,1.435e-05   ,1.36486e-05 ,1.35555e-05 ,1.37491e-05 ,1.34255e-05 ,1.33987e-05 ,
                                    1.34061e-05 ,1.34211e-05 ,1.34177e-05 ,1.32959e-05 ,1.33287e-05 ],




    'Moriond18MC_mix_2017' :[3.39597497605e-05,    6.63688402133e-06,     1.39533611284e-05,     3.64963078209e-05,     6.00872171664e-05,     9.33932578027e-05,    0.000120591524486,
                             0.000128694546198,    0.000361697233219,     0.000361796847553,     0.000702474896113,     0.00133766053707,      0.00237817050805,     0.00389825605651,
                             0.00594546732588,     0.00856825906255,      0.0116627396044,       0.0148793350787,       0.0179897368379,       0.0208723871946,      0.0232564170641,
                             0.0249826433945,      0.0262245860346,       0.0272704617569,       0.0283301107549,       0.0294006137386,       0.0303026836965,      0.0309692426278,   
                             0.0308818046328,      0.0310566806228,       0.0309692426278,       0.0310566806228,       0.0310566806228,       0.0310566806228,      0.0307696426944,
                             0.0300103336052,      0.0288355370103,       0.0273233309106,       0.0264343533951,       0.0255453758796,       0.0235877272306,      0.0215627588047,
                             0.0195825559393,      0.0177296309658,       0.0160560731931,       0.0146022004183,       0.0134080690078,       0.0129586991411,      0.0125093292745,
                             0.0124360740539,      0.0123547104433,       0.0123953922486,       0.0124360740539,       0.0124360740539,       0.0123547104433,      0.0124360740539,
                             0.0123387597772,      0.0122414455005,       0.011705203844,        0.0108187105305,       0.00963985508986,      0.00827210065136,     0.00683770076341,
                             0.00545237697118,     0.00420456901556,      0.00367513566191,      0.00314570230825,      0.0022917978982,       0.00163221454973,     0.00114065309494,
                             0.000784838366118,    0.000533204105387,     0.000358474034915,     0.000238881117601,     0.0001984254989,       0.000157969880198,    0.00010375646169,
                             6.77366175538e-05,    4.39850477645e-05,     2.84298066026e-05,     1.83041729561e-05,     1.17473542058e-05,     7.51982735129e-06,    6.16160108867e-06,
                             4.80337482605e-06,    3.06235473369e-06,     1.94863396999e-06,     1.23726800704e-06,     7.83538083774e-07,     4.94602064224e-07,    3.10989480331e-07,
                             1.94628487765e-07,    1.57888581037e-07,     1.2114867431e-07,      7.49518929908e-08,     4.6060444984e-08,      2.81008884326e-08,    1.70121486128e-08,
                             1.02159894812e-08],






}

### MC pu scenario to be used
#puMCscenario = 'Spring2016MC_PUscenarioV1'
puMCscenario = 'Moriond18MC_mix_2017'
puDirEOS = '/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_01162018/PU/'

#### Compute weights for all data epoch specified below
puDataEpoch = {
    '2017_runB' : puDirEOS + 'pileup_2017_RUNB.root',
    '2017_runC' : puDirEOS + 'pileup_2017_RUNC.root',
    '2017_runD'  : puDirEOS +'pileup_2017_RUND.root' ,
    '2017_runE'  : puDirEOS +'pileup_2017_RUNE.root' ,
    '2017_runF' : puDirEOS + 'pileup_2017_RUNF.root',    
    '2017_runBCDEF' : puDirEOS + 'pileup_2017_41fb.root',
    }

nVtxDataEpoch = {
    '2016_runBCD' : 'etc/inputs/nVtx_2016_runBCD.root',
    '2016_runEF'  : 'etc/inputs/nVtx_2016_runEF.root' ,
    '2016_runGH'  : 'etc/inputs/nVtx_2016_runGH.root' ,
}

rhoDataEpoch = {
    '2016_runE'   : 'etc/inputs/rho_pu_runE.root',
    '2016_runGH'  : 'etc/inputs/rho_pu_runGH.root',
}





def reweight( sample, puType = 0  ):
    if sample.path is None:
        print '[puReweighter]: Need to know the MC tree (option --mcTree or sample.path)'
        sys.exit(1)
    

### create a tree with only weights that will be used as friend tree for reweighting different lumi periods
    print 'Opening mc file: ', sample.path[0]
    fmc = rt.TFile(sample.path[0],'read')
    tmc = None
    if sample.tnpTree is None:
        dirs = fmc.GetListOfKeys()
        for d in dirs:
            if (d.GetName() == "sampleInfo"): continue
            tmc = fmc.Get("%s/fitter_tree" % d.GetName())
    else:
        tmc = fmc.Get(sample.tnpTree)
    

#### can reweight vs nVtx but better to reweight v truePU
    puMCnVtx = []
    puMCrho = []
    if   puType == 1 :
        hmc   = rt.TH1F('hMC_nPV'  ,'MC nPV'  , 75,-0.5,74.5)
        tmc.Draw('event_nPV>>hMC_nPV','','goff')
        hmc.Scale(1/hmc.Integral())
        for ib in range(1,hmc.GetNbinsX()+1):
            puMCnVtx.append( hmc.GetBinContent(ib) )
        print 'len nvtxMC = ',len(puMCnVtx)

    elif puType == 2 :
        hmc   = rt.TH1F('hMC_rho'  ,'MC #rho'  , 75,-0.5,74.5)
        tmc.Draw('rho>>hMC_rho','','goff')
        hmc.Scale(1/hmc.Integral())
        for ib in range(1,hmc.GetNbinsX()+1):
            puMCrho.append( hmc.GetBinContent(ib) )
        print 'len rhoMC = ',len(puMCrho)
    

    puDataDist = {}
    puDataArray= {}
    weights = {}
    epochKeys = puDataEpoch.keys()
    if puType == 1  : epochKeys = nVtxDataEpoch.keys()
    if puType == 2  : epochKeys = rhoDataEpoch.keys()
 
    for pu in epochKeys:
        fpu = None
        if   puType == 1 : fpu = rt.TFile(nVtxDataEpoch[pu],'read')
        elif puType == 2 : fpu = rt.TFile(rhoDataEpoch[pu],'read')
        else             : fpu = rt.TFile(puDataEpoch[pu],'read')
        puDataDist[pu] = fpu.Get('pileup').Clone('puHist_%s' % pu)
        puDataDist[pu].Scale(1./puDataDist[pu].Integral())
        puDataDist[pu].SetDirectory(0)
        puDataArray[pu] = []
        for ipu in range(len(puMC[puMCscenario])):
            ibin_pu  = puDataDist[pu].GetXaxis().FindBin(ipu+0.00001)
            puDataArray[pu].append(puDataDist[pu].GetBinContent(ibin_pu))
        print 'puData[%s] length = %d' % (pu,len(puDataArray[pu]))
        fpu.Close()
        weights[pu] = []

    mcEvts = tree2array( tmc, branches = ['weight','truePU','event_nPV','rho'] )


    pumc = puMC[puMCscenario]
    if   puType == 1:  pumc = puMCnVtx
    elif puType == 2:  pumc = puMCrho
    else            :  pumc = puMC[puMCscenario]

    puMax = len(pumc)
    print '-> nEvtsTot ', len(mcEvts)
    for ievt in xrange(len(mcEvts)):
        if ievt%100000000 == 0 :            print 'iEvt:',ievt
        evt = mcEvts[ievt]
        for pu in epochKeys:
            pum = -1
            pud = -1
            if puType == 1 and evt['event_nPV'] < puMax:
                pud = puDataArray[pu][evt['event_nPV']]
                pum = pumc[evt['event_nPV']]
            if puType == 2 and int(evt['rho']) < puMax:
                pud = puDataArray[pu][int(evt['rho'])]
                pum = pumc[int(evt['rho'])]
            elif puType == 0:
#                if ievt%1000: print pu, evt['truePU']
                if evt['truePU']> 0 and evt['truePU']<99: 
                    pud = puDataArray[pu][evt['truePU']] 
                    pum = pumc[evt['truePU']]
            puw = 1
            if pum > 0: 
                puw  = pud/pum

            if evt['weight'] > 0 : totw = +puw
            else                 : totw = -puw
            weights[pu].append( ( puw,totw) )

    newFile    = rt.TFile( sample.puTree, 'recreate')

    for pu in epochKeys:
        treeWeight = rt.TTree('weights_%s'%pu,'tree with weights')
        wpuarray = np.array(weights[pu],dtype=[('PUweight',float),('totWeight',float)])
        array2tree( wpuarray, tree = treeWeight )
        treeWeight.Write()

    newFile.Close()    
    fmc.Close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='tnp EGM pu reweighter')
    parser.add_argument('--mcTree'  , dest = 'path',  default = None, help = 'MC tree to compute weights for')
    parser.add_argument('puTree'    , default = None                , help = 'output puTree')

    args = parser.parse_args()
    args.path = [args.path]
    reweight(args)





