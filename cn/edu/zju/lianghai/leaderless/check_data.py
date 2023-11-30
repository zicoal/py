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

f1 = 'D:\\pydata\\data\\lianghai\\mentions_tozike.txt'
logger.info("loading data...")
time_start=time.time()

'''
**Test Reading data
f2 = 'D:\\py\\data\\lianghai\\events\\%s.csv'
df = pd.read_csv(f2 % "paper_239")
time_end=time.time()
logger.info("data loaded! time:%d s.",time_end-time_end)
data = df.values.tolist()
logger.info(data[0][0].split("\t"))
logger.info(len(data))
exit(0)
'''
#df = pd.read_csv(f1,usecols=[0])
#df = pd.read_csv(f1,nrows=10)
#data = df.values.tolist()
#for i in range(len(data)):
#    for j in range(len(data[i])):
#        print(data[i][j] )
time_end = time.time()
logger.info("data loaded...time cost:%d s'", time_end - time_start)
#print(df)
tweets = {}

time_end = time.time()
#data = df.values.tolist()
logger.info("data converted...time cost:%d s'", time_end - time_start)

f = open(f1, encoding='UTF-8', mode='r', errors='ignore')
line = f.readline()

line_count = 0
event_number = 0
event = ""
tweets_number=0
total_movements=0
movement_index =0
while line:
    words = line.replace("\n","").split('\t')
    event_id=words[0]

    if event_id =="movement_index":
#        line_count += 1
        movement_index +=1
        time_end = time.time()
        logger.info("movement_index/line:%d/%d, time cost:%d s'",  movement_index
                    , line_count, time_end - time_start)
#        line = f.readline()
#        continue


    line_count += 1
    line = f.readline()
f.close()
time_end = time.time()
logger.info("movement_index/line:%d/%d, time cost:%d s'",  movement_index
            , line_count, time_end - time_start)

for i in range(len(data)):
    if data[i][0] not in tweets:
        tweets[data[i][0]] = 1
#tweets = [data[i][0] for i in range(len(data))]
#tweets = set(tweets)
#tweets = sorted(list(set(tweets)))
logger.info("total number of tweets:",len(tweets))

time_end = time.time()
logger.info('The end,cost time:%d s', time_end - time_start)
