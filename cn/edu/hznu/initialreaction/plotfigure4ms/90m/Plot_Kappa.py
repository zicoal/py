#!/usr/bin/python
# coding:utf-8

import os,sys
import logging
import time
import string
from matplotlib import pyplot as plt
import numpy as np
#from cn.edu.hznu.tools import plotfig as pf


color_line= [['lavender','pink','palegreen'],['lightblue','navajowhite','lightgreen']]

def shaded_Error_Bar_Mean_Error_Params_SubPlot_OneCaption(x, y,error, subplot_pos, pars=[], logx=False,logy=False, n=1, isSave=False):

    line_width=2
    fig_file=''
    xlabel=''
    ylabel=''

    pos = subplot_pos.split(',')
    axes = plt.subplot(int(pos[0]),int(pos[1]),int(pos[2]))

    plt.tick_params(labelsize=5)

    if(pars[6]==0):
        plt.text(-0.6,1.04,'A' + pos[2],fontsize=10)
        yt=[ 0.65, 0.75, 0.85, 0.95, 1]
        plt.yticks(yt)
    else:
        plt.text(-0.5,1.022,'A' + pos[2],fontsize=10)
        yt=[0.80, 0.85, 0.90, 0.95, 1]
        plt.yticks(yt)

    if (pars[4] is not None):
        fig_file = pars[4]
#    if (pars[3] is not None):
#        colors = pars[3]
    if (pars[2] is not None):
        line_width = pars[2]

#    plt.xlabel(pars[0],fontsize='5')
    if (isSave is not True):
        plt.ylabel("K-Value",fontsize='9')


    cl=color_line[0]
    if(pars[6]>1):
        cl= color_line[1]
    if(pars[6]==1 or pars[6]==4 ):
        xlegend = ['30m', '60m', '90m']
        if (pars[6] > 1):
            xlegend = ['t=3', 't=5', 't=7']
        for i in range(len(error)):
            axes.errorbar(x[i], y[i], yerr=errors[i], fmt='-',color=cl[i],ecolor=cl[i])
        plt.legend(xlegend,
                   loc='upper right',
                   fontsize=7, ncol=1, frameon=False)
    else:
        for i in range(len(error)):
            logger.info(cl[i])
            axes.errorbar(x[i], y[i], yerr=errors[i],color=cl[i],ecolor=cl[i])
        #sys.exit()
    #plt.yticks([1])
    if(pars[11] ==2): # the 3d subgraph
        if (pars[5] is not None):
            legend=pars[5]
            xy = plt.axis()
            x=4.3
            y = 0.85
            if (pars[6] > 1 ):
                x = 5.5
            if (pars[6]==1):
                y=0.96
            if( pars[6] == 4):
                y = 0.92
            axes.text(x,y,legend, \
                      size='12', color = 'black', weight = "light")

    #(a-e)
    '''
    xy = plt.axis()
    x = (xy[0]) +0.1
    y = (xy[2]) + ((xy[3])-(xy[2]))/10
    if (pars[6] == 2):
        x = x+0.6
    axes.text(x, y, pars[12], \
              color='black', weight="light", size=10)
    '''
    xt=[1,2,3,4,5,6,7]
    if(pars[6]<2):#weibo or twitter
        xtickers=['1h','2h','12h','1d','2d','10d','final']
    else:
        xtickers=['10','15','20','25','30','40','final']

#    axes.set_xticks(x[0])
    #axes.set_xticklabels(xtickers)

    plt.xticks(xt,xtickers)

    '''
    if ( pars[6] == 4):
        plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                   wspace=0.2, hspace=0.15)
    '''


    axes.tick_params(axis='x', tickdir='in', labelsize=7)
    axes.tick_params(axis='y', tickdir='out', labelsize=7)


    if(isSave==True):
        ax = plt.gca()
        #ax.update_datalim(corners)
        plt.savefig(fig_file+ ".png", dpi=200,  bbox_inches='tight')
        plt.savefig(fig_file + ".pdf", format='pdf', dpi=600, bbox_inches='tight')
        plt.close('all')
'''
    if (isSave==True):
        if (pars[0] is not None):
            xlabel = pars[0]
            xlabel_axis = pars[7]
            plt.text(xlabel_axis[0], xlabel_axis[1],  xlabel,transform=axes.transAxes,
                 color='black', size='12', weight="light")


        if (pars[1] is not None):
            ylabel = pars[1]
            ylabel_axis = pars[8]
            plt.text(ylabel_axis[0], ylabel_axis[1],  ylabel, rotation=90, transform=axes.transAxes,
                 color='black', size='12', weight="light")
'''

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

#dir_data = "D:\\py\\data\\initialreaction\\results\\201911\\Multi-Classification\\Prediction_Kappa_Value\\Fig%s\\%s_Prediction_Percentage_Error_%s_%s\\%s.txt"
dir_data = "D:\\py\\data\\initialreaction\\results\\201911\\Result_Updata_1.5Hour\\Prediction_Kappa_Value\\Fig%s\\%s_Prediction_Kappa_5_400\\%s.txt"

fig_data = "D:\\py\\data\\initialreaction\\figs\\fig3-1" #e.g.Weibo_200_Kappa
#fig_data = "D:\\py\\data\\initialreaction\\figs\\kappa" #e.g.Weibo_200_Kappa
#weibo_axis_motif
logx = False
logy = False
#Weibo
num_data_type = 2
str_data_type = ["Weibo","Twitter"]
#str_data_type = ["Weibo","Twitter","Random","Small_World","Scale_Free"]
str_fig_type = ["Weibo","Twitter","RN","SW","SF"]

xlabel_bak='Time'
ylabel_bak='K-Value'


data_observation=[['30m','1h','1.5h'],\
                    ['30m','1h','1.5h'],\
                    ['3','5','7'],\
                    ['3','5','7'],\
                    ['3','5','7']
                  ]
data_motif=['5']
data_legend=['(a)','(b)','(c)','(d)','(e)','(f)']
data_size=['100','200']

#fig_names = ['%s_vs_1hour_cascade_%s' % (str_feature,str_data_type),'%s_vs_2hour_cascade_%s' % (str_feature,str_data_type),'%s_vs_1day_cascade_%s' % (str_feature,str_data_type), '%s_vs_2day_cascade_%s' % (str_feature,str_data_type), '%s_vs_10day_cascade_%s' % (str_feature,str_data_type),'%s_vs_final_cascade_%s' % (str_feature,str_data_type)]
color_index=0
colors = [('red','pink'),('blue','lightblue'),('green','lightgreen'),('black','gray')]

xx=-0.8
xy=-0.25
yx=-3.0
#yx=-0.20
yy=1.25

y_text_axis=[yx,yy]
x_text_axis=[xx,xy]



num_data_dir=1
legend=[]
num_data_type=0
num=0
motif = data_motif[0]
for dt in str_data_type:

    logger.info("Plotting %s ." % dt)

    tmp_num_motif = 0

    x = []
    y = []
    errors = []
    legend = str_fig_type[num_data_type]
    isSave = False
    for data_obs in data_observation[num_data_type]:

        #tmp_src_file = dir_data % (num_data_type+num+1,dt,data_obs)
        tmp_src_file = dir_data % (5 * num_data_type + 4, dt, data_obs)
#        tmp_src_file = dir_data % (2*num_data_type+num+1,dt, motif,data_size[num],data_obs)
        logger.info('plotting Kappa : %s ' % tmp_src_file)
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
            if((data_obs!=data_observation[num_data_type][0]) and num_data_type <2):
                tmp_values_x.append(float(words[0])+1) # 去掉第一个数字 1h-1h
            else:
                tmp_values_x.append(float(words[0]))
            tmp_values_y.append(float(words[1]))
            tmp_error.append(float(words[2]))
            line = f.readline()
        x.append(tmp_values_x)
        y.append(tmp_values_y)
        errors.append(tmp_error)
        f.close()

    xlabel = xlabel_bak
    ylabel = None
    x_num_show=True
    y_num_show=True

    subplot = "%s,%s,%s" % (2, 2, num_data_type+1)
#    if (num_data_type >1):# (len(dir_data) - 1)):
#        subplot = "%s,%s,%s" % (2,3, num_data_type+2)
    fig_file=""
    #logger.info(subplot)
    if (num_data_type==len(str_data_type)-1):
       isSave=True
       fig_file = fig_data
#               xlabel = xlabel_bak
#               ylabel = ylabel_bak
       xlabel = xlabel_bak
       ylabel = ylabel_bak
    pars=[xlabel,ylabel,1,colors[0],fig_file,legend,num_data_type,x_text_axis,y_text_axis,y_num_show,x_num_show,tmp_num_motif,data_legend[num_data_type] + " " +str_fig_type[num_data_type] ]
    shaded_Error_Bar_Mean_Error_Params_SubPlot_OneCaption(x,y,errors, subplot,pars=pars,logx=logx,logy=logy,isSave=isSave)
    f.close()
   # os._exit(0)
    tmp_num_motif += 1
#num_data_dir += 1

    #sys.exit()
    num_data_type +=1

sys.exit()