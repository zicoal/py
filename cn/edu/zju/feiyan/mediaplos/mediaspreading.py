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
    return '$%.1f$' % (x/10000000)
#formatter = FuncFormatter(formatnum)
#ax2.yaxis.set_major_formatter(formatter)

N = 10
m0 = 2

g = nx.barabasi_albert_graph(N, m0)
ps = nx.spring_layout(g)   # 布置框架

#for i in range(0, N):
#    logger.info("%s: %s" % (i,list(G.neighbors(i))))
#a = nx.to_numpy_matrix(g) # to matrix

labels_infected = []
num_infected=0
num_initial_infected=3
for i in range(0, N):
    labels_infected.append(0)

list_infected=[]
#intial infected
for i in range(0, num_initial_infected):
    tmp_in_list=True
    while tmp_in_list:
        tmp_rand = random.randint(0, N-1)
        if tmp_rand not in list_infected:
#            logger.info(tmp_rand)
            labels_infected[tmp_rand] = 1
            list_infected.append(tmp_rand)
            tmp_in_list =False


logger.info(list_infected)
logger.info(labels_infected)
#while (b)

#nx.draw(BA, ps, with_labels=False, node_size=30)
#plt.show()
sys.exit()