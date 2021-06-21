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
#import psutil

#version POI

inputDirectory= sys.argv[1] # dataset where for each user, a file containing POIs ('IDs','lat','lon','total','timestampStart','timestampEnd','diameter')
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
	lat1=radians(lat1)
	lon1=radians(lon1)
	lat2=radians(lat2)
	lon2=radians(lon2)
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
		index_point=random.randint(0, max_index-1)
		#print(index_point)
		list_index.append(index_point)
	randomPOIs.append(list_index)
	for i in list_index:
		row=df_current.iloc[[i]]
		lat=row['lat'].values[0]
		lon=row['lon'].values[0]
		timestamp_start=row['timestampStart'].values[0]
		timestamp_end=row['timestampEnd'].values[0]
		IDs=row['IDs'].values[0]

		list_points.append([IDs,lat,lon,timestamp_start,timestamp_end])
		
	return list_points


def checkValidity(p,max_index,df_current,list_df_users,user_SIp_its,it):
	SIp=1
		#select p random points and save them in a list
	
	if max_index <= p:
		list_points=[]
		for i in range(max_index):
			row=df_current.iloc[[i]]
			lat=row['lat'].values[0]
			lon=row['lon'].values[0]
			timestamp_start=row['timestampStart'].values[0]
			timestamp_end=row['timestampEnd'].values[0]
			IDs=row['IDs'].values[0]
			list_points.append([IDs,lat,lon,timestamp_start,timestamp_end])
	else:
		list_points=generatePtn(p,max_index,df_current)
	

		#check if p points are in other users
	for df in list_df_users:
		# start cheking p points in df :
		cpt_p=0
		for point in list_points: # we go on each point in p 
			
			res=df.apply(lambda x: 1 if (distance(point[1],point[2],x['lat'],x['lon']) <= spatialResolution) and (temporal_distance(point[4],x['timestampStart'],temporalResolution) ==1) else 0, axis=1) #res contient, pour chacun des POIs (1 ligne de df) de l'autre utilisateur en cours d'observation (df=1 utilisateur parmi la liste des df_users), si ce POI est commun avec le POI en cours d'observation
			i=0
			while i < len(res):
				if res[i]==1:
					cpt_p+=1
					break
				else:
					i+=1

			#cpt_p=cpt_p+ res.max()#on ajoute 1 si l'autre utilisateur a un POI proche de celui considéré actuellement
			#print(type(cpt_p))
			#print("cptttttttttt",cpt_p)
			#df['result']=0
		if cpt_p == p:
			SIp= 0 #l'utilisateur n'est pas unique
			break;
	#print(SIp)
	user_SIp_its.insert(it,SIp)

def unique(filename,inputDirectory,p,spatialResolution,temporalResolution,iterations,outputDirectory):	
	#user_SIp_its=[-1]*iterations
	users = set(os.listdir(inputDirectory))-set([filename])
	df_current=pd.read_csv(inputDirectory+'/'+filename,names=['IDs','lat','lon','timestampStart','timestampEnd']) #ligne de code modifiée par rapport à la version primault
	max_index= df_current.shape[0]
	# read prealably the other user df and put them in a tab :
	list_df_users=[]
	for user in users:
		df=pd.read_csv(inputDirectory+'/'+user,names=['IDs','lat','lon','timestampStart','timestampEnd']) #ligne de code modifiée par rapport à la version primault
		list_df_users.append(df)
	thread_list_perUser = []
	user_SIp_its=[]*iterations
	for it in range(iterations):
		#print("iterations : "+ str(it)+ ", "+filename)
		t = threading.Thread(target=checkValidity, args=(p,max_index,df_current,list_df_users,user_SIp_its,it))
		thread_list_perUser.append(t)
		t.start()
		if max_index <= (p):
			break
		#t.start()


	#for thread in thread_list_perUser:
		#thread.start()
	
	for thread in thread_list_perUser:
		thread.join()
	
	data = pd.Series(user_SIp_its)
	#frame = { 'Author': auth_series, 'Article': article_series }
	df_data = pd.DataFrame(data)
	#data=data.transpose()
	data.to_csv(outputDirectory+'/'+filename,index=False,header=0)
	
	data2 = pd.Series(randomPOIs, dtype=int)
	df_data2 = pd.DataFrame(data)
	#data=data.transpose()
	data2.to_csv(outputDirectory+'/POIs'+filename,index=False,header=0)
	



#NB_PROCESS = psutil.cpu_count(logical=False)

## Create pool of processes
#executor = concurrent.futures.ProcessPoolExecutor(NB_PROCESS)


## For each trace launch the trace processing job
#futures = [executor.submit(unique,filename,inputDirectory,p,spatialResolution,temporalResolution,iterations, outputDirectory) for filename in os.listdir(inputDirectory)]

listUsers=os.listdir(inputDirectory)
for filename in listUsers:
	randomPOIs=[]
	unique(filename,inputDirectory,p,spatialResolution,temporalResolution,iterations, outputDirectory)
#en sortie, randomPOIs contient dans chaque ligne : nom_utilisateur | les p POIs tirés au hasard


# Wait for the processes to finish
#concurrent.futures.wait(futures)
