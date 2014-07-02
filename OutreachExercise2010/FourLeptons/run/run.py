#
# XXX
#
import ROOT
ROOT.gROOT.ProcessLine(".x tdrstyle.C")


from OutreachExercise2010.FourLeptons.sources import sources
from OutreachExercise2010.FourLeptons.FourLeptonAnalyzer \
    import FourLeptonAnalyzer

analyzer = FourLeptonAnalyzer()

analyzer.declareHistos()

for sample in sources:
    analyzer.processSample(sample, 5000)

analyzer.exportData()
