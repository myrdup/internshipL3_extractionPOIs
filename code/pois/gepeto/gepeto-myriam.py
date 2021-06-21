import csv
import sys
import time
import pandas as pd
import math
from math import sin, cos, sqrt, atan2, radians

inputFile=sys.argv[1]
outputFile=sys.argv[2]
duration=int(sys.argv[3])*60000 #input in minutes, eventually in ms
diameter=float(sys.argv[4])#input diameter in meters
radius = diameter/2
tolerance=float(sys.argv[5]) #input tolerance in [0,1] = maximum ratio of points outside the maximal diameter in a cluster
dist=float(sys.argv[6])
user=int(sys.argv[7])


def centroid (cluster, size):
	sumlat=0
	sumlon=0
	for i in range (size):
		sumlat+=cluster[i][0]
		sumlon+=cluster[i][1]
	return sumlat/size, sumlon/size

def distance_points(c1, c2):
	lat1, lon1=c1[0], c1[1]
	lat2, lon2=c2[0], c2[1]
	return distance(lat1,lon1,lat2,lon2)

def distance_clusters(c1, c2):
	lat1, lon1=c1[1], c1[2]
	lat2, lon2=c2[1], c2[2]
	return distance(lat1,lon1,lat2,lon2)

deg_to_m_lat= 78850
deg_to_m_lgt = 111110
'''def distance (lati, lgti, latj, lgtj):
	return sqrt((((lgti-lgtj)*deg_to_m_lat)**2) + (((lati-latj)*deg_to_m_lgt)**2))'''
	
R = 6373.0 # approximate radius of earth in km
def distance(lat1,lon1,lat2,lon2):
	lat1=radians(lat1)
	lon1=radians(lon1)
	lat2=radians(lat2)
	lon2=radians(lon2)
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))
	distance = R * c
	return distance*1000  #return value in meter

def merge(c1, c2):
	[user1, lat1, lon1, size1, timein1, timeout1] = c1
	[user2, lat2, lon2, size2, timein2, timeout2] = c2
	size= size1 + size2
	return [user1, (lat1*size1 + lat2*size2)/size, (lon1*size1 + lon2*size2)/size, size, min(timein1, timein2), max(timeout1, timeout2)]

df_current=pd.read_csv(inputFile,names=['lat','lon','timestamp'])
max_index= df_current.shape[0]

cumulTime=0
cluster=[]
listclusters=[]
size=0
nextrow=df_current.iloc[[0]]
nextlat=nextrow['lat'].values[0]
nextlon=nextrow['lon'].values[0]
nexttimestamp=nextrow['timestamp'].values[0]

#1.creating clusters according to constraints
for i in range(max_index-1):
	lat=nextlat
	lon=nextlon
	timestamp=nexttimestamp
	
	nextrow=df_current.iloc[[i+1]]
	nextlat=nextrow['lat'].values[0]
	nextlon=nextrow['lon'].values[0]
	nexttimestamp=nextrow['timestamp'].values[0]
	
	cumulTime = cumulTime + nexttimestamp - timestamp
	if cumulTime <= duration : 
		cluster.append([lat,lon,timestamp])
		size+=1
	elif size>0 :#case of time jump
		if size != len(cluster) :
			print("au secours!")
		c_centroid = centroid(cluster, size)
		nbPtsOutsideRadius=0
		for j in range(size):
			if distance_points(cluster[j], c_centroid) > radius:
				nbPtsOutsideRadius+=1
		if nbPtsOutsideRadius/size < tolerance:
			listclusters.append([user, lat, lon, size, cluster[0][2], nexttimestamp]) #user, lat, lon, nbpts, timein, timeout
		cumulTime=0
		cluster=[]
		size=0
	else:
		cumulTime=0
		cluster=[]
		size=0
#2.merging close clusters
nbClusters= len(listclusters)
print("nbclusters=", nbClusters)
with open(outputFile, mode='w') as f:
	writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	i=0
	k=0
	while i < (nbClusters-1) :
		finalcluster=listclusters[i]
		j=i+1
		while j < nbClusters and distance_clusters(finalcluster, listclusters[j]) < dist:
			finalcluster=merge(finalcluster, listclusters[j])
			j+=1
		writer.writerow(finalcluster)
		k+=1
		i=j
print("nb final clusters=", k)
