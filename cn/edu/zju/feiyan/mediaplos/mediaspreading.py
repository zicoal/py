#!/usr/bin/python
# coding:utf-8
#COVID-19 spreading
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
fig="..//figs//meida_spreading_sir_%s"
def formatnum(x, pos):
    return '$%f$' % (x/10000000)
#formatter = FuncFormatter(formatnum)
#ax2.yaxis.set_major_formatter(formatter)



dates=[]
cases=[]
news=[]
f = open(data_dir, encoding='UTF-8', mode='r', errors='ignore')
line = f.readline()
line_count = 0
valid_date=16
while line:
    if (line_count <valid_date):
        line_count += 1
        line = f.readline()
        continue
    words = line.replace('号', '').replace('\n', '').split('\t')
#    logger.info(words)
    dates.append(int(words[0]))
    #news.append(int(words[1]))
    news.append(math.log10(int(words[1])))
    if (len(words[4])==0):
        words[4]=0
    cases.append(int(words[4]))
    line_count += 1
    line = f.readline()
f.close()

alpha=0.2
lamda=1
def get_media_impact(t):
    theta = 0.0
    tmp_count=t #t starts from 0
    if t==0:
        theta = lamda * news[t]
    else:
        for i in range(t-1,-1,-1):
            theta += math.pow(1-lamda,t-i)* news[i]
        theta = lamda * (news[t] + theta)
    #logger.info(math.exp(-1*theta*alpha))
    #sys.exit()
    return math.exp(-1*theta*alpha)

N = 1000000 #N个节点，默认标号为0到N-1
m0 = 2  # m0*2 equals average degree
MAX_Spreading_Time=len(news)
num_initial_infected=20
#num_initial_infected=int(N*0.02)
beta =0.35
mu=1

logger.info("Generating network...")

g = nx.barabasi_albert_graph(N, m0)
degrees = g.degree()
degree=[]
#for d in range(0,N):
#    degree.append(g.degree(d))
#print(degrees)
#print(degree)
#print("average/sum:%s/%s" % (np.mean(degree),np.sum(degree)))
#sys.exit()

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
IR=[]
x.append(tmp_spread_count)
I.append(len(list_infected))
S.append(len(list_suspective))
R.append(0)
IR.append(len(list_infected))
while (tmp_spread_count <= MAX_Spreading_Time):
    for infected in list_infected:
        for nb in  list(g.neighbors(infected)):
            if (nb in list_suspective and random.random() <= beta*get_media_impact(tmp_spread_count)):
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
    IR.append(len(list_infected)+len(list_recoverd))
    logger.info("run/total:%s/%s" % (tmp_spread_count,MAX_Spreading_Time))

#plt.plot(x,S,label="S")
plt.plot(x,I,label="I")
#plt.plot(x,R,label="R")
plt.plot(x,IR,label="I+R")
plt.legend(loc="best", frameon=False)
plt.xlabel("Time")
plt.ylabel('Numbers')
logger.info("S:%s, I:%s, R:%s",len(list_suspective),len(list_infected),len(list_recoverd))

#nx.draw(BA, ps, with_labels=False, node_size=30)
plt.savefig((fig % N)+".png", dpi=500, bbox_inches='tight')
#plt.show()
sys.exit()