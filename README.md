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

You must specify in your run.py code which analysis you wants to run; 

also, you must specify in python/Analyzer.py if you want to look the massZ o massZZ:

```
 #uncomment line below to run the FourLeptons analysis
 #self.data.append(box.ZZ.mass())
 #uncomment line below to run the TwoLeptons analysis
 self.data.append(box.Z.mass())
```

You also need to give the path to the pattuples you use in the python/sources.py file.
 
Then, go to the run dir area:

```
$run> ipython run.py
```

Then, you can plot the histrograms defined in your analyzers within the interactive python session. 
For example:

```
$> analyzer.malePlot("massZ")
$> analyzer.makePlot("massFull1")
```

Events selection can be modified in the FourLeptons and TwoLeptons codes.
The number of events to be analyzed can be modified in the function processSample within the Analyzer.py code.


