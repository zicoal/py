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

#df = pd.read_csv(f2 % "paper_10")
#logger.info(df)
#exit(0)
#headers  =["movement_index", "tweet_id", "created_at", "author_id", "mentions"]
headers  ="movement_index\ttweet_id\tcreated_at\tauthor_id\tmentions\n"
#headers = pd.DataFrame(columns=line.replace("\n","").split('\t'))
print(headers)
#exit(0)
line_count = 0
event_number = 1
event = ""
#data = pd.DataFrame(columns=headers, index=False)
tweets_number=0
total_movements=108
data=headers

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

    if (line_count ==0 or len(line)==0) :
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
    if event_id == event:
        data=data+line
#        data.loc[len(data)] = [word for word in words]
        if (line_count%10000==0):
             logger.info("line:%d, event: %d/%s",line_count,event_number,event_id)
    elif event_id == "movement_index":
        fx = open(f2 % event, encoding='UTF-8', mode='w', errors='ignore')
        fx.write(data)
        fx.close()
        #        data.to_csv(f2 % event, index=False)
        time_end = time.time()
        logger.info("event:%s,event/total:%d/%d,tweets/line:%d/%d,time:%ds'", event, event_number,total_movements,line_count-tweets_number, line_count, time_end - time_start)
        event_number += 1
        event = ""
        tweets_number = line_count
        data= headers
#        data = pd.DataFrame(columns=headers,index=False)
    line_count += 1

    line = f.readline()
f.close()
#THE LAST EVENT
fx = open(f2 % event, encoding='UTF-8', mode='w', errors='ignore')
fx.write(data)
fx.close()
event_number += 1
time_end = time.time()
logger.info("event: %s, event/total:%d/%d, tweets/line:%d/%d,time:%ds'", event, event_number, total_movements,
            line_count - tweets_number, line_count, time_end - time_start)
#time_end = time.time()
#logger.info("movement_index/line:%d/%d, time cost:%d s'",  movement_index
#            , line_count, time_end - time_start)

time_end = time.time()
logger.info("DONE! events/tweets:%d/%d, time:%ds'", event_number, line_count, time_end - time_start)
