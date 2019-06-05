#!/usr/bin/python
# coding:utf-8

import os
import logging
import time
import string
from matplotlib import pyplot as plt
import numpy as np
#from cn.edu.hznu.tools import plotfig as pf



def shaded_Error_Bar_Mean_Error_Params_SubPlot_OneCaption(x, y,error, subplot_pos, pars=[], logx=False,logy=False, n=1, isSave=False):

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
    '''
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
     '''

    if (isSave == False):
        xlegend = ['10min','30min','1h']
        for i in range(len(error)):
            axes.errorbar(x[i],y[i],yerr=errors[i],fmt='-')
        plt.legend(xlegend,
                       loc='upper right',
                       fontsize=5)

    else:
        for i in range(len(error)):
            axes.errorbar(x[i],y[i],yerr=errors[i])


    if (pars[5] is not None):
        legend=pars[5]
        xy = plt.axis()
        x=5
     #   print(xy)
        if(isSave==True):
            y=xy[2]+0.08
        else:
            y = xy[2] + 0.1
        axes.text(x,y,legend, \
                  size='12', color = 'black', weight = "light")

    xtickers=(('1h','2h','12h','1d','2d','10d','final'))
#    axes.set_xticks(x[0])
    axes.set_xticklabels(xtickers)
  #  plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
  #                      wspace=0.1, hspace=0.05)

    axes.tick_params(axis='x', tickdir='in', labelsize=7)
    axes.tick_params(axis='y', tickdir='out', labelsize=7)


    if(isSave==True):
        ax = plt.gca()
        #ax.update_datalim(corners)
        plt.savefig(fig_file, dpi=400,  bbox_inches='tight')
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

dir_data = "D:\\py\\data\\initialreaction\\results\\Fig234\\Fig4\\%s\\%s.txt"
fig_data = "D:\\py\\data\\initialreaction\\figs\\mae.png"
#weibo_axis_motif
logx = False
logy = False
#Weibo
num_data_type = 2
str_data_type = ["Weibo","Twitter"]
xlabel_bak='Time'
ylabel_bak='MAE'


data_observation=['10mins','30mins','1hour']


#fig_names = ['%s_vs_1hour_cascade_%s' % (str_feature,str_data_type),'%s_vs_2hour_cascade_%s' % (str_feature,str_data_type),'%s_vs_1day_cascade_%s' % (str_feature,str_data_type), '%s_vs_2day_cascade_%s' % (str_feature,str_data_type), '%s_vs_10day_cascade_%s' % (str_feature,str_data_type),'%s_vs_final_cascade_%s' % (str_feature,str_data_type)]
color_index=0
colors = [('red','pink'),('blue','lightblue'),('green','lightgreen'),('black','gray')]

xx=-1.3
xy=-0.2
yx=-2.5
yy=1.5

y_text_axis=[yx,yy]
x_text_axis=[xx,xy]



num_data_dir=0
legend=[]
for dt in str_data_type:
    x=[]
    y=[]
    errors=[]
    legend=dt
    isSave = False
    for data_obs in data_observation:

        logger.info('plotting MAE (%s): %s ' % (dt,data_obs))

        tmp_src_file = dir_data %(dt,data_obs)
        f = open(tmp_src_file, encoding='UTF-8', mode='r', errors='ignore')
        line =f.readline()
        tmp_values_x=[]
        tmp_values_y=[]
        tmp_error=[]
        line_count=0
        r1=0
        while line:
            if(line_count<1):
                line_count+=1
                line = f.readline()
                continue
            words = line.replace('\n', '').split('\t')
            tmp_values_x.append(float(words[0]))
            tmp_values_y.append(float(words[1]))
            tmp_error.append(float(words[2]))
            line = f.readline()
        x.append(tmp_values_x)
        y.append(tmp_values_y)
        errors.append(tmp_error)
        f.close()

    xlabel = None
    ylabel = None
    x_num_show=True
    y_num_show=True

    subplot="%s,%s,%s" % (2,2, num_data_dir+1)
    fig_file=""
    #logger.info(subplot)
    if (num_data_dir==len(str_data_type)-1):
       isSave=True
       fig_file = fig_data
       xlabel = xlabel_bak
       ylabel = ylabel_bak
    pars=[xlabel,ylabel,1,colors[0],fig_file,legend,num_data_type,x_text_axis,y_text_axis,y_num_show,x_num_show]
    shaded_Error_Bar_Mean_Error_Params_SubPlot_OneCaption(x,y,errors, subplot,pars=pars,logx=logx,logy=logy,isSave=isSave)
    f.close()
   # os._exit(0)
    num_data_dir += 1

