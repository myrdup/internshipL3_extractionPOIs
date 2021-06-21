import csv
import sys
import skmob
import pandas as pd
import time
from skmob.preprocessing import filtering
from skmob.preprocessing import detection, clustering
from skmob.preprocessing import compression

inputFile=sys.argv[1]
outputFile=sys.argv[2]
duration=int(sys.argv[3]) #in minutes
radius=float(sys.argv[4])/2000.0 #input diameter in meters, radius eventually in kilometers
inputUser=sys.argv[5]

defaultUser=24
defaultInputFile = '/home/mdupraz/Documents/L3_stage/mobility-datasets/privamov-tree-30days/24.csv'
defaultOutputFile = '/home/mdupraz/Documents/L3_stage/code_clustering/scikitmob/results/o24.csv'

def list_from_csv (file, user):
	"""
	input:
	file = csv file with its path from current directory
	user = integer, identifyer of the user whose trace is studied

	output:
	tracemob = (int*float*float*float) list list, containing : [user, latitude, longitude, timestamp] for every point in file
	i = number of entries in list
	"""
	with open(file, newline='') as f:
		reader = csv.reader(f)
		tracemob=[]
		i=0
		for row in reader:
			point=list(map(float,row))
			point.insert(0,user)
			point[3]=pd.to_datetime(point[3], unit='ms')
			tracemob.append(point)
			#print(tracemob[i])
			i+=1
		return tracemob, i

def csv_from_tdf (csvFile, stdf, user):
	"""
	input:
	cvsFile = cvs file where we want to store stdf's content
	stdf = TrajDataFrame object containing information about stops, columns are labelled :'0', 'lat', 'lng', 'datetime', 'leaving_datetime'
	user = identifyer of the user
	
	output: nothing
	
	side effect :
	cvsFile's columns contain respectively : user, latitude, longitude, time-in, time-out
	"""
	with open(csvFile, mode='w') as f:
		writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		for i in range(0,nbr_stops,1):
			t= stdf.at[i,'datetime']
			lt= stdf.at[i,'leaving_datetime']
			writer.writerow([user, stdf.at[i,'lat'], stdf.at[i,'lng'], 1000*time.mktime(t.timetuple()), 1000*time.mktime(lt.timetuple())])

def tdf_from_list (data_list):
	return skmob.TrajDataFrame(data_list, latitude=1, longitude=2, datetime=3)

# 1) import csv into list
data_list, nbr_pts = list_from_csv(inputFile, inputUser)

# 2) transform list into TrajDataFrame 
tdf = tdf_from_list (data_list)
#print(tdf.head())

			#compression
			#ctdf = compression.compress(tdf, spatial_radius_km=0.2)
			#print('Points of the original trajectory:\t%s'%len(tdf))
			#print('Points of the compressed trajectory:\t%s'%len(ctdf))

# 3) compute the stops for each individual into another TrajDataFrame
stdf = detection.stops(tdf, minutes_for_a_stop=duration, spatial_radius_km=radius, leaving_time=True)
#print(stdf.head())
nbr_stops = len(stdf)
print('Points of the original trajectory:\t%s'%nbr_pts)
print('Points of stops:\t\t\t%s'%nbr_stops)

# 4) export TrajDataFrame into csv
csv_from_tdf(outputFile, stdf, inputUser)









