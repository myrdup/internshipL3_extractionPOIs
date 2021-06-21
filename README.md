# internshipL3_extractionPOIs

## Table of contents
+ [Tree structure](#Tree%20structure)
+ [Content](#Content)
  + [Scikitmob](#SCIKITMOB)
  + [Primault](#PRIMAULT)
+ [References](#References)


## Tree structure
* *file* README.md
* *directory* **data**
  * *directory* pois
    * *directories* scikitmob / primault / gepeto / sigdbscan
      * *directories* durX_diamY (X=duration in minutes, Y=diameter in meters)
       * *files* U.csv (U=user, a natural number)
  * *directory* uniqueness
    * *directories* scikitmob / primault / gepeto / sigdbscan
      * *directories* durX_diamY_spatZ_tempK (X=duration in minutes, Y=diameter in meters, Z=spatial resolution in meters, K=temporal resolution in meters)
       * *files* U.csv (U=user, a natural number)

* *directory* **code**
  * *directory* pois
    * *directories* scikitmob / primault / gepeto / sigdbscan
      * *files.py* eventual additional code to eventual prerequisites
      * Makefile
  * *directory* uniqueness
    * *files.py* uniqueness codes adapted to scikitmob / primault / gepeto / sigdbscan
    * Makefile

* *directory* **results**
  * *directory* countPOIs
    * figures, eventual codes and Makefiles
  * *directory* commonPOIs
  * *directory* uniqueness

## Extraction of POIs (./code/pois/ and ./data/pois)
Each folder in those directories corresponds to a method to extract POIs from a mobility trace.  

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
The makefile admits the following parameters : DURATION (in minutes), DIAMETER (in meters), DATA_IN_DIR, DATA_OUT_DIR (directory paths), SKMOB_DIR (path to directory where skmob has been installed), and additionnally USER (integer) used in case of command `make oneuser`.  

Before to run the extraction, we must activate skmob with command `make activate`.  
The command `make` extracts POIs of all mobility traces (cvs files) located in `[DATA_IN_DIR]`, and stores them in directory named `dur[DURATION]_diam[DIAMETER]`, created (if necessary) in `[DATA_OUT_DIR]`. The syntax is the following : (here for command `make`, supposing that other parameters are default) :  `make DURATION=15 DIAMETER=200`  
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

<a id="scikitmob_2019">[scikitmob_2019]</a> Luca Pappalardo, Filippo Simini, Gianni Barlacchi and Roberto Pellungrini. scikit-mobility: a Python library for the analysis, generation and risk assessment of mobility data, 2019. https://arxiv.org/pdf/1907.07062.pdf  
<a id="scikitmob_github">[scikitmob_github]</a> https://github.com/scikit-mobility/scikit-mobility/blob/master/README.md#tutorials  
<a id="toyama_2004">[toyama_2004]</a> HARIHARAN, Ramaswamy et TOYAMA, Kentaro. Project Lachesis: parsing and modeling location histories. In : International Conference on Geographic Information Science. Springer, Berlin, Heidelberg, 2004. p. 106-124. http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.422.3690&rep=rep1&type=pdf  
<a id="accio_2015">[accio_2015]</a> PRIMAULT, Vincent, MAOUCHE, Mohamed, BOUTET, Antoine, et al. ACCIO: How to make location privacy experimentation open and easy. In : 2018 IEEE 38th International Conference on Distributed Computing Systems (ICDCS). IEEE, 2018. p. 896-906. https://discovery.ucl.ac.uk/id/eprint/10047858/1/Primault_paper.pdf  
<a id="zhou_2004">[zhou_2004]</a> ZHOU, Changqing, FRANKOWSKI, Dan, LUDFORD, Pamela, et al. Discovering personal gazetteers: an interactive clustering approach. In : Proceedings of the 12th annual ACM international workshop on Geographic information systems. 2004. p. 266-273. https://www.researchgate.net/profile/Dan-Frankowski-2/publication/221589563_Discovering_personal_gazetteers_An_interactive_clustering_approach/links/562a314108ae518e347f1054/Discovering-personal-gazetteers-An-interactive-clustering-approach.pdf).  

