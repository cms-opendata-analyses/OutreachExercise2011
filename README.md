# CMS Outreach Exercise 2011

This repository contains two examples:

a) the TwoLeptons analysis: Z ->  ll

b) the FourLeptons analysis: ZZ -> llll

Both examples exercises read 2011 data, but not directly in the AOD format.

The exercise runs over derived datasets created following the Physics Analysis Toolkit (pattuples) from the 2011 AOD data. 
More details on the pattuples generation are in the pattuple repository:
https://github.com/katilp/pattuples2011

From now on it is assumed that you will work on a VM properly contextualized for CMS, available from http://opendata.cern.ch/VM/CMS.

## Creating the Working Area

This step is only needed the first time (cmsrel command is needed only if you do not have created your CMSSW_5_3_32 working area earlier).

```
cmsrel CMSSW_5_3_32
cd CMSSW_5_3_32/src
cmsenv
git clone https://github.com/katilp/OutreachExercise2011.git
scram b 
```

## Sourcing the environment 

This step is needed each time you want to run the exercise.

```
cd CMSSW_5_3_32/src
cmsenv
```

## Running the Exercise

The path to the pattuples is giving in the file:
```
OutreachExercise2011/DecaysToLeptons/python/sources.py
``` 

To run the code you have to move to the directory:

```
cd OutreachExercise2011/DecaysToLeptons/run/
```

You must specify in your run.py code from the path above which analysis you want to run:

```python
# Import the Analyzer you want to run:
# FourLeptonAnalyzer or TwoLeptonAnalyzer
# by uncommenting the appropiate line below. 

#from OutreachExercise2011.DecaysToLeptons.FourLeptonAnalyzer import FourLeptonAnalyzer as MyAnalyzer
from OutreachExercise2011.DecaysToLeptons.TwoLeptonAnalyzer import TwoLeptonAnalyzer as MyAnalyzer
``` 

The number of events to be analyzed can be modified in the run.py file.

```python
for sample in sources:
    # maxEv defines the maximum number of events to analyze
    # set it to -1 to analyze all available events; 
    analyzer.processSample(sample, maxEv=100)
```

To get enough events in the plots, you would need to run over more events. That takes time.
Run over at least 100000 events to get a nice plot for the two lepton example, and more for the four lepton example: you get a clear signal with 1000000 events in the plot for the two lepton example. 

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

By default all the histrograms defined in your analyzer will be plotted and saved in png format (with the name of the histogram). In the interactive mode, you can also plot them typing (depending on the analysis your are running):

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
OutreachExercise2011/DecaysToLeptons/python/FourLeptonAnalyzer.py
OutreachExercise2011/DecaysToLeptons/python/TwoLeptonAnalyzer.py
```

