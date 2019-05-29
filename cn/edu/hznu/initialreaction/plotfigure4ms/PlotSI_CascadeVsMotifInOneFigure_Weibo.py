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

dir_data = "D:\\py\\data\\initialreaction\\results\\FigS_Data\\FigS3\\%s\\motif=%s.txt"
fig_data = "D:\\py\\data\\initialreaction\\figs\\figS3\\%s"
#weibo_axis_motif
logx = False
logy = False
#Weibo
num_data_type = 1
str_data_type = "Weibo"
xlabel_bak='Initial Structure (%s)'% str_data_type
data_dir = ['a','b','c', 'd','e']
str_feature="motif"

#xlabels=['Initial Complexity','Initial Time','Initial Participation ', 'Initial Attention']
fig_names = ['%s_vs_1hour_cascade_%s' % (str_feature,str_data_type),'%s_vs_2hour_cascade_%s' % (str_feature,str_data_type),'%s_vs_1day_cascade_%s' % (str_feature,str_data_type), '%s_vs_2day_cascade_%s' % (str_feature,str_data_type),'%s_vs_final_cascade_%s' % (str_feature,str_data_type)]
ylabel=['Cascade Size (One-Hour)','Cascade Size (Two-Hour)','Cascade Size (One-Day)','Cascade Size (Two-Day)','Cascade Size (Final)']
#ylabel=['1-Hour Cascade Size (%s)','2-Hour Cascade Size(%s)','1-Day Cascade Size(%s)','2-Day Cascade Size(%s)','Final Cascade Size(%s)']
color_index=0
colors = [('red','pink'),('green','lightgreen'),('blue','lightblue'),('black','gray')]


y_text_axis=[[-10.7,60],[-10.7,85],[-10.7,150],[-10.7,155],[-10.7,150]]
x_text_axis=[[-5.5,-11],[-5.5,-14],[-5.5,-20],[-5.5,-20],[-5.5,-19]]


num_data_dir=0



for d in data_dir:
#    if num_data_type ==2:
#        continue
    isSave = False
    logger.info('plotting '+ xlabel_bak +d)

    for file in range(5,11):
        tmp_src_file = dir_data %(d,file)
        f = open(tmp_src_file, encoding='UTF-8', mode='r', errors='ignore')
        line =f.readline()
        tmp_values_x=[]
        tmp_values_y=[]
        tmp_values_err=[]
        line_count=0
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
        xlabel = None
        legend = "motif=%s" % file
    #   pf.shaded_Error_Bar_Mean_Error(tmp_values_x,tmp_values_y,tmp_values_err,logx=logx)
        subplot=int("23%s" % (file-4))
        fig_file=""
        #logger.info(subplot)
        if file==10:
           isSave=True
           fig_file = (fig_data % fig_names[num_data_dir]  )+".png"
           xlabel=xlabel_bak
        pars=[xlabel,ylabel[num_data_dir] ,1,colors[color_index],fig_file,legend,num_data_type,file-4,x_text_axis[num_data_dir],y_text_axis[num_data_dir]]
        pf.shaded_Error_Bar_Mean_Error_Params_SubPlot_OneCaption(tmp_values_x,tmp_values_y,tmp_values_err,subplot,pars=pars,logx=logx,logy=logy,isSave=isSave)
        f.close()
    num_data_dir += 1

