# CMS Outreach Exercise 2010

Some intro text here. This repo contains two examples:

a) the TwoLeptons analysis: Z ->  ll

b) the FourLeptons analysis: ZZ -> llll

Both running on 2010 data, but not directly.

The exercise runs over pattuples created from the 2010 AOD data. 
More details on the pattuples generation are in the pattuple repository:
https://github.com/ayrodrig/pattuples2010

The lepton selection is preliminary.

## Creating the Working Area

This step is only needed the first time.

```
cmsrel CMSSW_4_2_8
cd CMSSW_4_2_8/src
git init
git remote add origin https://github.com/ayrodrig/OutreachExercise2010.git 
git fetch origin
git checkout master
scram b 
```

## Sourcing the environment 

This step is needed each time you want to run the exercise.

```
cd CMSSW_4_2_8/src
source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsenv
```

## Running the Exercise

To run the code you have to move to the directory:

```
OutreachExercise2010/DecaysToLeptons/run/
```

You must specify in your run.py code from the path above which analysis you want to run:

```python
# Import the Analyzer you want to run:
# FourLeptonAnalyzer or TwoLeptonAnalyzer
# by uncommenting the appropiate line below. 

#from OutreachExercise2010.DecaysToLeptons.FourLeptonAnalyzer import FourLeptonAnalyzer as MyAnalyzer
from OutreachExercise2010.DecaysToLeptons.TwoLeptonAnalyzer import TwoLeptonAnalyzer as MyAnalyzer
``` 

You also need to give the path to the pattuples you use in the file:
```
OutreachExercise2010/DecaysToLeptons/python/sources.py
``` 
 
Then, just run:

```
ipython run.py
```

The number of events to be analyzed can be modified in the run.py file.

```python
for sample in sources:
    # maxEv defines the maximum number of events to analyze
    # set it to -1 to analyze all available events; 
    analyzer.processSample(sample, maxEv=100)
```

At the beginning you will get a message like: 

```python
Processing Files
['root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/PATtuples/Mu_PAT_data_500files_1.root', 'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/PATtuples/Mu_PAT_data_500files_2.root', 'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/PATtuples/Mu_PAT_data_500files_3.root', 'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/PATtuples/Mu_PAT_data_500files_4.root', 'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/PATtuples/Mu_PAT_data_500files_5.root', 'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/PATtuples/Mu_PAT_data_500files_6.root', 'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Electron/PATtuples/Electron_PAT_data_500files_1.root', 'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Electron/PATtuples/Electron_PAT_data_500files_2.root', 'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Electron/PATtuples/Electron_PAT_data_500files_3.root', 'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Electron/PATtuples/Electron_PAT_data_500files_4.root', 'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Electron/PATtuples/Electron_PAT_data_500files_5.root', 'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Electron/PATtuples/Electron_PAT_data_500files_6.root']
1 events processed in 28.4234111309 seconds
100 events processed in 49.6256351471 seconds
[...]
In [1]: 
```

Then, you can plot the histrograms defined in your analyzers within the interactive python session. 
For example, to get the Z mass or the ZZ mass in the full range:

```python
analyzer.makePlot("massZ") 
analyzer.makePlot("massFull1")
```

Events selection can be modified in the FourLeptonsAnalyzer.py and TwoLeptonsAnalyzer.py codes:
```
OutreachExercise2010/DecaysToLeptons/python/FourLeptonAnalyzer.py
OutreachExercise2010/DecaysToLeptons/python/TwoLeptonAnalyzer.py
```

