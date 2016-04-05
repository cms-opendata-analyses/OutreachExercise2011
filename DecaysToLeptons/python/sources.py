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
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_07.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_08.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_09.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_10.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_11.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_12.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_13.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_14.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_15.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_16.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_17.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_18.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_19.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_20.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_21.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_22.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_23.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_24.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_25.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_26.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_27.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_28.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_29.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_30.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_31.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_32.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_33.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_34.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_35.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_36.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_37.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_38.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_39.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_40.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_41.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_42.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_43.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_44.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_45.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_46.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_47.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_48.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_49.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_50.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_51.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_52.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleMu/PATtuples/Mu_PAT_data_500files_53.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleElectron/PATtuples/Electron_PAT_data_500files_01.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleElectron/PATtuples/Electron_PAT_data_500files_02.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleElectron/PATtuples/Electron_PAT_data_500files_03.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleElectron/PATtuples/Electron_PAT_data_500files_04.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleElectron/PATtuples/Electron_PAT_data_500files_05.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/DoubleElectron/PATtuples/Electron_PAT_data_500files_06.root'
]

data = Sample('data', False, data_files, 1)

sources = [data]
