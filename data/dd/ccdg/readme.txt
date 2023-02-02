# CCDG Data Dictionary for FHIR
The files within this directory represent CSV downloads from the google sheet: https://docs.google.com/spreadsheets/d/1_hN_9hbPSF_gjmkQCvbobOP4G8oPVcJBbvRzMRk8fRA/edit#gid=1507031680

The files were downloaded Feb 02, 2023


## Changes required to make these files work with whistler
There were some issues that resulted in the files being unable to be properly
understood by NCPI Whistler without some changes: 

* dbgap_subject_id appears 2x. One should probably be dbgap_consent_id or something like that, so I've changed it since whistler doesn't like having two identically named variables. 
* dbgap_consent_id - The list of codes were provided via a URL in the enumerations page. I provided those that were static as a list
* Google exports with checkboxes create over 1000 lines even though there are far fewer valid lines. I deleted those empty rows
* The sequencing file has a row above the header which I deleted

## TODO 

### Complex Consent Codes
There were some codes described in the document which included -[XX] which indicates 
some additional info is required to determine the full code. I'm not sure how to 
handle enumerations that aren't actually enumerated...
