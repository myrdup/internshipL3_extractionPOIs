#parameters
DURATION=15#in minutes
DIAMETER=200#in meters
TOLERANCE=0.1#ratio
DIST=60#to merge pois, in meters

DATA_IN_DIR= /home/mdupraz/Documents/L3_stage/mobility-datasets/privamov-tree-30days/
DATA_OUT_DIR= /home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/data/pois/gepeto/
SRC=/home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/code/pois/gepeto/gepeto-myriam.py
USER=1

#other macros
DATA_OUT_SPEC_DIR = $(DATA_OUT_DIR)dur$(DURATION)_diam$(DIAMETER)_tol$(TOLERANCE)_dist$(DIST)/
CSVFILES_IN=$(wildcard $(DATA_IN_DIR)*.csv)
CSVFILES_OUT=$(CSVFILES_IN:$(DATA_IN_DIR)%.csv=$(DATA_OUT_SPEC_DIR)%.csv)


#compute POIs of all users
all : $(DATA_OUT_SPEC_DIR)
	python3 $(SRC) $(DATA_IN_DIR)$(USER).csv $(DATA_OUT_SPEC_DIR)$(USER)-rad.csv $(DURATION) $(DIAMETER) $(TOLERANCE) $(DIST) $(USER)

$(DATA_OUT_SPEC_DIR):
	mkdir $(DATA_OUT_DIR)dur$(DURATION)_diam$(DIAMETER)_tol$(TOLERANCE)_dist$(DIST)
