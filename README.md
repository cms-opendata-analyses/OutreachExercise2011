# CMS Outreach Exercise 2010

Some intro text here. This repo contains two examples:

a) the TwoLeptons analysis: Z ->  ll

b) the FourLeptons analysis: ZZ -> llll

Both examples exercises running on 2010 data, but not directly in the AOD format.

The exercise runs over tuples created following the Physics Analysis Toolkit (pattuples) from the 2010 AOD data. 
More details on the pattuples generation are in the pattuple repository:
https://github.com/ayrodrig/pattuples2010

From now on it is assumed that you will work on a VM properly contextualized for CMS.

## Creating the Working Area

This step is only needed the first time.

```
source /cvmfs/cms.cern.ch/cmsset_default.sh
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
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd CMSSW_4_2_8/src
cmsenv
```

## Running the Exercise

The path to the pattuples is giving in the file:
```
OutreachExercise2010/DecaysToLeptons/python/sources.py
``` 

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

The number of events to be analyzed can be modified in the run.py file.

```python
for sample in sources:
    # maxEv defines the maximum number of events to analyze
    # set it to -1 to analyze all available events; 
    analyzer.processSample(sample, maxEv=100)
```

To get enough events in the plots, you would need to run over all available samples. That takes time.
If you just want to see whether you can get this running, run over at least 100000 events to get some entries in the plot for the two lepton example, and more for the four lepton example.

Then, just run your analysis in a interactive mode:

```
ipython run.py 
```

or in a non-interactive mode:

```
python run.py 
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

By default all the histrograms defined in your analyzer will be plotted and saved in pdf format (with the name of the histogram). In the interactive mode, you can also plot them typing (depending on the analysis your are running):

```python
analyzer.makePlot("massZ") 
```
or
```
analyzer.makePlot("massZZ")
```

You can exit the ipython session by typing exit() or ctrl+d.

Events selection can be modified in the FourLeptonAnalyzer.py and TwoLeptonAnalyzer.py codes:
```
OutreachExercise2010/DecaysToLeptons/python/FourLeptonAnalyzer.py
OutreachExercise2010/DecaysToLeptons/python/TwoLeptonAnalyzer.py
```

