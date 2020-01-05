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

data_type=["Weibo","Twitter"]

fig_data = "D:\\py\\data\\initialreaction\\figs\\%s"

files = ['motif_entropy','initial_time','hub_time', 'initial_size']
xlabels=['Initial Complexity','Initial Time','Initial Participation ', 'Initial Attention']
file_names = ['cascade_vs_motif','cascade_vs_initial_time','cascade_vs_hub_time', 'cascade_vs_initial_size']
colors = [('red','pink'),('green','lightgreen'),('blue','lightblue'),('black','gray')]
ylabel='Cascade Size'

num_data_type=0
#Weibo
isSave = False
for d in data_type:
    num_file_count = 0
    num_data_type +=1
    for file in files:
        tmp_src_file = (dir_data % d) + file +".txt"
        logger.info(tmp_src_file)
        f = open(tmp_src_file, encoding='UTF-8', mode='r', errors='ignore')
        line =f.readline()
        tmp_values_x=[]
        tmp_values_y=[]
        tmp_values_err=[]
        line_count=0
        logx = True
        logy = False
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
        if num_file_count == 0:
            logx = False
        else:
            ylabel=None
        if num_file_count == len(files)-1:
            logy = True
    #   pf.shaded_Error_Bar_Mean_Error(tmp_values_x,tmp_values_y,tmp_values_err,logx=logx)
        subplot=int("%s4%s" % (num_data_type,num_file_count+1))
        fig_file=""
        if num_data_type==2 and num_file_count==3:
            isSave=True
            fig_file = (fig_data % "all.png" )
        pars=[xlabels[num_file_count],ylabel,2,colors[num_file_count],fig_file]
        pf.shaded_Error_Bar_Mean_Error_Params_SubPlot(tmp_values_x,tmp_values_y,tmp_values_err,subplot,pars=pars,logx=logx,logy=logy,isSave=isSave)
        isSave= False
      # pf.shaded_Error_Bar_Mean_Error_Params(tmp_values_x,tmp_values_y,tmp_values_err,pars=pars,logx=logx,logy=logy,isShow=False)
        num_file_count +=1
        f.close()
        #exit(0)
