#!/usr/bin/python
# coding:utf-8

import  pandas  as pd
import  sys,os
import logging
import time
import string
from matplotlib import pyplot as plt
import numpy as np
import xlrd,math,random
from matplotlib.ticker import FuncFormatter
import matplotlib.transforms as mtransforms
import networkx as nx

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 定义handler的输出格式
#logger to console
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
#fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(ch)

data_dir="d://BaiduNetdiskDownload//肺炎相关数据//results//报道-日期.txt"

def formatnum(x, pos):
    return '$%f$' % (x/10000000)
#formatter = FuncFormatter(formatnum)
#ax2.yaxis.set_major_formatter(formatter)

N = 1000 #N个节点，默认标号为0到N-1
m0 = 2
MAX_Spreading_Time=200
num_initial_infected=int(N*0.02)
beta =0.1
mu=0.1

logger.info("Generating network...")

g = nx.barabasi_albert_graph(N, m0)
ps = nx.spring_layout(g)   # 布置框架

#for i in range(0, N):
#    logger.info("%s: %s" % (i,list(G.neighbors(i))))
#a = nx.to_numpy_matrix(g) # to matrix

labels_infected = []
num_infected=0
list_suspective=[]
list_infected=[]
list_recoverd=[]
logger.info("initializatoin....")
for i in range(0, N):
    labels_infected.append(0)
    list_suspective.append(i)

#intialization
for i in range(0, num_initial_infected):
    tmp_in_list=True
    while tmp_in_list:
        tmp_rand = random.randint(0, N-1)
        if tmp_rand not in list_infected:
#            logger.info(tmp_rand)
            labels_infected[tmp_rand] = 1
            list_infected.append(tmp_rand) # add to infected list
            list_suspective.remove(tmp_rand) #remove infected nodes from suspective list
            tmp_in_list =False

#logger.info(list_infected)
#logger.info(labels_infected)
#logger.info(len(list_suspective))
logger.info("initialized!")

#spreading
tmp_spread_count=0
x=[]
S=[]
I=[]
R=[]
x.append(tmp_spread_count)
I.append(len(list_infected))
S.append(len(list_suspective))
R.append(0)
while (tmp_spread_count < MAX_Spreading_Time):
    for infected in list_infected:
        for nb in  list(g.neighbors(infected)):
            if (nb in list_suspective and random.random() <= beta):
                list_infected.append(nb)
                list_suspective.remove(nb)
        if(random.random()<=mu):
            list_infected.remove(infected)
            list_recoverd.append(infected)
    tmp_spread_count += 1
#    logger.info("time: %s, infected: %s" % (tmp_spread_count,num ))
    x.append(tmp_spread_count)
    I.append(len(list_infected))
    S.append(len(list_suspective))
    R.append(len(list_recoverd))

plt.plot(x,S,label="S")
plt.plot(x,I,label="I")
plt.plot(x,R,label="R")
plt.legend(loc="best", frameon=False)
plt.xlabel("Time")
plt.ylabel('Numbers')
logger.info("S:%s, I:%s, R:%s",len(list_suspective),len(list_infected),len(list_recoverd))

#nx.draw(BA, ps, with_labels=False, node_size=30)
plt.show()
#sys.exit()