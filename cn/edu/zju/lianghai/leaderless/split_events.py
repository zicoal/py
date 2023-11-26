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
f2 = 'D:\\py\\data\\lianghai\\events\\%s.csv'
logger.info("starting...")
time_start=time.time()

f = open(f1, encoding='UTF-8', mode='r', errors='ignore')
line = f.readline()

headers  =["movement_index", "tweet_id", "created_at", "author_id", "mentions"]
#headers = pd.DataFrame(columns=line.replace("\n","").split('\t'))
logger.info(headers)
line_count = 0
event_number = 0
event = ""
data = pd.DataFrame(columns=headers)
tweets_number=0
total_movements=108

while line:
    words = line.replace("\n","").split('\t')
    event_id=words[0]
    '''
    if event_id =="movement_index":
#        line_count += 1
        movement_index +=1
        time_end = time.time()
        logger.info("movement_index/line:%d/%d, time cost:%d s'",  movement_index
                    , line_count, time_end - time_start)
#        line = f.readline()
#        continue
    '''

    if (line_count ==0 or len(line)==0 ) :
        line_count += 1
        line = f.readline()
        continue
#    if  event_id=="movement_index" :
#        line_count += 1
#        event = ""
#        data = pd.DataFrame(columns=headers)
#        line = f.readline()
#        continue
    if  event=="":
        event = event_id
    elif event_id == event:
        data.loc[len(data)] = [word for word in words]
        if (line_count%10000==0):
             logger.info("line:%d, event: %s",line_count,event_id)
    elif event_id == "movement_index":
        data.to_csv(f2 % event, index=False)
        event_number += 1
        time_end = time.time()
        logger.info("event: %s, event/total:%d/%d, tweets/line:%d/%d, time cost:%d s'", event, event_number,total_movements,line_count-tweets_number, line_count, time_end - time_start)
        event = ""
        tweets_number = line_count
        data = pd.DataFrame(columns=headers)
    line_count += 1
    line = f.readline()
f.close()
#THE LAST EVENT
data.to_csv(f2 % event, index=False)
event_number += 1
time_end = time.time()
logger.info("event: %s, event/total:%d/%d, tweets/line:%d/%d, time cost:%d s'", event, event_number, total_movements,
            line_count - tweets_number, line_count, time_end - time_start)
#time_end = time.time()
#logger.info("movement_index/line:%d/%d, time cost:%d s'",  movement_index
#            , line_count, time_end - time_start)

time_end = time.time()
logger.info("DONE! events/tweets:%d/%d, time cost:%d s'", event_number, line_count, time_end - time_start)
