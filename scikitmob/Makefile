#parameters
DURATION=15#in minutes
DIAMETER=200#in meters
USER=24
DATA_IN_DIR= /home/mdupraz/Documents/L3_stage/mobility-datasets/privamov-tree-30days/
DATA_OUT_DIR= /home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/scikitmob/results/
SKMOB_DIR=/home/mdupraz/Documents/L3_stage/code_clustering/scikitmob/

#other macros
DATA_OUT_SPEC_DIR = $(DATA_OUT_DIR)dur$(DURATION)_diam$(DIAMETER)/
CSVFILES_IN=$(wildcard $(DATA_IN_DIR)*.csv)
CSVFILES_OUT=$(CSVFILES_IN:$(DATA_IN_DIR)%.csv=$(DATA_OUT_SPEC_DIR)%.csv)

#compute POIs of all users
all : $(CSVFILES_OUT)

$(DATA_OUT_SPEC_DIR)%.csv : $(DATA_OUT_SPEC_DIR)
	python3 csvPOI_from_csvTrace.py '$(DATA_IN_DIR)$(*F).csv' '$(DATA_OUT_SPEC_DIR)$(*F).csv'  $(DURATION) $(DIAMETER) $(*F)

$(DATA_OUT_SPEC_DIR):
	mkdir $(DATA_OUT_DIR)dur$(DURATION)_diam$(DIAMETER)


#compute POIs of a specific user :
oneuser : $(DATA_OUT_SPEC_DIR)
	python3 csvPOI_from_csvTrace.py '$(DATA_IN_DIR)$(USER).csv' '$(DATA_OUT_SPEC_DIR)$(USER).csv' $(DURATION) $(DIAMETER) $(USER)



#installation of skmob (to remember, does not work with make)
install :
	python3 -m venv skmob
	source skmob/bin/activate
	pip install scikit-mobility
	source activate skmob

#activation of skmob after installing (to remember, does not work with make)
activate :
	source $(SKMOB_DIR)skmob/bin/activate
