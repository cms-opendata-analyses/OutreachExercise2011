# CMS Outreach Exercise 2010

Some intro text here. This repo contains two examples:

a) the TwoLeptons analysis: Z ->  ll

b) the FourLeptons analysis: ZZ -> llll

Both running on 2010 data, but not directly.

The exercise runs over pattuples created from the 2010 AOD data.

The lepton selection is preliminary.

## Creating the Working Area

```
cmsrel CMSSW_4_2_8
cd CMSSW_4_2_8/src
git init
git remote add origin https://github.com/ayrodrig/OutreachExercise2010.git 
git fetch origin
git checkout master
scram b 
cmsenv
```

## Running the Exercise


Go to the run dir area:

```
$run> ipython run.py
```

You must specify in your run.py code which analysis you wants to run; 

also, you must specify in python/Analyzer.py if you want to look the massZ o massZZ:

```
 #uncomment line below to run the FourLeptons analysis
 #self.data.append(box.ZZ.mass())
 #uncomment line below to run the TwoLeptons analysis
 self.data.append(box.Z.mass())
```
 



