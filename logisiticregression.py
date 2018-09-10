# -*- coding: utf-8 -*-
"""
Created on Mon Nov 07 18:14:42 2016

@author: zico
"""
import math
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np

#read train data
x=[]
y=[]
f=open('horseColicTraining.txt')
for line in f:
    a = line.split("\t")
    tmp=[1]
    for i in range(21):
        tmp.append(float(a[i]))        
    x.append(tmp)        
    y.append(float(a[21]))
   #print str(x[len(x)-1][0]+x[len(x)-1][1])+":"+str(y[len(y)-1])
f.close()
#model training
alpha = 0.001
loss = 50
Eps = 0.001
theta =ones(22)
#theta = [0.001,0.002,0.001,0.001,0.001,0.002,0.002,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.002,0.002,0.003,0.001]
#while loss>Eps:
iters=500
start = time.time()
for iter in range(iters):
    loss = 0  
    #train parameters
    for i in range(len(y)) :
        tmp = 0
        #alpha = 4 / (1.0 + i + iter) + 0.0001
        for j in range(len(theta)) :
            tmp = tmp + theta[j] * x[i][j]
        h=1.0/(1+ exp(-1 * tmp))
        for j in range(len(theta)) :
            theta[j] = theta[j]+alpha*(y[i]-h)*x[i][j]
    if iter%500==0:
        end = time.time()
        print "iter:%d/%d,percent:%.2f%%, time:%.2f" % (iter,iters,1.0*iter/iters*100, (end-start)/1000)
    # judge convergence
    '''
    for i in range(len(y)) :
        Error = 0
        for j in range(len(x[0])) :
            Error = Error + theta[j]*x[i][j]
        Error = 1.0/(1+ math.exp(-1 * Error)) - y[i]
        Error = Error * Error
        loss = loss + Error
   '''
    #print loss
#test model
#f=open('horseColicTraining.txt')
f=open('horseColicTest.txt')
xt=[]
yt=[]
lines =0
for line in f:
    a = line.split("\t")    
    tmp=[]
    tmp.append(1)
    for i in range(21):
        tmp.append(float(a[i]))        
    xt.append(tmp)        
    yt.append(float(a[21]))
   #print str(x[len(x)-1][0]+x[len(x)-1][1])+":"+str(y[len(y)-1])
    lines+=1
f.close()
et=0.0

xcord1 = []; ycord1 = []
xcord2 = []; ycord2 = []
errors=0
p=0.5
for i in range(len(yt)) :
    tmp = 0
    for j in range(len(xt[0])) :
        tmp = tmp + theta[j]*xt[i][j]  
    h=1.0/(1+ math.exp(-1 * tmp))
    et = et + abs(h-yt[i])
    '''
    if h>0.5 :
        xcord1.append(i+1);
        ycord1.append(xt[i][3])
    else:
        xcord2.append(i+1);
        ycord2.append(xt[i][3])
    '''
    if (h>p and yt[i]==1) or (h<=p and yt[i]==0):
        xcord1.append(i+1);
        ycord1.append(yt[i])
    else :
        xcord2.append(i+1);
        ycord2.append(yt[i])
        errors+=1
print et
print str(errors) +"/"+ str(lines)+","+str(100.0*errors/lines)
#plot
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.scatter(xcord,ycord, c=colors, s=markers)
ax.scatter(xcord1, ycord1, s=30, c='green',marker="o")
ax.scatter(xcord2, ycord2, s=30, c='red',marker="x")
plt.xlabel('X1')
plt.ylabel('X2')
plt.show()
#draw figure

