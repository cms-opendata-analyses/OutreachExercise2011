#
# XXX
#
import ROOT
ROOT.gROOT.ProcessLine(".x tdrstyle.C")

from OutreachExercise2010.DecaysToLeptons.sources import sources
#uncomment line below to run the FourLepton analysis
from OutreachExercise2010.DecaysToLeptons.FourLeptonAnalyzer \
    import FourLeptonAnalyzer
#uncomment line below to run the TwoLepton analysis
#from OutreachExercise2010.DecaysToLeptons.TwoLeptonAnalyzer \
#    import TwoLeptonAnalyzer

#uncomment line below to run the FourLepton analysis
analyzer = FourLeptonAnalyzer()
#uncomment line below to run the TwoLepton analysis
#analyzer = TwoLeptonAnalyzer()

analyzer.declareHistos()

for sample in sources:
    analyzer.processSample(sample, 1000000000)

analyzer.exportData()
