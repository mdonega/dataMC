import sys
import os
from quantileRegression import quantileRegression

class mycolors:
   red = '\033[91m'
   green = '\033[92m'
   blue = '\033[94m'
   yan = '\033[96m'
   cWhite = '\033[97m'
   yellow = '\033[93m'
   magenta = '\033[95m'
   grey = '\033[90m'
   black = '\033[90m'
   default = '\033[0m'

print "sys.argv", sys.argv
print mycolors.green+"Training quantile regressions on"+mycolors.default
dataMC = sys.argv[1]
print "Data/MC = ", dataMC
Y = sys.argv[2]
print "Y = ", Y
quantiles  = [ float(sys.argv[3]) ]
print "Quantile = ", quantiles
startEvt = int(sys.argv[4])
stopEvt  = int(sys.argv[5])
print "Events in [", startEvt, ", ", stopEvt, "]"
imaxDepth  = int(sys.argv[6])
iminLeaf   = int(sys.argv[7])
print "maxDepth / minLeaf = ", imaxDepth, " , " , iminLeaf
sEBEE = ""
if len(sys.argv) == 9 : 
   sEBEE      = sys.argv[8]
print "EB/EE = ", sEBEE

qr = quantileRegression(sys.argv[1])

outputDir = "/mnt/t3nfs01/data01/shome/mdonega/dataMC/MTR/weights_MaxDepth_" + str(imaxDepth) + "_minLeaf_" + str(iminLeaf)
if (not os.path.exists(outputDir)):
   print 'Creating output dir:', outputDir
   os.mkdir(outputDir)

if dataMC == "data":
   #qr.loadDF("/mnt/t3nfs01/data01/shome/mdonega/lxplus/work/CMSSW_8_0_26_patch1/src/diphotons/Analysis/macros/double_ele_v9_moriond17_mc/",
   #          "cicNoSigmaIetaIeta/trees/",
   #          ["Data_13TeV_EBHighR9", "Data_13TeV_EBLowR9", "Data_13TeV_EEHighR9", "Data_13TeV_EELowR9" ],
   #          startEvt, stopEvt, 12345)
   # to reduce memory consuption just load the locally pre-made h5 file
   qr.loadDFh5("/mnt/t3nfs01/data01/shome/mdonega/dataMC/MTR/df_data_0-2000000.h5", startEvt, stopEvt)
   for q in quantiles:
      # qr.trainQuantile(Y, q, outputDir, maxDepth = imaxDepth, minLeaf = iminLeaf)
      qr.trainQuantile(Y, q, outputDir, EBEE = sEBEE, maxDepth = imaxDepth, minLeaf = iminLeaf, useWeights=True)

elif dataMC == "mc":
   #qr.loadDF("/mnt/t3nfs01/data01/shome/mdonega/lxplus/work/CMSSW_8_0_26_patch1/src/diphotons/Analysis/macros/double_ele_v9_moriond17_mc/",
   #          "cicNoSigmaIetaIeta/trees/",
   #          ["DYJetsToLL_13TeV_EBHighR9", "DYJetsToLL_13TeV_EBLowR9", "DYJetsToLL_13TeV_EEHighR9", "DYJetsToLL_13TeV_EELowR9" ],
   #          startEvt, stopEvt, 12345)
   # to reduce memory consuption just load the locally pre-made h5 file
   qr.loadDFh5("/mnt/t3nfs01/data01/shome/mdonega/dataMC/MTR/df_mc_0-2000000.h5", startEvt, stopEvt)   
   for q in quantiles:
      # qr.trainQuantile(Y, q, outputDir, maxDepth = imaxDepth, minLeaf = iminLeaf)
      qr.trainQuantile(Y, q, outputDir, EBEE = sEBEE, maxDepth = imaxDepth, minLeaf = iminLeaf, useWeights=True)
      
else: print " ERROR: choose data or mc"



    
