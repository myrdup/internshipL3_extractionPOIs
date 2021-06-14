#parameters
DURATION=15#in minutes
DIAMETER=200#in meters
DATA_IN_DIR= /home/mdupraz/Documents/L3_stage/mobility-datasets/privamov-tree-30days/
DATA_OUT_DIR= /home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/scikitmob/results/
SRC=/home/mdupraz/Documents/L3_stage/code_clustering/primault/accio.jar
JSON=/home/mdupraz/Documents/L3_stage/code_clustering/primault/poi-attack.json

#other macros
DATA_OUT_SPEC_DIR = $(DATA_OUT_DIR)dur$(DURATION)_diam$(DIAMETER)/
CSVFILES_IN=$(wildcard $(DATA_IN_DIR)*.csv)
CSVFILES_OUT=$(CSVFILES_IN:$(DATA_IN_DIR)%.csv=$(DATA_OUT_SPEC_DIR)%.csv)


#compute POIs of all users
all : $(DATA_OUT_SPEC_DIR)
	java -jar $(SRC) run -workdir $(DATA_OUT_SPEC_DIR) -params "urltrain=$(DATA_IN_DIR) urltest=$(DATA_IN_DIR) diameter=$(DIAMETER).meters duration=$(DURATION).minutes" $(JSON) >> $(DATA_OUT_DIR)output_dur$(DURATION)_diam$(DIAMETER).txt

$(DATA_OUT_SPEC_DIR):
	mkdir $(DATA_OUT_DIR)dur$(DURATION)_diam$(DIAMETER)

