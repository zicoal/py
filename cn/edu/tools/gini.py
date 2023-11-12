# -*- coding: utf-8 -*-
"""
Created on Thu Nov 03 20:14:48 2016

@author: zico
"""
import numpy as np

def gini_coefficient(src):
	"""
#	>>> gini_coefficient([245,362,826])
# 	0.40544312630844381
#	>>> gini_coefficient([2,10,5,6,12])
#	0.35714285714285715
	"""
	out = []
	for i in range(0,len(src)):
		for j in range(i+1,len(src)):
			out.append(abs(src[i]-src[j]))
	avdiff = np.mean(out)
	mn = np.mean(src)
	return avdiff / (2*mn)

s=[1,1,1,1]
print('I: ',gini_coefficient(s))
s=[1,2,1,1]
print('II: ',gini_coefficient(s))
s=[1,1,2,2]
print('III: ',gini_coefficient(s))
s=[1,1,2,2]
print('IV: ',gini_coefficient(s))
s=[1,1,2,3]
print('V: ',gini_coefficient(s))
s=[1,2,2,2]
print('VI: ',gini_coefficient(s))
s=[1,2,2,3]
print('VII: ',gini_coefficient(s))
s=[1,2,3,3]
print('VIII: ',gini_coefficient(s))
s=[1,2,3,4,5,6,7,8,9,10]
print('IX: ',gini_coefficient(s))
