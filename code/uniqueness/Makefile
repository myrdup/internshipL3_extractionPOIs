#characteristics of POIs
DURATION=15
DIAMETER=200
#characteristics of tolerance
SPATIAL=400#meters
TEMPORAL=2#hours

all : r0

r0 :
	for p in 1 2 3 4 5 ; do \
		python3 /home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/code/uniqueness/uniqueness-POI-gepeto.py /home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/data/pois/gepeto/dur15_diam50_tol0.1_dist13/ 100 2 $$p 100 /home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/data/uniqueness/gepeto/dur15_diam50_tol0.1_dist13_spat100_temp2/$$p ; \
		echo gepeto $$p fini ; \
	done
	echo 15 50 100 2 fini
	for p in 1 2 3 4 5 ; do \
		python3 /home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/code/uniqueness/uniqueness-POI-gepeto.py /home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/data/pois/gepeto/dur15_diam50_tol0.1_dist13/ 400 2 $$p 100 /home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/data/uniqueness/gepeto/dur15_diam50_tol0.1_dist13_spat400_temp2/$$p ; \
		echo gepeto $$p fini ; \
	done
	echo 15 50 400 2 fini
	
	
r1 :
	for p in 1 2 3 4 5 ; do \
		python3 /home/mdupraz/Documents/L3_stage/code-uniqueness/uniqueness-parallel-POI-primault-rad.py /home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/primault/results/dur15_diam50/data/*/testPOI 100 $(TEMPORAL) $$p 100 /home/mdupraz/Documents/L3_stage/code-uniqueness/primault/dur15_diam50_spat100_temp$(TEMPORAL)/$$p ; \
		echo primault $$p fini ; \
		python3 /home/mdupraz/Documents/L3_stage/code-uniqueness/uniqueness-parallel-POI-scikitmob-rad.py /home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/scikitmob/results/dur$(DURATION)_diam50 100 $(TEMPORAL) $$p 100 /home/mdupraz/Documents/L3_stage/code-uniqueness/scikitmob/dur$(DURATION)_diam50_spat100_temp$(TEMPORAL)/$$p ; \
		echo scikitmob $$p fini ; \
	done
	echo r1 fini

r2 :
	for p in 1 2 3 4 5 ; do \
		python3 /home/mdupraz/Documents/L3_stage/code-uniqueness/uniqueness-parallel-POI-primault-rad.py /home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/primault/results/dur15_diam50/data/*/testPOI $(SPATIAL) $(TEMPORAL) $$p 100 /home/mdupraz/Documents/L3_stage/code-uniqueness/primault/dur15_diam50_spat$(SPATIAL)_temp$(TEMPORAL)/$$p ; \
		echo primault $$p fini ; \
		python3 /home/mdupraz/Documents/L3_stage/code-uniqueness/uniqueness-parallel-POI-scikitmob-rad.py /home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/scikitmob/results/dur$(DURATION)_diam50 $(SPATIAL) $(TEMPORAL) $$p 100 /home/mdupraz/Documents/L3_stage/code-uniqueness/scikitmob/dur$(DURATION)_diam50_spat$(SPATIAL)_temp$(TEMPORAL)/$$p ; \
		echo scikitmob $$p fini ; \
	done
	echo r2 fini

r3 :
	for p in 1 2 3 4 5 ; do \
		python3 /home/mdupraz/Documents/L3_stage/code-uniqueness/uniqueness-parallel-POI-primault-rad.py /home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/primault/results/dur$(DURATION)_diam200/data/*/testPOI $(SPATIAL) $(TEMPORAL) $$p 100 /home/mdupraz/Documents/L3_stage/code-uniqueness/primault/dur$(DURATION)_diam200_spat$(SPATIAL)_temp$(TEMPORAL)/$$p ; \
		echo primault $$p fini ; \
		python3 /home/mdupraz/Documents/L3_stage/code-uniqueness/uniqueness-parallel-POI-scikitmob-rad.py /home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/scikitmob/results/dur$(DURATION)_diam200 $(SPATIAL) $(TEMPORAL) $$p 100 /home/mdupraz/Documents/L3_stage/code-uniqueness/scikitmob/dur$(DURATION)_diam200_spat$(SPATIAL)_temp$(TEMPORAL)/$$p ; \
		echo scikitmob $$p fini ; \
	done
	echo r3 fini

r4 : 
	for p in 1 2 3 4 5 ; do \
		python3 /home/mdupraz/Documents/L3_stage/code-uniqueness/uniqueness-parallel-POI-primault-rad.py /home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/primault/results/dur$(DURATION)_diam200/data/*/testPOI $(SPATIAL) 4 $$p 100 /home/mdupraz/Documents/L3_stage/code-uniqueness/primault/dur$(DURATION)_diam200_spat$(SPATIAL)_temp4/$$p ; \
		echo primault $$p fini ; \
		python3 /home/mdupraz/Documents/L3_stage/code-uniqueness/uniqueness-parallel-POI-scikitmob-rad.py /home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/scikitmob/results/dur$(DURATION)_diam200 $(SPATIAL) 4 $$p 100 /home/mdupraz/Documents/L3_stage/code-uniqueness/scikitmob/dur$(DURATION)_diam200_spat$(SPATIAL)_temp4/$$p ; \
		echo scikitmob $$p fini ; \
	done
	echo r4 fini

USER=primault#paramètres à préciser en entrée souvent
NBR=1
count:
	python3 count_uniqueness.py /home/mdupraz/Documents/L3_stage/code-uniqueness/$(USER)/dur$(DURATION)_diam$(DIAMETER)_spat$(SPATIAL)_temp$(TEMPORAL)/$(NBR)


#	python3 [fichier_code] [repertoire_données] [paramètres] [fichier_sortie]
#background :
#	nohup [cmd] &	
