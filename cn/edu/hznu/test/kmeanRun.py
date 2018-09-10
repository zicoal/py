import math
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np



def Euclid(x,y,b):
    d=0
    d= (x-b[0])*(x-b[0])+(y-b[1])*(y-b[1])
    d = math.sqrt(d)
    return d



f=open('kmeans.csv')
x=[]
y=[]
c=0
for line in f:
    if c>0:
        tmp=line.split(",")
        x.append(float(tmp[0]))
        y.append(float(tmp[1]))
    c=1


labelchanged = 1

#ck=[(1.0,1.0),(5.0,5.0),(-1.0,8.0)] # centroids
#ck=[[1.0,1.0],[5.0,5.0],[-1.0,0.0],[11.0,11.0]] # centroids
ck=[[-1.0,3.0],[0.75,-1],[1.0,6.0]] # centroids
#ck=[[1.8,4.0],[0.7,0.5],[4.2,1.0]] # centroids
ic=zeros(len(x))
cc=0
check = 14
dist = zeros(len(x)) + 99999
while labelchanged >0 :
    labelchanged = 0
    for i in range(len(x)):
        tmp =999
        tmpc=-1
        for j in range(len(ck)):
            d= Euclid(x[i],y[i],ck[j])
            if d<tmp:
                tmp=d
                tmpc=j
        if (ic[i] != tmpc):
            ic[i] = tmpc
            labelchanged+=1
        #if i==check:
          # print "check:"+str(tmpc)+","+str(ic[check])+","+str(Euclid(x[check],y[check],ck[0])) + "," +str(Euclid(x[check],y[check],ck[1]))+ "," +str(Euclid(x[check],y[check],ck[2]))
    # update centroids
    #print "come: %d" % (cc)
    if labelchanged > 0:
        for j in range(len(ck)):
            a=0
            b=0
            count = 0
            for i in range(len(x)):
                if(ic[i]==j):
                    a+=x[i]
                    b+=y[i]
                    count+=1
            if count>0:
               # print str(ck[j][0]) + "," + str(ck[j][1]) + "," +str(a/count) + "," + str(b/count) + "," + str(count)
                ck[j][0]=a/count
                ck[j][1]=b/count
    cc+=1
   # print ck



# plot
# ax.scatter(xcord,ycord, c=colors, s=markers)
xcord1 = []
xcord2 = []
xcord3 = []
ycord1 = []
ycord2 = []
ycord3 = []

count = [0, 0, 0]
for i in range(len(x)):
    if ic[i] == 0:
        xcord1.append(x[i])
        ycord1.append(y[i])
        count[0] += 1
    elif ic[i] == 1:
        xcord2.append(x[i])
        ycord2.append(y[i])
        count[1] += 1
    elif ic[i] == 2:
        xcord3.append(x[i])
        ycord3.append(y[i])
        count[2] += 1
# draw figure
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(xcord1, ycord1, s=30, c='m', marker="o")
ax.scatter(xcord2, ycord2, s=30, c='c', marker="o")
ax.scatter(xcord3, ycord3, s=30, c='r', marker="o")
ax.scatter(ck[0][0], ck[0][1], s=100, c='m', marker="s")
ax.scatter(ck[1][0], ck[1][1], s=100, c='c', marker="D")
ax.scatter(ck[2][0], ck[2][1], s=100, c='r', marker="v")
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

