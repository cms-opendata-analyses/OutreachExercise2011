## This file is part of CMSOutreachExercise2010.
## Copyright (C) 2014 Instituto de Fisica de Cantabria and CERN.
## Based on the code of the CMSData Analysis School 2014 Long Exercise: 
## Search for the Higgs in ZZ -> 4 leptons decay channel (available 
## at https://github.com/bachtis/CMSDAS)

## CMSOutreachExercise2010 is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## CMSOutreachExercise2010 is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with CMSOutreachExercise2010. If not, see <http://www.gnu.org/licenses/>.

from OutreachExercise2010.DecaysToLeptons.Sample import Sample

data_files = [
        'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/PATtuples/Mu_PAT_data_500files_1.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/PATtuples/Mu_PAT_data_500files_2.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/PATtuples/Mu_PAT_data_500files_3.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/PATtuples/Mu_PAT_data_500files_4.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/PATtuples/Mu_PAT_data_500files_5.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/PATtuples/Mu_PAT_data_500files_6.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Electron/PATtuples/Electron_PAT_data_500files_1.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Electron/PATtuples/Electron_PAT_data_500files_2.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Electron/PATtuples/Electron_PAT_data_500files_3.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Electron/PATtuples/Electron_PAT_data_500files_4.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Electron/PATtuples/Electron_PAT_data_500files_5.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Electron/PATtuples/Electron_PAT_data_500files_6.root'
]

data = Sample('data', False, data_files, 1)

sources = [data]
