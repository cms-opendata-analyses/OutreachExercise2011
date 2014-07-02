import ROOT
ROOT.gROOT.ProcessLine(".x tdrstyle.C")
from OutreachExercise2010.FourLeptons.sources import *
from OutreachExercise2010.FourLeptons.FourLeptonAnalyzer import *

analyzer = FourLeptonAnalyzer()

analyzer.declareHistos()

for sample in sources:
    analyzer.processSample(sample, 5000)

analyzer.exportData()
