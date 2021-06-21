import numpy as np
import time

import csv
import sys
import skmob
import pandas as pd
import time

traceP=sys.argv[1]
traceS=sys.argv[2]
user=int(sys.argv[3])
duration=int(sys.argv[4])
diameter=int(sys.argv[5])
coef_duration=float(sys.argv[6])
coef_distance=float(sys.argv[7])

deg_to_m_lat= 78850
deg_to_m_lgt = 111110
distance_threshold = (diameter*coef_distance)**2
duration_threshold = duration*coef_duration*60000 #from minutes to ms

def assoc (traceP, traceS, user, diameter, coef):
	"""
	input:
	traceP = csv file with its path from current directory obtained with Primault extraction
	traceS = csv file with its path from current directory obtained with Scikitmobility extraction
	user = integer, identifyer of the user whose trace is studied
	duration=int(sys.argv[4])
	diameter=int(sys.argv[5])
	coef_duration=float (0.5 for example) such that common duration > duration_threshold x duration
	coef_distance=float (0.25 for example) such that distance between centroids < distance_threshold x diameter


	output:
	lis = list of pairs of corresponding POIs
	"""
	with open(traceP, newline='') as p:
		rp = list(csv.reader(p))
		with open(traceS, newline='') as s:
			rs = list(csv.reader(s))
			i=0
			j=0
			k=0
			pairs=[]
			#print(len(rp), len(rp[1]), len(rs), len(rs[1]))
			while i < len(rp) and  j  < len(rs):
				bi = int(rp[i][4]) #time in of i
				bj = int(float(rs[j][3])) #time out of i
				ei = int(rp[i][5]) # time in of j
				ej = int(float(rs[j][4])) # time out of j
				if bi < bj and  bj < ei or bj < bi and bi < ej : #if begin(i) < begin(j) < end(i) or begin(j) < begin(i) < end(j) : we only consider POIs which intersect each other
					common_duration=0
					if bi < bj :
						common_duration= min(bj,ei) - bi
					else:
						common_duration= min(bi,ej) - bj
					if common_duration > duration_threshold : #restriction on time in common
						lgti=float(rp[i][2])
						lgtj=float(rs[j][2])
						lati=float(rp[i][1])
						latj=float(rs[j][1])
						squared_distance =(((lgti-lgtj)*deg_to_m_lat)**2) + (((lati-latj)*deg_to_m_lgt)**2)
						if squared_distance < distance_threshold : #restriction on distance between centroids
							pairs.append([i,j])
							#print(user, i,j, common_duration/60000, np.sqrt(squared_distance))
							i+=1
							j+=1
						else:
							if k==0 : 
								i+=1
								k=1
							else : 
								j+=1
								k=0
					else:
						if k==0 :
							i+=1
							k=1
						else : 
							j+=1
							k=0
				elif ei < bj : #i se termine avant que j ne commence
					i+=1
				else :
					j+=1
	print(coef_duration, coef_distance, user, len(pairs))

#print(duration_threshold/60000, np.sqrt(distance_threshold))	
assoc(traceP,traceS,user,duration, diameter)

