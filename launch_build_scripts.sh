#!/bin/bash

qsub build_scripts/$1/kraken_build_standard_db_1999_2010.sh

qsub build_scripts/$1/kraken_build_standard_db_2011_2014.sh

qsub build_scripts/$1/kraken_build_standard_db_2015.sh

qsub build_scripts/$1/kraken_build_standard_db_2016.sh

qsub build_scripts/$1/kraken_build_standard_db_2017.sh

qsub build_scripts/$1/kraken_build_standard_db_2018.sh

qsub build_scripts/$1/kraken_build_standard_db_2019.sh