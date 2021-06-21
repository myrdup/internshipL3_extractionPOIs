import numpy as np
import time

import csv
import sys
import pandas as pd
import time

inputFile=sys.argv[1]
user=sys.argv[2]


def count_csv (file, user):
	"""
	input:
	file = csv file with its path from current directory
	user = integer, identifyer of the user whose trace is studied

	output:
	len(file) = nbr POIs
	"""
	with open(file, newline='') as f:
		reader = csv.reader(f)
		#tracemob=[]
		i=0
		for row in reader: #user lat lgt timein timeout
			#point=list(map(float,row))
			#point.insert(5,point[4]-point[3]) #delta-time
			#tracemob.append(point)
			#print(tracemob[i])
			i+=1
		print(i)
		return 0
		
count_csv(inputFile,user)

