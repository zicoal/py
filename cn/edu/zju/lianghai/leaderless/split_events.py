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

headers = pd.DataFrame(columns=line.replace("\n","").split('\t'))
logger.info(headers)
line_count = 0
event_number = 0
event = ""
data = headers
while line:
    if (line_count ==0 or len(line)==0) :
        line_count += 1
        line = f.readline()
        continue
    words = line.replace("\n","").split('\t')
    event_id=words[0]
    if  event=="":
        event = event_id
    elif event_id == event:
        data.loc[len(data)] = [word for word in words]
    elif (event_id != event):
        data.to_csv(f2 % event, index=False)
        data = headers
        event_number+=1
        time_end = time.time()
        logger.info("events/tweets:%d/%d, time cost:%d s'", event_number , line_count, time_end - time_start)
        if (event_number ==2):
            f.close()
            exit(0)
    line_count += 1
    line = f.readline()
f.close()
#    dates.append(int(words[0]))
#    dates.append(line_count-1)
#    news_cul.append(int(words[2]))
#    if (len(words[3])==0):
#        words[3]=0
#    cases_cul.append(int(words[3]))

time_end = time.time()
logger.info("events/tweets:%d/%d, time cost:%d s'", event_number, line_count, time_end - time_start)
