## This file is part of CMSOutreachExercise2011 derived from CMSOutreachExercise2010.
## Copyright (C) 2014 Instituto de Fisica de Cantabria and CERN.
## Based on the code of the CMSData Analysis School 2014 Long Exercise: 
## Search for the Higgs in ZZ -> 4 leptons decay channel (available 
## at https://github.com/bachtis/CMSDAS)

## CMSOutreachExercise2011 is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## CMSOutreachExercise2011 is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with CMSOutreachExercise2011. If not, see <http://www.gnu.org/licenses/>.

from OutreachExercise2011.DecaysToLeptons.Sample import Sample

data_files = [
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_01.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_02.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_03.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_04.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_05.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_06.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleElectron/PATtuples/Electron_PAT_data_500files_01.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleElectron/PATtuples/Electron_PAT_data_500files_02.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleElectron/PATtuples/Electron_PAT_data_500files_03.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleElectron/PATtuples/Electron_PAT_data_500files_04.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleElectron/PATtuples/Electron_PAT_data_500files_05.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleElectron/PATtuples/Electron_PAT_data_500files_06.root'
]

data = Sample('data', False, data_files, 1)

sources = [data]
