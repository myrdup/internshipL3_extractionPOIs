#characteristics of POIs
DURATION=15
DIAMETER=50
#characteristics of tolerance
SPATIAL=400#meters
TEMPORAL=2#hours
#characteristics of gepeto to merge
DISTANCE=13
TOLERANCE=0.1

USER=primault#paramètres à préciser en entrée souvent
NBR=5#p = number of selected POIs in the draw for the computation of uniqueness
all : 
	python3 count_uniqueness.py /home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/data/uniqueness/$(USER)/dur$(DURATION)_diam$(DIAMETER)_spat$(SPATIAL)_temp$(TEMPORAL)/$(NBR)

gepeto :
	python3 count_uniqueness.py /home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/data/uniqueness/gepeto/dur$(DURATION)_diam$(DIAMETER)_tol$(TOLERANCE)_dist$(DISTANCE)_spat$(SPATIAL)_temp$(TEMPORAL)/$(NBR)
