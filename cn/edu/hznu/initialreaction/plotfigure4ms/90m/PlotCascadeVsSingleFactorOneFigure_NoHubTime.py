#!/usr/bin/python
# coding:utf-8

import os
import sys
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


#more parameters
#pars=[xlabel,ylabel, linewidth, color=[mean_color,bound_color],fig_file]
def shaded_Error_Bar_Mean_Error_Params_SubPlot(category, values_mean, errors, subplot_pos, pars=[], logx=False,logy=False, n=1, isSave=False):
    values_up=[]
    values_down=[]
    num_count=0
    scale=0.3
    for x in values_mean:
        if (logy == True):
            values_up.append(x + n * errors[num_count])
            if(errors[num_count]/x>0.25):
                values_down.append((x - x*0.4))
            else:
                values_down.append((x - n * errors[num_count]))
        else:
            if (errors[num_count] / x > 0.25):
                values_up.append(x + x * scale)
                values_down.append((x - x * scale))
            else:
                values_up.append(x + n * errors[num_count])
                values_down.append((x - n * errors[num_count]))

        num_count+=1

    colors=['red','pink']
    line_width=2
    fig_file=''


    axes = plt.subplot(subplot_pos)

    if (pars[4] is not None):
        fig_file = pars[4]
    if (pars[3] is not None):
        colors = pars[3]
    if (pars[2] is not None):
        line_width = pars[2]
    if (pars[1] is not None):
        ylabel = pars[1]
        axes.set_ylabel(ylabel, size='10')
    if (pars[0] is not None):
        xlabel = pars[0]
        axes.set_xlabel(xlabel, size='7')

    plt.tick_params(labelsize=7)
    axes.plot(category, values_up, colors[1])
    axes.plot(category, values_down, colors[1])
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                        wspace=0.3, hspace=None)
    plt.fill_between(category, values_down, values_up, color=colors[0], alpha=0.25)
    axes.plot(category, values_mean, linewidth=line_width, color=colors[0])

    if (pars[5] is not None):
        if (pars[6]==1):
            axes.text(2,95,pars[5])
        else:
            axes.text(1.5, 165, pars[5])

    if (logx == True):
        axes.set_xscale("log")
    if (logy == True):
        axes.set_yscale("log")


    if(isSave==True):
#        plt.savefig(fig_file, dpi=400, bbox_inches='tight')
        plt.savefig(fig_file+".png", dpi=200,  bbox_inches='tight')
        plt.savefig(fig_file+".pdf", format='pdf', dpi=600, bbox_inches='tight')
        plt.cla()
        plt.clf()
        plt.close()

dir_data = "D:\\py\\data\\initialreaction\\results\\%s\\Feature_VS_Size\\"

data_type=["Weibo","Twitter"]

fig_data = "D:\\py\\data\\initialreaction\\figs\\%s"

files = ['motif_entropy','initial_time', 'initial_size']
xlabels=['Initial Structure','Initial Time', 'Initial Attention']
file_names = ['cascade_vs_motif','cascade_vs_initial_time', 'cascade_vs_initial_size']
colors = [('red','pink'),('green','lightgreen'),('blue','lightblue'),('black','gray')]
ylabel='Cascade Size'
ylabel_bak='Cascade Size'
num_data_type=0
#Weibo
isSave = False
for d in data_type:
    num_file_count = 0
    num_data_type +=1
#    if num_data_type ==2:
#        continue
    for file in files:
        tmp_src_file = (dir_data % d) + file +".txt"
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
        xlabel = None
        lengend = None
        if num_file_count == 0:
            logx = False
            ylabel = ylabel_bak
            lengend = d
        else:
            ylabel=None
        if num_file_count == len(files)-1:
            logy = True
        if num_data_type!=1:
            xlabel=xlabels[num_file_count]
    #   pf.shaded_Error_Bar_Mean_Error(tmp_values_x,tmp_values_y,tmp_values_err,logx=logx)
        subplot=int("23%s" % (3*(num_data_type-1) + num_file_count+1))
        fig_file=""
        logger.info(tmp_src_file)
        #logger.info(subplot)
        if num_data_type==2 and num_file_count==2:
           isSave=True
           fig_file = (fig_data % "fig1-1" )
    #        fig_file = (fig_data % "cascade_vs_single_factor")
        pars=[xlabel,ylabel,1,colors[num_file_count],fig_file,lengend,num_data_type]
        shaded_Error_Bar_Mean_Error_Params_SubPlot(tmp_values_x,tmp_values_y,tmp_values_err,subplot,pars=pars,logx=logx,logy=logy,isSave=isSave)
        isSave= False
        #pf.shaded_Error_Bar_Mean_Error_Params(tmp_values_x,tmp_values_y,tmp_values_err,pars=pars,logx=logx,logy=logy,isShow=False)
        num_file_count +=1
        f.close()
        #exit(0)
sys.exit()