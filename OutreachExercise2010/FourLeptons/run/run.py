#
# XXX
#
import ROOT
ROOT.gROOT.ProcessLine(".x tdrstyle.C")

from OutreachExercise2010.FourLeptons.sources import sources
#uncomment line below to run the FourLeptons analysis
#from OutreachExercise2010.FourLeptons.FourLeptonAnalyzer \
#    import FourLeptonAnalyzer
#uncomment line below to run the TwoLeptons analysis
from OutreachExercise2010.FourLeptons.TwoLeptonAnalyzer \
    import TwoLeptonAnalyzer

#uncomment line below to run the FourLeptons analysis
#analyzer = FourLeptonAnalyzer()
#uncomment line below to run the TwoLeptons analysis
analyzer = TwoLeptonAnalyzer()

analyzer.declareHistos()

for sample in sources:
    analyzer.processSample(sample, 1000000000)

analyzer.exportData()
