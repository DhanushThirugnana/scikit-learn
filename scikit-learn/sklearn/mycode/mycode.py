"""
Below is the code for the Fuzzy Cmeans algorithm as a part of adding additional feature to the sklearn package.
It is a basic implementation of Fuzzy Cmeans clustering. 

Returns Centroids of the clusters and cluster labels of the data points given.
parameters of cmeans()  are: Input DataFrame , Number of clusters required and Number of iterations to be done, respectively.

"""

import numpy as np
import random
import pandas as pd

# Fuzzy CMeans algorithm
class MyCMeans:
	# Initializing Fuzzy parameter p. It is generally recommended that p = 2
    def __init__(self):
        self.p=2
        
	# Sample function check
    def pri(self):
        print(self.p)

	# Assign random membership function c(i,j) for each data point
	# Membership function is the likelihood that a data point (xi) belongs to a particular cluster (j) or not, 0<=c(i,j)<=1
    def member_func(self,X,noOfClusters):
        cij=[]
        for i in range(len(X)):
            wt=[]
            randomcij = [random.random() for i in range(noOfClusters)]
            sigma=sum(randomcij)
            for i in randomcij:
                wt.append(i/sigma)
            cij.append(wt)
        return cij
		
	#Initializing /Re-initializing the data points to new clusters based on the c(i,j) values
    def cluster_func(self,X,cij):
        labelPts=[]
        max_pb=-10000
        for i in range(len(X)):
            max_pb, indx = max((a, b) for (b, a) in enumerate(cij[i]))
            labelPts.append(indx)
        return labelPts
    
	
	# Computing the c(i,j) values based on new centroids
    def cij_calc(self,X,cij,centroid,p):
        p = 2.0/(p-1)
        ln=len(centroid)
        for i in range(len(X)):
            dist=[np.linalg.norm(X[i]-centroid[j]) for j in range(ln)]
            for k in range(ln):
                g = sum([float(dist[k]/dist[y]) ** p for y in range(ln)])
                cij[i][k] = 1.0/g       
        return cij
        

	# Computing new centroids using the formula: [Sigma(1 to N)((c(i,j)^p)*x) / Sigma(1 to N) (c(i,j)^p)]; 
    def centroid_calc(self,X,cij,num):
        cij_val = list(zip(*cij))
        centroid=[]
        for i in range(num):
            row = list(cij_val[i])
            #print(row)
            rowp = [cx ** self.p for cx in row]
            sump = sum(rowp)
            l1 = list()
            for k in range(len(X)):
                row1 = list(X[k])
                mul = [rowp[k] * val for val in row1]
                l1.append(mul)
            cen_vals=[sum(x) for x in zip(*l1)]
            c = [z/sump for z in cen_vals]
            centroid.append(c)
        return centroid

	# Function to be called.
	# Computes the clusters and centroids of the clusters using Fuzzy-cmeans
    def cmeans(self,arr,c, itr):
        if isinstance(c,int):
            noOfClusters = c
        else:
            print("Required Int, provided ",type(c))
            return
        if isinstance(itr,int):
            noOfIter=itr
        else:
            print("Required Int, provided ",type(itr))
            return 
        
        if not isinstance(arr, pd.DataFrame):
            print("Required Dataframe, provided ",type(arr))
            return
        X=arr.values
        cij=self.member_func(X,noOfClusters)
        for i in range(noOfIter):
            f=20
            while f>0:
                centroid = self.centroid_calc(X,cij,noOfClusters)
                cij = self.cij_calc(X,cij, centroid,self.p)
                clusters = self.cluster_func(X,cij)
                f-=1
        return centroid, clusters