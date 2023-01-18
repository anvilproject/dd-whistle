# dd-whistle
FHIR Ingest Project for Data-Dictionaries to be Loaded Into Public FHIR Demo Server. 

This project contains the projections used to load data-dictionaries into FHIR using [NCPI Whistler](https://github.com/NIH-NCPI/ncpi-whistler). 

Due to a current limitation of the whistler application, the configuration must point to "dataset" files which will be loaded into the data object passed into whistle. The data used at this time is fake data and is provided in the repo for completeness. It will be removed once that requirement has been removed. 

The Data-Dictionary entries for CMG were based on tab, Fields and definitions, from the [google doc](https://docs.google.com/spreadsheets/d/1rBABWeyplNtYSOwIKVwx_fudcyUZNb-MymdkefYYbxU/edit#gid=1507031680) with some minor tweaks to make the resulting data-dictionaries comply with the expectations of the Whistler application. The script, scripts/extract-dd.py, was used to generate the base data dictionaries which were later tweaked to accommodate whistler's expectations. 

