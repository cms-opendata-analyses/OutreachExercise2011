#
# Copyright (c) 2014 A.Y. Rodriguez-Marrero and E. Fernandez-del-Castillo
# Based on the code of the CMSData Analysis School 2014 Long Exercise: 
# Search for the Higgs in ZZ -> 4 leptons decay channel (available 
# at https://github.com/bachtis/CMSDAS)
#

class Sample(object):
    def __init__(self, type, isMC, files, crossSection):
        self.type = type
        self.files = files
        self.isMC = isMC
        self.crossSection = crossSection
