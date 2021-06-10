# internshipL3_extractionPOIs

## Tree structure
* *file* README.md
* *directory* SCIKITMOB
  * *file* Makefile
* *directory* PRIMAULT
  * *file* Makefile

## Content
Each folder corresponds to a method to extract POIs from a mobility trace.  

### SCIKITMOB
SCIKITMOB uses the tool detailed in [scikitmob_2019](https://arxiv.org/pdf/1907.07062.pdf) and [scikitmob_github](https://github.com/scikit-mobility/scikit-mobility/blob/master/README.md#tutorials) based on the DT-clustering method explained in [toyama_2004](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.422.3690&rep=rep1&type=pdf).  

**prerequisites**  
Before to use SCIKITMOB, the environnement must be installed with following commands :   
`python3 -m venv skmob`  
`source skmob/bin/activate`  
`pip install scikit-mobility`  
`source activate skmob`  

**in and out files**  
Input mobility traces are cvs files under the shape "latitude | longitude | timestamp in ms" with name "x.cvs" where x is an integer.  
Output POIs lists (one list per trace) are cvs files under the shape "user | latitude | longitude | timestamp in | timestamp out".  

**commands make**  
The makefile has 5 parameters : DURATION, DIAMETER, DATA_IN_DIR, DATA_OUT_DIR and additionnally USER used in case of command `make oneuser`.  
The syntax is the following : (here for command `make`, supposing that other parameters are default) :  `make DURATION=15 DIAMETER=200`  
The command `make` extracts POIs of all mobility traces (cvs files) located in `[DATA_IN_DIR]`, and stores them in directory named `dur[DURATION]_diam[DIAMETER]`, created (if necessary) in `[DATA_OUT_DIR]`.  
To run the extraction for a single cvs file, we use command `make oneuser`. The cvs file we are interested in is specified with parameter `USER=x`, where x is the integer file name without the extension .cvs (if file is 4.cvs then USER is 4).  

### PRIMAULT
PRIMAULT uses the tool detailed in [accio_2015](https://discovery.ucl.ac.uk/id/eprint/10047858/1/Primault_paper.pdf) also based on DT- and DJ-clustering [zhou_2004](https://www.researchgate.net/profile/Dan-Frankowski-2/publication/221589563_Discovering_personal_gazetteers_An_interactive_clustering_approach/links/562a314108ae518e347f1054/Discovering-personal-gazetteers-An-interactive-clustering-approach.pdf).  


