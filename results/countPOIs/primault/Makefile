#parameters
DATA=/home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/primault/results/dur15_diam500/data/ac162f07ba885869effda4ce1929b619a2bcfc84-PoisReidentKSet/testPOI/
FILE_OUT_POIS=/home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/results/countPOIs/count.txt
FILE_OUT_USERS=/home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/results/countPOIs/users.txt
DIR_CODE=/home/mdupraz/Documents/L3_stage/internshipL3_extractionPOIs/results/countPOIs/


all: 
	for number in 1 2 7 9 13 17 18 24 26 27 29 30 32 35 36 39 41 42 44 48 49 50 51 52 54 57 59 62 63 65 66 67 68 69 70 71 72 73 75 77 78 80 81 83 84 85 87 90 ; do \
		python3 $(DIR_CODE)count_pois.py $(patsubst %,$(DATA)%.csv,$$number) $$number >> $(FILE_OUT_POIS) ; \
		#python3 $(DIR_CODE)names_users.py $$number >> $(FILE_OUT_USERS) ; \
	done



