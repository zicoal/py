#!/usr/bin/python
# coding:utf-8

import os
import logging
import time
import string
from matplotlib import pyplot as plt
import numpy as np
#from cn.edu.hznu.tools import plotfig as pf



def shaded_Error_Bar_Mean_Error_Params_SubPlot_OneCaption(category, values_mean, errors, subplot_pos, pars=[], logx=False,logy=False, n=1, isSave=False):
    values_up=[]
    values_down=[]
    num_count=0
    for x in values_mean:
        values_up.append(x + n * errors[num_count])
        if(errors[num_count]/x>0.25):
            values_down.append((x - x*0.4))
        else:
            values_down.append((x - n * errors[num_count]))
        num_count+=1

    colors=['red','pink']
    line_width=2
    fig_file=''
    xlabel=''
    ylabel=''

    axes = plt.subplot(subplot_pos)
    if (pars[4] is not None):
        fig_file = pars[4]
    if (pars[3] is not None):
        colors = pars[3]
    if (pars[2] is not None):
        line_width = pars[2]

    if (isSave==True):
        if (pars[1] is not None):
            ylabel = pars[1]
            ylabel_axis = pars[9]
#            axes.set_ylabel(ylabel, size='10')
            plt.text(ylabel_axis[0], ylabel_axis[1],  ylabel, rotation=90, transform=axes.transAxes,
                 color='black', size='12', weight="light")
#            plt.text(ylabel_axis[0], ylabel_axis[1],  ylabel, rotation=90, transform=axes.transAxes,
#                 family="fantasy", color='black', size='12', weight="light")

        if (pars[0] is not None):
            xlabel = pars[0]
            xlabel_axis = pars[8]
            plt.text(xlabel_axis[0], xlabel_axis[1], xlabel,  transform=axes.transAxes,
                     color='black', size='12', weight="bold")
#            plt.text(xlabel_axis[0], xlabel_axis[1], xlabel,  transform=axes.transAxes,
#                     family="fantasy", color='black', size='12', weight="light")


    plt.tick_params(labelsize=7)
    axes.plot(category, values_up, colors[1])
    axes.plot(category, values_down, colors[1])
    plt.fill_between(category, values_down, values_up, color=colors[0], alpha=0.25)
    axes.plot(category, values_mean, linewidth=line_width, color=colors[0])
    if (pars[5] is not None):
        pos=pars[7]-4  #the position

      #  if (pars[6]==1):

        xy=plt.axis()
        #print(xy)
        x= 2
        y= (xy[3] )*0.7
        axes.text(x,y,pars[5],\
                family = "fantasy", color = 'black', style = "italic", weight = "light")

       # else:
        #    axes.text(0.9, 92, pars[5])


    if (logx == True):
        axes.set_xscale("log")
    if (logy == True):
        axes.set_yscale("log")

  #  print(subplot_pos)

    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                        wspace=0.3, hspace=None)


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

dir_data = "D:\\py\\data\\initialreaction\\results\\FigS_Data\\FigS9\\%s\\First %s mins.txt"
fig_data = "D:\\py\\data\\initialreaction\\figs\\figS9\\%s"
#weibo_axis_motif
logx = True
logy = True
#Weibo
num_data_type = 2
str_data_type = "Weibo"
xlabel_bak='Initial Attention (%s)'% str_data_type
str_feature="initial_attention"

data_dir = ['a','b','c', 'd','e','f']
fig_names = ['%s_vs_1hour_cascade_%s' % (str_feature,str_data_type),'%s_vs_2hour_cascade_%s' % (str_feature,str_data_type),'%s_vs_1day_cascade_%s' % (str_feature,str_data_type), '%s_vs_2day_cascade_%s' % (str_feature,str_data_type), '%s_vs_10day_cascade_%s' % (str_feature,str_data_type),'%s_vs_final_cascade_%s' % (str_feature,str_data_type)]
ylabel=['Cascade Size (One-Hour)','Cascade Size (Two-Hour)','Cascade Size (One-Day)','Cascade Size (Two-Day)','Cascade Size (Ten-Day)','Cascade Size (Final)']
#ylabel=['1-Hour Cascade Size (%s)','2-Hour Cascade Size(%s)','1-Day Cascade Size(%s)','2-Day Cascade Size(%s)','Final Cascade Size(%s)']
initial_times=[10,20,30,40,50,60]
color_index=2
colors = [('red','pink'),('green','lightgreen'),('blue','lightblue'),('black','gray')]

xx=-1.5
yx=-3
xy=-0.3
yy=1.6

y_text_axis=[[yx,yy],[yx,yy],[yx,yy],[yx,yy],[yx,yy],[yx,yy]]
x_text_axis=[[xx,xy],[xx,xy],[xx,xy],[xx,xy],[xx-0.3,xy-0.05],[xx-0.3,xy-0.05]]


num_data_dir=0



for d in data_dir:
#    if num_data_type ==2:
#        continue
    isSave = False
    logger.info('plotting '+ xlabel_bak +d)

    for file in range(5,11):
        tmp_src_file = dir_data %(d,initial_times[file-5])
        f = open(tmp_src_file, encoding='UTF-8', mode='r', errors='ignore')
        line =f.readline()
        tmp_values_x=[]
        tmp_values_y=[]
        tmp_values_err=[]
        line_count=0
        while line:
            if(line_count<2):
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
        legend = "first %s mins" % initial_times[file-5]
    #   pf.shaded_Error_Bar_Mean_Error(tmp_values_x,tmp_values_y,tmp_values_err,logx=logx)
        subplot=int("23%s" % (file-4))
        fig_file=""
        #logger.info(subplot)
        if file==10:
           isSave=True
           fig_file = (fig_data % fig_names[num_data_dir]  )+".png"
        if (num_data_dir == (len(data_dir) - 1) or num_data_dir == (len(data_dir) - 2)):
               xlabel = xlabel_bak
        pars=[xlabel,ylabel[num_data_dir] ,1,colors[color_index],fig_file,legend,num_data_type,file-4,x_text_axis[num_data_dir],y_text_axis[num_data_dir]]
        shaded_Error_Bar_Mean_Error_Params_SubPlot_OneCaption(tmp_values_x,tmp_values_y,tmp_values_err,subplot,pars=pars,logx=logx,logy=logy,isSave=isSave)
        f.close()
    num_data_dir += 1

