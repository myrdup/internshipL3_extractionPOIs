# internshipL3_extractionPOIs

## Table of contents
+ [Tree structure](#Tree%20structure)
+ [Content](#Content)
  + [Scikitmob](#SCIKITMOB)
  + [Primault](#PRIMAULT)
+ [References](#References)


## Tree structure
* *file* README.md
* *directory* SCIKITMOB
  * *file* cvsPOI_from_cvsTrace.py
  * *file* Makefile
* *directory* PRIMAULT
  * *file* Makefile

## Content
Each folder corresponds to a method to extract POIs from a mobility trace.  

### SCIKITMOB
SCIKITMOB uses the tool detailed in [scikitmob_2019](#scikitmob_2019) and [scikitmob_github](#scikitmob_github) based on the DT-clustering method explained in [toyama_2004](#toyama2004).  

**prerequisites**  
Before to use SCIKITMOB, the environnement must be installed with following commands :   
`python3 -m venv skmob`  
`source skmob/bin/activate`  
`pip install scikit-mobility`  
`source activate skmob`  

**in and out files**  
Input mobility traces are cvs files under the shape "latitude | longitude | timestamp (ms)" with name "x.cvs" where x is an integer.  
Output POIs lists (one list per trace) are cvs files under the shape "user | latitude | longitude | timestamp in (s)| timestamp out (s)".  

**commands make**  
The makefile admits the following parameters : DURATION (in minutes), DIAMETER (in meters), DATA_IN_DIR, DATA_OUT_DIR (directory paths) and additionnally USER (integer) used in case of command `make oneuser`.  
The syntax is the following : (here for command `make`, supposing that other parameters are default) :  `make DURATION=15 DIAMETER=200`  
The command `make` extracts POIs of all mobility traces (cvs files) located in `[DATA_IN_DIR]`, and stores them in directory named `dur[DURATION]_diam[DIAMETER]`, created (if necessary) in `[DATA_OUT_DIR]`.  
To run the extraction for a single cvs file, we use command `make oneuser`. The cvs file we are interested in is specified with parameter `USER=x`, where x is the integer file name without the extension .cvs (if file is 4.cvs then USER is 4).  

### PRIMAULT
PRIMAULT uses the tool detailed in [accio_2015](https://discovery.ucl.ac.uk/id/eprint/10047858/1/Primault_paper.pdf) also based on DT- and DJ-clustering [zhou_2004](https://www.researchgate.net/profile/Dan-Frankowski-2/publication/221589563_Discovering_personal_gazetteers_An_interactive_clustering_approach/links/562a314108ae518e347f1054/Discovering-personal-gazetteers-An-interactive-clustering-approach.pdf).  

**prerequisites**
To run the extraction of POIs with PRIMAULT, we need the folder `accio.jar`and file `poi-attack.json`.  

**in and out files**
Input mobility traces are cvs files under the shape "latitude | longitude | timestamp (ms)" with name "x.cvs" where x is an integer.  
Output POIs lists (one list per trace) are cvs files under the shape "user | latitude | longitude | number of points in POI | timestamp in (ms)| timestamp out (ms) | effective diameter (m)".  

**commands make**  
The makefile admits the following parameters : DURATION (in minutes), DIAMETER (in meters), DATA_IN_DIR, DATA_OUT_DIR (directory paths), SRC (file path to accio.jar), JSON (file path to poi-attack.json).  
The syntax is the following : (here for command `make`, supposing that other parameters are default) :  `make DURATION=15 DIAMETER=200`  
The command `make` extracts POIs of all mobility traces (cvs files) located in `[DATA_IN_DIR]`, and stores them in directory `[DATA_OUT_DIR]/dur[DURATION]_diam[DIAMETER]/data/someComplicatedName/testPOI/`.  

## References

<a id="scikitmob_2019">[scikitmob_2019]</a> https://arxiv.org/pdf/1907.07062.pdf
<a id="scikitmob_github">[scikitmob_github]</a> https://github.com/scikit-mobility/scikit-mobility/blob/master/README.md#tutorials
<a id="toyama_2004">[scikitmob_github]</a> http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.422.3690&rep=rep1&type=pdf

