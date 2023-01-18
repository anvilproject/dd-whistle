# dd-whistle
FHIR Ingest Project for Data-Dictionaries to be Loaded Into Public FHIR Demo Server. 

This project contains the projections used to load data-dictionaries into FHIR using [NCPI Whistler](https://github.com/NIH-NCPI/ncpi-whistler). 

Due to a current limitation of the whistler application, the configuration must point to "dataset" files which will be loaded into the data object passed into whistle. The data used at this time is fake data and is provided in the repo for completeness. It will be removed once that requirement has been removed. 

# Datasets
## CMG
The Data-Dictionary entries for CMG were based on tab, Fields and definitions, from the [google doc](https://docs.google.com/spreadsheets/d/1rBABWeyplNtYSOwIKVwx_fudcyUZNb-MymdkefYYbxU/edit#gid=1507031680) with some minor tweaks to make the resulting data-dictionaries comply with the expectations of the Whistler application. The script, scripts/extract-dd.py, was used to generate the base data dictionaries which were later tweaked to accommodate whistler's expectations. 

Tweaks before running extract-dd.py script included:
* Removed "Key Field:" from the first line's Instrument column
* Removed extraneous information in the Instrument column, such as "Tables", "and", etc so that the column contained only comma separated lists of instruments. Whitespace shouldn't be problematic. 
   
Tweaks made after generally involved replacing unknown types: 'boolean', 'enumeration', 'identifier' and 'date' with 'string'. Whistler treats anything with a list of values as enumerations. Dates are not currently supported because auto-generating tabular code with tables containing dates could be problematic due to the wide range of possible formats (and the tendency for some datasets to be inconsistent within the same column due to copy/paste, etc. ).

# Key Directories
## Projector 
This directory contains the whistle code which will be used to transform the data-dictionaries into FHIR resources. Please see the [manual](https://nih-ncpi.github.io/ncpi-whistler/#/?id=whistle-projections) for more information about whistle projections. 

## harmony/cmg
This directory contains the CSV File which is used to build the FHIR ConceptMap used by whistle to perform terminological transformations. Please see the [manual](https://nih-ncpi.github.io/ncpi-whistler/#/?id=harmony-files) for more information about harmony files. For the purposes of the data-dictionaries, there isn't a lot here, though, it might be helpful to provide some deeper codes based on real values found for certain fields like HP and UBERON, etc. 

## data/cmg
This directory contains some fake data to satisfy the whistler application's expectation of valid datasets being provided in the configuration. 

## data/cmg/dd
This contains the final data-dictionary files extracted (with slight modifications described above) from the original data-dictionary google sheet. 

# Key Files
## cmg-dd.yaml 
This is the whistler configuration file which tells the application what tables to look for, etc. 

## _cmg.wstl
This is the CMG whistle entry point that basically kicks of the whistle transformation. It must live outside the projector library due to the way whistle works. 

