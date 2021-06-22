import numpy as np
import time
import os
import fnmatch
import csv
import sys
import pandas as pd
import time

inputDirectory=sys.argv[1] #contains one csv file for each user, with H lines : H is the number of draws of p POIs among the user's set of POIs ; each line contains either 0 or 1, depending on whether the associated user's set of p POIs is unique or not among all users'

# WHAT DOES THIS PROGRAM DO ? for each user in inputDirectory, it counts the number of draws in which the user is considered unique among all users (it reads the csv file and counts the number of zeros)

def count_uniqueness (file, user):
	"""
	input:
	file = csv file with its path from current directory
	user = integer, identifyer of the user whose trace is studied

	output: nothing
	
	side effect : prints the user identifyer next to the number of associated unique draws
	"""
	global nbrDraws
	with open(file, newline='') as f:
		reader = csv.reader(f)
		i=0 
		for row in reader: #user lat lgt timein timeout
			point=list(map(int,row))
			if point[0]==1: #draw in which the user is unique
				i+=1
			nbrDraws+=1
		print(user, i)
		return 0

listUsers=os.listdir(inputDirectory)
nbrDraws=0
for filename in listUsers: #the count is done for every user in the inputDirectory
	if fnmatch.fnmatch(filename, '[!POI]*.csv'): #the inputDirectory also contains another file per user, whose name starts with "POI", and that contains the identifyers of selected POIs for every draw : those files are meaningless here, so we do not consider them
		user = int(filename.split(".")[0]) #the user identifyer is deduced from the csvfile name
		count_uniqueness(inputDirectory+'/'+filename, user)
print('nbrDraws',nbrDraws)
		
