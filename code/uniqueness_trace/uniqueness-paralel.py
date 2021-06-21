import sys
import os
import numpy as np
import math
import itertools
import pandas as pd
import datetime as dt
import ntpath
import shutil
import random
from math import sin, cos, sqrt, atan2, radians
from datetime import datetime,timedelta
import threading
import ntpath
import concurrent.futures
import psutil

#version finale


# For each trace: 
# Do the following  N iterations:
 # 1- take "p" random points. (Ip) , i.e. a point is defined by time and location
 # 2- a trace is compatible with  Ip if  Ip is included in the current trace  (exactement ou avec une erreur spatiale et une fenetre temporelle)
 # obtain S(Ip) number of users sharing this Ip
#estimated percentage of S(Ip) on N iteration 

# run : python uniqueness-paralel.py ./federatedUniqueness/Privamov-filter-100km-POI/200m-5min/POIs-traces-merged/ 500 2 4 1000 Users-uniqueness/privamov/unique-p-4-2h-500m/

inputDirectory= sys.argv[1] # dataset where we have one trace per user;
spatialResolution=int(sys.argv[2]) # in meters for example 20 meters
temporalResolution=int(sys.argv[3]) # in hours for example : 1 hour of difference without considering the date.
p=int(sys.argv[4]) # represent number of point selected for example p =2, 3 , 4 ....
iterations= int(sys.argv[5])
outputDirectory= sys.argv[6]


if not os.path.exists(outputDirectory):
	os.makedirs(outputDirectory)


# approximate radius of earth in km
R = 6373.0

def distance(lat1,lon1,lat2,lon2):
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))
	distance = R * c
	return distance *1000  #return value in meter

def temporal_distance(t1,t2,t_resolution):
	#convert temporal resolution into a time stamp in ms
	t1=datetime.fromtimestamp(t1/1000).strftime('%H:%M')
	t2=datetime.fromtimestamp(t2/1000).strftime('%H:%M')
	datetime_t1 = datetime.strptime(t1, '%H:%M')
	datetime_t2 = datetime.strptime(t2, '%H:%M')

	hours_added = timedelta(hours = float(t_resolution)/2)
	datetime_t1_max = datetime_t1 + hours_added
	datetime_t1_min = datetime_t1 - hours_added

	if ( datetime_t2 >= datetime_t1_min ) and (datetime_t2 <= datetime_t1_max):
		return 1
	else:
		return 0


def generatePtn(p,max_index,df_current):
	list_points=[]
	list_index=[]
	for i in range(p):
		index_point=random.randint(1, max_index-1)
		list_index.append(index_point)
	for i in list_index:
		row=df_current.iloc[[i]]
		lat=row['lat'].item()
		lon=row['lon'].item()
		timestamp=row['timestamp'].item()
		list_points.append((lat,lon,timestamp))
	return list_points


def checkValidity(p,max_index,df_current,list_df_users,user_SIp_its,it):
	SIp=1
		#select p random points and save them in a list
	list_points=generatePtn(p,max_index,df_current)
		#check if p points are in other users
	for df in list_df_users:
		# start cheking p points in df :
		cpt_p=0
		for point in list_points: # we go on each point in p 
			res=df.apply(lambda x: 1 if (distance(point[0],point[1],x['lat'],x['lon']) <= spatialResolution) and (temporal_distance(point[2],x['timestamp'],temporalResolution) ==1) else 0, axis=1)
			cpt_p=cpt_p+ res.max()
			#df['result']=0
		if cpt_p == p:
			SIp= 0
			break
	user_SIp_its.insert(it,SIp)


def unique(filename,inputDirectory,p,spatialResolution,temporalResolution,iterations,outputDirectory):	
	#user_SIp_its=[-1]*iterations
	users = set(os.listdir(inputDirectory))-set([filename])
	df_current=pd.read_csv(inputDirectory+'/'+filename,names=['lat','lon','timestamp'],header=0)
	max_index= df_current.shape[0]
	# read prealably the other user df and put them in a tab :
	list_df_users=[]
	for user in users:
		df=pd.read_csv(inputDirectory+'/'+user,names=['lat','lon','timestamp'],header=0)
		list_df_users.append(df)
	thread_list_perUser = []
	user_SIp_its=[]*iterations
	for it in range(iterations):
		print("iterations : "+ str(it)+ ", "+filename)
		t = threading.Thread(target=checkValidity, args=(p,max_index,df_current,list_df_users,user_SIp_its,it))
		thread_list_perUser.append(t)
		t.start()

	for thread in thread_list_perUser:
		thread.join()
	
	data = pd.Series(user_SIp_its)
	#frame = { 'Author': auth_series, 'Article': article_series }
  
	df_data = pd.DataFrame(data)
	#data=data.transpose()
	data.to_csv(outputDirectory+'/'+filename,index=False,header=0)



NB_PROCESS = psutil.cpu_count(logical=False)

# Create pool of processes
executor = concurrent.futures.ProcessPoolExecutor(NB_PROCESS)


# For each trace launch the trace processing job
futures = [executor.submit(unique,filename,inputDirectory,p,spatialResolution,temporalResolution,iterations, outputDirectory) for filename in os.listdir(inputDirectory)]
#futures = [processCsvTraceFile(filename,inputDirectory,outputDirectory,sliceSize) for filename in os.listdir(inputDirectory) if filename.endswith(".csv")]


# Wait for the processes to finish
concurrent.futures.wait(futures)
