#!/usr/bin/python
# coding:utf-8

import os,sys
import logging
import time
import string
from matplotlib import pyplot as plt
import numpy as np
#from cn.edu.hznu.tools import plotfig as pf


color_lines=['pink','lavender','skyblue']

def shaded_Error_Bar_Mean_Error_Params_SubPlot_OneCaption(x, y, subplot_pos, z,pars=[], logx=False,logy=False, n=1, isSave=False):

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
                 color='black', size='10', weight="light")

        if (pars[0] is not None):
            xlabel = pars[0]
            xlabel_axis = pars[7]
            plt.text(xlabel_axis[0], xlabel_axis[1], xlabel,  transform=axes.transAxes,
                     color='black', size='10', weight="light")
        xy=plt.axis()
        plt.text(0.001, 3000, 'C', fontsize=15)


    tmp_color=colors[0]
    if("30m" in  pars[5][0]):
       tmp_color = color_lines[0]
    else:
       tmp_color = color_lines[2]

    axes.scatter(x,y,s=line_width, color=tmp_color)
    axes.plot(x,z, linewidth=0.5, linestyle=':', color='gray')

#    print(pars[9])
    #plt.yticks([])
#    plt.gca().axes.get_yaxis().set_visible(False)

#    axes.plot(category, values_up, colors[1])
#    axes.plot(category, values_down, colors[1])
#    axes.plot(category, values_mean, linewidth=line_width, color=colors[0])

    if (pars[5] is not None):
        legend=pars[5]
        xy=plt.axis()
        x1=0
        y1=0
        logger.info(xy)
        if ("final" in pars[5][0]):
            x1 = 6
            y1=  0.005
            if ("30m" in pars[5][0]):
                x1 = 1.5
                y1 = 0.02
            xlegend = ['Real','Predicted']
            plt.legend(xlegend,
                           loc='upper right',
                           fontsize=7,ncol=1, frameon=False)
        else:
            x1 = 1.5
            y1= 0.001
            if ("30m" in pars[5][0]):
                y1 = 0.001

        axes.text(x1,y1,legend[0], \
                  family="fantasy", size='8', color = 'black', weight = "light")


    if (logx == True):
        axes.set_xscale("log")
    if (logy == True):
        axes.set_yscale("log")


    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                        wspace=0.15, hspace=0.12)
#    plt.subplots_adjust(left=0.2, bottom=0.2, right=0.8, top=0.8,hspace = 0.1, wspace = 0.1)


    if (pars[9] ==False):
        axes.set_yticks([])
    if (pars[10] ==False):
        axes.set_xticks([])

    axes.tick_params(axis='x', tickdir='in', labelsize=7)
    axes.tick_params(axis='y', tickdir='out', labelsize=7)

    if(isSave==True):
        ax = plt.gca()
#        plt.tight_layout()
        plt.savefig(fig_file+".png", dpi=200,  bbox_inches='tight')
        plt.savefig(fig_file+".pdf", format='pdf', dpi=400, bbox_inches='tight')
#        plt.savefig(fig_file, dpi=1200,  bbox_inches='tight')
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

dir_data = "D:\\py\\data\\initialreaction\\results\\201911\\distribution\\Prediction_Real_Distribution\\Fig1\\%s.txt"
fig_data = "D:\\py\\data\\initialreaction\\figs\\size_ccdf_two_%s"
#weibo_axis_motif
logx = True
logy = True
#Weibo
num_data_type = 2
str_data_type = "Weibo"
xlabel_bak='Cascade Size'
ylabel_bak='CCDF'


#data_observation=['10m','30m','1h']
#data_predict=[['1h','final'],['1h','final'],['2h','final']]

data_observation=['30m','1.5h']
data_predict=[['1','7'],['2','7']]
predict_map=[['1h','final'],['2h','final']]

#data_observation=['10m','30m','1h']
#data_predict=[['1h','2h','12h','1d','final'],['1h','2h','12h','1d','final'],['2h','12h','1d','2d','final']]


#fig_names = ['%s_vs_1hour_cascade_%s' % (str_feature,str_data_type),'%s_vs_2hour_cascade_%s' % (str_feature,str_data_type),'%s_vs_1day_cascade_%s' % (str_feature,str_data_type), '%s_vs_2day_cascade_%s' % (str_feature,str_data_type), '%s_vs_10day_cascade_%s' % (str_feature,str_data_type),'%s_vs_final_cascade_%s' % (str_feature,str_data_type)]
color_index=2
colors = [('red','pink'),('blue','lightblue'),('green','lightgreen'),('black','gray')]

'''
xx=-3.4
xy=-0.35
yx=-5.8
yy=2.5
'''

xx=-0.25
xy=-0.18
yx=-1.38
yy=1.2
y_text_axis=[yx,yy]
x_text_axis=[xx,xy]
#y_text_axis=[[yx,yy],[yx,yy],[yx,yy],[yx,yy],[yx,yy],[yx,yy]]
#x_text_axis=[[xx,xy],[xx,xy],[xx,xy],[xx,xy],[xx-0.3,xy-0.05],[xx-0.3,xy-0.05]]


num_data_dir=0
for data_obs in data_observation:

    num_data_count=0
    for data_pre in data_predict[num_data_dir]:
        isSave = False
        logger.info('plotting Real vs Predicted Cascade (%s): %s ' % (str_data_type,data_obs+'-'+predict_map[num_data_dir][num_data_count]))
        legend=[data_obs+'-'+predict_map[num_data_dir][num_data_count]]
#        tmp_src_file = dir_data %(str_data_type,data_obs+'_'+data_pre)
        tmp_src_file = dir_data % (data_obs + '_' + data_pre)

        f = open(tmp_src_file, encoding='UTF-8', mode='r', errors='ignore')
        #logger.info(tmp_src_file)
        #sys.exit()
        line =f.readline()
        tmp_values_x=[]
        tmp_values_y=[]
        tmp_values_z=[]
        line_count=0
        r=0
        while line:
            if(line_count==0):
#                words = line.replace('\n', '').split('=')
#                r=float(words[1])
                line_count+=1
                line = f.readline()
                continue
            words = line.replace('\n', '').split('\t')
            tmp_values_x.append(float(words[0]))
            tmp_values_y.append(float(words[1]))
            tmp_values_z.append(float(words[2]))
            line = f.readline()
    #    logger.info(tmp_values_x)
        xlabel = None
        ylabel = None
        x_num_show=True
        y_num_show=True
    #   pf.shaded_Error_Bar_Mean_Error(tmp_values_x,tmp_values_y,tmp_values_err,logx=logx)
#        subplot=int("%s%s%s" % (len(data_observation),len(data_predict[0]), num_data_dir*(len(data_predict[0]))+num_data_count+1))
        subplot="%s,%s,%s" % (len(data_observation),len(data_predict[0]), num_data_dir*(len(data_predict[0]))+num_data_count+1)
        fig_file=""
        #logger.info(subplot)
        if (num_data_dir==len(data_observation)-1 and (num_data_count==len(data_predict[0])-1)):
           isSave=True
           fig_file = (fig_data % (str_data_type))
           xlabel = xlabel_bak
           ylabel = ylabel_bak
        if(num_data_count==0):
            y_num_show = True
        if(num_data_dir==len(data_observation)-1):
            x_num_show = True
        pars=[xlabel,ylabel,1,colors[1],fig_file,legend,num_data_type,x_text_axis,y_text_axis,y_num_show,x_num_show]
        shaded_Error_Bar_Mean_Error_Params_SubPlot_OneCaption(tmp_values_x,tmp_values_y,subplot,tmp_values_z,pars=pars,logx=logx,logy=logy,isSave=isSave)
        f.close()
        num_data_count += 1
       # os._exit(0)
    num_data_dir += 1

sys.exit()