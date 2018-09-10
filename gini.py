# -*- coding: utf-8 -*-
"""
Created on Thu Nov 03 20:14:48 2016

@author: zico
"""
import numpy as np

def gini_coefficient(src):
	"""
	>>> gini_coefficient([245,362,826])
 	0.40544312630844381
	>>> gini_coefficient([2,10,5,6,12])
	0.35714285714285715
	"""
	out = []
	for i in range(0,len(src)):
		for j in range(i+1,len(src)):
			out.append(abs(src[i]-src[j]))
	avdiff = np.mean(out)
	mn = np.mean(src)
	return avdiff / (2*mn)
s=[]
f=open('1.txt')
for line in f:
    s.append(float(line.strip()))
print gini_coefficient(s)
f.close()
s=[]
f=open('2.txt')
for line in f:
    s.append(float(line.strip()))
print gini_coefficient(s)