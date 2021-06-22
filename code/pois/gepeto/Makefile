#parameters
DURATION=15#in minutes
DIAMETER=500#in meters
TOLERANCE=0.1#ratio
DIST=125#to merge pois, in meters

DATA_IN_DIR= /home/mdupraz/Documents/L3_stage/mobility-datasets/privamov-tree-30days/
DATA_OUT_DIR= /home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/data/pois/gepeto/
SRC=/home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/code/pois/gepeto/gepeto-myriam.py
#USER=1

#other macros
DATA_OUT_SPEC_DIR = $(DATA_OUT_DIR)dur$(DURATION)_diam$(DIAMETER)_tol$(TOLERANCE)
CSVFILES_IN=$(wildcard $(DATA_IN_DIR)*.csv)
CSVFILES_OUT=$(CSVFILES_IN:$(DATA_IN_DIR)%.csv=$(DATA_OUT_SPEC_DIR)%.csv)


#compute POIs of all users
all :
	for distance in 125 ; do \
		mkdir $(DATA_OUT_DIR)dur$(DURATION)_diam$(DIAMETER)_tol$(TOLERANCE)_dist$$distance ; \
		for user in 1 2 7 9 13 17 18 24 26 27 29 30 32 35 36 39 41 42 44 48 49 50 51 52 54 57 59 62 63 65 66 67 68 69 70 71 72 73 75 77 78 80 81 83 84 85 87 90 ; do \
			python3 $(SRC) $(DATA_IN_DIR)$$user.csv $(DATA_OUT_SPEC_DIR)_dist$$distance/$$user.csv $(DURATION) $(DIAMETER) $(TOLERANCE) $$distance $$user ; \
		done ; \
	done


$(DATA_OUT_DIR)*:
	mkdir $@
