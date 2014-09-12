#
# Copyright (c) 2014 A.Y. Rodriguez-Marrero and E. Fernandez-del-Castillo
# Based on the code of the CMSData Analysis School 2014 Long Exercise: 
# Search for the Higgs in ZZ -> 4 leptons decay channel (available 
# at https://github.com/bachtis/CMSDAS)
#

import ROOT
ROOT.gROOT.ProcessLine(".x tdrstyle.C")

from OutreachExercise2010.DecaysToLeptons.sources import sources

# Import the Analyzer you want to run:
# FourLeptonAnalyzer or TwoLeptonAnalyzer
# by uncommenting the appropiate line below. 

#from OutreachExercise2010.DecaysToLeptons.FourLeptonAnalyzer import FourLeptonAnalyzer as MyAnalyzer
from OutreachExercise2010.DecaysToLeptons.TwoLeptonAnalyzer import TwoLeptonAnalyzer as MyAnalyzer

analyzer = MyAnalyzer()

analyzer.declareHistos()

for sample in sources:
    # maxEv defines the maximum number of events to analyze
    # set it to -1 to analyze all available events; 
    analyzer.processSample(sample, maxEv=100)

# uncommet line below to export selected data to a json file
#analyzer.exportData()
