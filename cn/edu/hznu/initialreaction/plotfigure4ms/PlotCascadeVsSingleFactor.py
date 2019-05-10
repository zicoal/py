#!/usr/bin/python
# coding:utf-8

import os
import logging
import time
import string
from matplotlib import pyplot as plt
import numpy as np
from cn.edu.hznu.tools import plotfig as pf



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
#logger.addHandler(fh)Hs_Hr
dir_data = "D:\\py\\data\\initialreaction\\results\\%s\\Feature_VS_Size\\"

dir_twitter= dir_data % "Twitter"
dir_weibo= dir_data % "Weibo"

fig_data = "D:\\py\\data\\initialreaction\\figs\\"

files = ['hub_time', 'initial_size', 'initial_time','motif_entropy']
labels=['Initial Participation ', 'Initial Attention','Initial Time','Initial Complexity']
num_file_count=0
#Twitter
for file in files:
    tmp_src_file = dir_weibo + file +".txt"
    logger.info(tmp_src_file)
    f = open(tmp_src_file, encoding='UTF-8', mode='r', errors='ignore')
    line =f.readline()
    tmp_values_x=[]
    tmp_values_y=[]
    tmp_values_err=[]
    line_count=0
    logx = True
    while line:
        if(line_count==0):
            line_count+=1
            line = f.readline()
            continue
        words = line.replace('\n', '').split('\t')
        tmp_values_x.append(float(words[0]))
        tmp_values_y.append(float(words[1]))
        tmp_values_err.append(float(words[2]))
        line = f.readline()
#    logger.info(tmp_values_x)
    if num_file_count == len(files):
        logx = False
    pf.shaded_Error_Bar_Mean_Error(tmp_values_x,tmp_values_y,tmp_values_err,logx=logx)
    num_file_count +=1
    f.close()
    exit(0)
