#
# Copyright (c) 2014 A.Y. Rodriguez-Marrero and E. Fernandez-del-Castillo
# Based on the code of the CMSData Analysis School 2014 Long Exercise: 
# Search for the Higgs in ZZ -> 4 leptons decay channel (available 
# at https://github.com/bachtis/CMSDAS)
#

from OutreachExercise2010.DecaysToLeptons.Sample import Sample

data_files = [
    'file:/data2/pattuples2010/Mu/Mu_PAT_data_500files_1.root',
    'file:/data2/pattuples2010/Mu/Mu_PAT_data_500files_2.root',
    'file:/data2/pattuples2010/Mu/Mu_PAT_data_500files_3.root',
    'file:/data2/pattuples2010/Electron/Electron_PAT_data_500files_1.root',
    'file:/data2/pattuples2010/Electron/Electron_PAT_data_500files_2.root',
    'file:/data/pattuples2010/Electron/Electron_PAT_data_500files_3.root',
    'file:/data3/pattuples2010/Mu/Mu_PAT_data_500files_4.root',
    'file:/data3/pattuples2010/Mu/Mu_PAT_data_500files_5.root',
    'file:/data3/pattuples2010/Mu/Mu_PAT_data_500files_6.root',
    'file:/data/pattuples2010/Electron/Electron_PAT_data_500files_4.root',
    'file:/data/pattuples2010/Electron/Electron_PAT_data_500files_5.root',
    'file:/data/pattuples2010/Electron/Electron_PAT_data_500files_6.root',
]

data = Sample('data', False, data_files, 1)

sources = [data]
