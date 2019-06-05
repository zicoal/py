#!/usr/bin/python
# coding:utf-8

import os
import logging
import time
import string
from matplotlib import pyplot as plt
import numpy as np
#from cn.edu.hznu.tools import plotfig as pf



def shaded_Error_Bar_Mean_Error_Params_SubPlot_OneCaption(x, y, subplot_pos, pars=[], logx=False,logy=False, n=1, isSave=False):

    colors=['red','pink']
    line_width=2
    fig_file=''
    xlabel=''
    ylabel=''

    pos = subplot_pos.split(',')
    axes = plt.subplot(int(pos[0]),int(pos[1]),int(pos[2]))

    if (pars[4] is not None):
        fig_file = pars[4]
    if (pars[3] is not None):
        colors = pars[3]
    if (pars[2] is not None):
        line_width = pars[2]

    if (isSave==True):
        if (pars[1] is not None):
            ylabel = pars[1]
            ylabel_axis = pars[8]
            plt.text(ylabel_axis[0], ylabel_axis[1],  ylabel, rotation=90, transform=axes.transAxes,
                 color='black', size='12', weight="light")
#            plt.text(ylabel_axis[0], ylabel_axis[1],  ylabel, rotation=90, transform=axes.transAxes,
#                 family="fantasy", color='black', size='12', weight="light")

        if (pars[0] is not None):
            xlabel = pars[0]
            xlabel_axis = pars[7]
            plt.text(xlabel_axis[0], xlabel_axis[1], xlabel,  transform=axes.transAxes,
                     color='black', size='12', weight="light")
#            plt.text(xlabel_axis[0], xlabel_axis[1], xlabel,  transform=axes.transAxes,
#                     family="fantasy", color='black', size='12', weight="light")

    x_max=20001
    y_max=20001
    axes.set_xlim(1,x_max)
    axes.set_ylim(1,y_max)
    x_compare = list(range(x_max))
    y_compare = list(range(x_max))
    axes.plot(x_compare,y_compare, linewidth=0.5, linestyle=':', color='black')
    x1 =x[0]
    y1= y[0]
    x2 =x[1]
    y2= y[1]
    axes.scatter(x1,y1,s=line_width, color=colors[0])
    axes.scatter(x2,y2,s=line_width, color='black')

    if (pars[5] is not None):
        legend=pars[5]
        xy=plt.axis()
        x=2
        y=7000
        axes.text(x,y,legend[0], \
                  family="fantasy", size='8', color = 'black', weight = "light")
        x=50
        y=700
        axes.text(x,y,legend[1], \
                   size='6', color = 'red', weight = "light")

        x=50
        y=3
        axes.text(x,y,legend[2], \
                   size='6', color = 'black', weight = "light")

    if (logx == True):
        axes.set_xscale("log")
    if (logy == True):
        axes.set_yscale("log")


    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                        wspace=0.1, hspace=0.05)
    axes.tick_params(axis='x', tickdir='in', labelsize=7)
    axes.tick_params(axis='y', tickdir='out', labelsize=7)

    if (pars[9] ==False):
        axes.set_yticks([])
    if (pars[10] ==False):
        axes.set_xticks([])

    if(isSave==True):
        ax = plt.gca()
        #ax.update_datalim(corners)
        plt.savefig(fig_file, dpi=1200,  bbox_inches='tight')
        plt.close('all')


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

dir_data = "D:\\py\\data\\initialreaction\\results\\Fig234\\Fig3\\%s\\%s.txt"
fig_data = "D:\\py\\data\\initialreaction\\figs\\comparision_predicted_real_size_%s"
#weibo_axis_motif
logx = True
logy = True
#Weibo
num_data_type = 2
str_data_type = "Weibo"
xlabel_bak='Real Cascade Size (%s)'% str_data_type
ylabel_bak='Predicted Cascade Size'


data_observation=['10m_1h','10m_2h','10m_12h','10m_1d','10m_final','10m_final']
data_compare=['1h','2h','12h','1d','2d','final']


#fig_names = ['%s_vs_1hour_cascade_%s' % (str_feature,str_data_type),'%s_vs_2hour_cascade_%s' % (str_feature,str_data_type),'%s_vs_1day_cascade_%s' % (str_feature,str_data_type), '%s_vs_2day_cascade_%s' % (str_feature,str_data_type), '%s_vs_10day_cascade_%s' % (str_feature,str_data_type),'%s_vs_final_cascade_%s' % (str_feature,str_data_type)]
color_index=0
colors = [('red','pink'),('blue','lightblue'),('green','lightgreen'),('black','gray')]

xx=-1.3
xy=-0.2
yx=-2.5
yy=1.5

y_text_axis=[yx,yy]
x_text_axis=[xx,xy]
#y_text_axis=[[yx,yy],[yx,yy],[yx,yy],[yx,yy],[yx,yy],[yx,yy]]
#x_text_axis=[[xx,xy],[xx,xy],[xx,xy],[xx,xy],[xx-0.3,xy-0.05],[xx-0.3,xy-0.05]]


num_data_dir=0
for data_obs in data_observation:


    isSave = False
    logger.info('plotting Compare Real vs Predicted Cascade (%s): %s ' % (str_data_type,data_obs))
    legend=[data_obs]
    tmp_src_file = dir_data %(str_data_type,data_obs)
    f = open(tmp_src_file, encoding='UTF-8', mode='r', errors='ignore')
    line =f.readline()
    tmp_values_x=[]
    tmp_values_y=[]
    line_count=0
    r1=0
    while line:
        if(line_count==0):
            words = line.replace('\n', '').split('=')
            r1=float(words[1])
            line_count+=1
            line = f.readline()
            continue
        elif(line_count==1):
            line_count+=1
            line = f.readline()
            continue
        words = line.replace('\n', '').split('\t')
        tmp_values_x.append(float(words[0]))
        tmp_values_y.append(float(words[1]))
        line = f.readline()
    f.close()
    legend.append("r=%s" % r1)

    data_pre = data_compare[num_data_dir]
    tmp_src_file = dir_data % (str_data_type, data_pre)
    f = open(tmp_src_file, encoding='UTF-8', mode='r', errors='ignore')
    line = f.readline()
    tmp_values_x_compare = []
    tmp_values_y_compare = []
    line_count = 0
    r2 = 0
    while line:
        if (line_count == 0):
            words = line.replace('\n', '').split('=')
            r2 = float(words[1])
            line_count += 1
            line = f.readline()
            continue
        elif (line_count == 1):
            line_count += 1
            line = f.readline()
            continue
        words = line.replace('\n', '').split('\t')
        tmp_values_x_compare.append(float(words[0]))
        tmp_values_y_compare.append(float(words[1]))
        line = f.readline()
#    logger.info(tmp_values_x)
    xlabel = None
    ylabel = None
    x_num_show=False
    y_num_show=False
    legend.append("r=%s" % r2)
#   pf.shaded_Error_Bar_Mean_Error(tmp_values_x,tmp_values_y,tmp_values_err,logx=logx)
#        subplot=int("%s%s%s" % (len(data_observation),len(data_predict[0]), num_data_dir*(len(data_predict[0]))+num_data_count+1))
    subplot="%s,%s,%s" % (2,3, num_data_dir+1)
    fig_file=""
    #logger.info(subplot)
    if (num_data_dir==len(data_observation)-1 ):
       isSave=True
       fig_file = (fig_data % (str_data_type+".png"))
       xlabel = xlabel_bak
       ylabel = ylabel_bak
    if(num_data_dir %3==0):
        y_num_show = True
    if(num_data_dir / 3>=1):
        x_num_show = True
    x=[tmp_values_x,tmp_values_x_compare]
    y=[tmp_values_y,tmp_values_y_compare]
    pars=[xlabel,ylabel,1,colors[0],fig_file,legend,num_data_type,x_text_axis,y_text_axis,y_num_show,x_num_show]
    shaded_Error_Bar_Mean_Error_Params_SubPlot_OneCaption(x,y,subplot,pars=pars,logx=logx,logy=logy,isSave=isSave)
    f.close()
   # os._exit(0)
    num_data_dir += 1

