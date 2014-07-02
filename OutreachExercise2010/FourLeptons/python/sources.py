from OutreachExercise2010.FourLeptons.Sample import Sample

data_files = [
    'file:/data/pattuples2010/simple_PAT_data.root',
]

data = Sample('data', False, data_files, 1)

sources = [data]
