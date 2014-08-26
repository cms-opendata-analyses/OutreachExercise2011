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
