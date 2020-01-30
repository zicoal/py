#!/usr/bin/python
# coding:utf-8

import  pandas  as pd
import  sys,os
import logging
import time
import string
from matplotlib import pyplot as plt
import numpy as np
import xlrd

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

data_dir="d://BaiduNetdiskDownload//肺炎相关数据//"

num_file=0
num_record=0
for root,b,files in os.walk(data_dir):
    for file in files:
#        logging.error(file)
        if file.endswith(".xlsx") and not file.startswith("~"):
            num_file+=1
            f= os.path.join(root, file)
            logging.info("reading:"+f)
            wb = xlrd.open_workbook(f)
            logging.info("Read Done:"+f)
            st=wb.sheets()[0]
            print(st.nrows)
            num_record+=st.nrows
logger.info("files:%s, records:%s" % (num_file,num_record))
sys.exit()