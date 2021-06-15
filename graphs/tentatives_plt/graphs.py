import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import time

import csv
import sys
import skmob
import pandas as pd
import time

#inputFile=sys.argv[1]
#outputFile=sys.argv[2]
#duration=int(sys.argv[3]) #in minutes
#radius=float(sys.argv[4])/2000.0 #input diameter in meters, radius eventually in kilometers
#inputUser=sys.argv[5]

defaultUser=24
defaultInputFile = '/home/mdupraz/Documents/L3_stage/mobility-datasets/privamov-tree-30days/24.csv'
defaultOutputFile = '/home/mdupraz/Documents/L3_stage/code_clustering/scikitmob/results/dur15_diam200/o2.csv'
#taille_res =[(1488, 23, 4, 0.18109920000000557, 0.06978229999998575),
            #(28288, 126, 14, 3.5245369000000437, 1.1643670999999927),
            #(49413, 85, 7, 6.2205372999999895, 2.0461087000000475),
            #68448, 423, 30, 8.619970799999976, 3.3434527000000003),
            #(265696, 1666, 177, 33.851786600000196, 14.253807499999766),
            #(477204, 1134, 84, 61.287547599999925, 51.5582773000001),
            #(537004, 809, 120, 68.53074360000028, 30.26284130000022),
            #(694960, 7191, 712, 89.53106480000042, 67.25998179999988),
            #(836204, 15656, 1355, 109.37472539999999, 247.63929629999996)]

def list_from_csv (file):
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
		for row in reader: #user lat lgt timein timeout
			point=list(map(float,row))
			point.insert(5,point[4]-point[3]) #delta-time
			tracemob.append(point)
			#print(tracemob[i])
			i+=1
		return tracemob, i
		
def graph (listpois):
	"""
	input : 
	l : list
	ilat : index of latitudes in l
	ilgt : index of longitude in l
	itime : index of deltatime in l
	
	output : nothing
	
	side effect : creates a graph with abscissa=latitude, ordinate=longitude and applicate=deltatime
	"""
	n=len(listpois)
	latitude= [listpois[i][1] for i in range (n)]
	longitude = [listpois[i][2] for i in range (n)]
	deltatime= [listpois[i][5] for i in range (n)]
	
	fig=plt.figure()
	ax=plt.axes(projectin='3d')
	ax.plot3D(atitude, longitude, deltatime,'gray')
	plt.show()

"""	
    taille=[taille_res[i][0] for i in range(len(taille_res))]
    duree_seg_taille=[taille_res[i][3] for i in range(len(taille_res))]
    duree_fus_taille=[taille_res[i][4] for i in range(len(taille_res))]
    plt.plot(taille,duree_seg_taille,color='blue',marker='x', label='curb')
    plt.xlabel('taille(pixels)')
    plt.ylabel('b: temps de segmentation(s),r: temps de fusion (s)')
    plt.plot(taille, duree_fus_taille,color='magenta',marker='x')
    ax.set_title("Simple Plot")  # Add a title to the axes.
    ax.legend()  # Add a legend.
    plt.show()
    #functions
    x = np.linspace(0, 2, 100)
    ax.plot(x, x**2, label='quadratic')

scikit = [[0,0,0,0] for i in range (0, nbr_poi)]
"""
graph(list_from_csv(defaultOutputFile))
