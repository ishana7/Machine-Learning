'''
We have given a collection of 8 points.
P1=[0.1,0.6] P2=[0.15,0.71] P3=[0.08,0.9] P4=[0.16, 0.85] P5=[0.2,0.3] P6=[0.25,0.5] P7=[0.24,0.1] P8=[0.3,0.2].
 Perform the k-mean clustering with initial centroids as m1=P1 =Cluster#1=C1 and m2=P8=cluster#2=C2.
 Answer the following
1] Which cluster does P6 belongs to?
2] What is the population of cluster around m2?
3] What is updated value of m1 and m2?
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.array([0.1,0.15,0.08,0.16,0.2,0.25,0.24,0.3])
y = np.array([0.6,0.71,0.9,0.85,0.3,0.5,0.1,0.2])

plt.plot(x,y,'o')
plt.show()

def eucledian_distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def kmeans
