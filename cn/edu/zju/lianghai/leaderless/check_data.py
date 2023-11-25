import matplotlib.pyplot as plt
import math
import os
import networkx as nx
import numpy as np
import pandas as pd
from random import *
import time
import logging
import xlsxwriter
from openpyxl import load_workbook
from xlsxwriter import Workbook

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



#logger.info(getscore(5))
#exit(0)

f1 = 'D:\\py\\data\\lianghai\\mentions_tozike.txt'
logger.info("loading data...")
time_start=time.time()
df = pd.read_csv(f1,usecols=[0])
#df = pd.read_csv(f1,nrows=10)
#data = df.values.tolist()
#for i in range(len(data)):
#    for j in range(len(data[i])):
#        print(data[i][j] )
time_end = time.time()
logger.info("data loaded...time cost:%d s'", time_end - time_start)
#print(df)
tweets = {}
data = df.values.tolist()
tweets = [data[i][0] for i in range(len(data))]
tweets = sorted(list(set(tweets)))
logger.info("total number of tweets:",len(tweets))

time_end = time.time()
logger.info('The end,cost time:%d s', time_end - time_start)
