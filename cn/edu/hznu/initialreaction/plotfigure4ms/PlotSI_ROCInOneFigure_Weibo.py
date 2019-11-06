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
colors = [('red','pink'),('green','lightgreen'),('blue','lightblue'),('orange','navajowhite'),('purple','orchid'),('black','lightgray')]

def shaded_Error_Bar_Mean_Error_Params_SubPlot_OneCaption(x, y, error, subplot_pos, pars=[], logx=False,logy=False, n=1, isSave=False):
    values_up=[]
    values_down=[]
    num_count=0
#    for x in values_mean:
#        values_up.append(x + n * errors[num_count])
#        values_down.append(x - n * errors[num_count] )
#        num_count+=1


    line_width=2
    fig_file=''
    xlabel=''
    ylabel=''


    pos = subplot_pos.split(',')
    axes = plt.subplot(int(pos[0]), int(pos[1]), int(pos[2]))
    #logger.info(subplot_pos)
    #if (pars[5] is not None):
    #   plt.legend(pars[5],loc='best')

    if (pars[4] is not None):
        fig_file = pars[4]

#    if (pars[3] is not None):
#        colors = pars[3]

    if (pars[2] is not None):
        line_width = pars[2]
    #logger.info(colors)
    #sys.exit()

    #labels
    if (isSave==True):
        if (pars[1] is not None):
            ylabel = pars[1]
            ylabel_axis = pars[9]
#            axes.set_ylabel(ylabel, size='10')
            plt.text(ylabel_axis[0], ylabel_axis[1],  ylabel, rotation=90,
                  color='black', size='12', weight="light")
#            plt.text(ylabel_axis[0], ylabel_axis[1],  ylabel, rotation=90,
#                 family="fantasy", color='black', size='12', weight="light")

        if (pars[0] is not None):
            xlabel = pars[0]
            xlabel_axis = pars[8]
            plt.text(xlabel_axis[0], xlabel_axis[1], xlabel, \
                     color='black', size='12',  weight="bold")
#            plt.text(xlabel_axis[0], xlabel_axis[1], xlabel, \
#                     family="fantasy", color='black', size='12', weight="light")

#    if (pars[10] is not None):

    plt.tick_params(labelsize=5)
    #axes.plot(category, values_mean, linewidth=line_width, color=colors[0])
    #fig

#    axes.plot(category, values_up, colors[1])
#    axes.plot(category, values_down, colors[1])
#    plt.fill_between(category, values_down, values_up, color=colors[0], alpha=0.25)
#    logger.info(values_mean)
#    plt.plot(category, values_mean, linewidth=line_width, color=colors[0])
#    axes.plot(x, y, linewidth=line_width, color=colors[0])

    x_legend = pars[10]
#    logger.info( pars[10])
    #logger.info(len(x_legend))
    for i in range(len(error)):
        color=colors[i]
        axes.errorbar(x[i], y[i], yerr=errors[i], fmt='o:',color =color[1],elinewidth=0.2,ms=1)
    plt.legend(x_legend,
                       loc='lower right',
                       fontsize=5,frameon=False)

    #labels inside
    if (pars[5] is not None):
#        axes.legend(pars[5],loc='upper right')
        pos=pars[7]-4  #the position

        if (pars[6]==1):

            xy=plt.axis()

            x= (xy[1] )*0.01
            y= (xy[3] )*0.9
            axes.text(x,y,pars[5], \
                    family = "fantasy", color = 'black', style = "italic", weight = "light", size=7)
#            axes.text(x,y,pars[5], \
#                    family = "fantasy", color = 'black', style = "italic", weight = "light")

        else:
            axes.text(0.9, 92, pars[5])


  #  print(subplot_pos)

    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                        wspace=0.3, hspace=None)

    if(isSave==True):

        plt.savefig(fig_file, dpi=200,  bbox_inches='tight')
#        plt.savefig(fig_file, dpi=1200,  bbox_inches='tight')
        plt.close('all')


dir_data = "D:\\py\\data\\initialreaction\\results\\201911\\roc\\Prediction_ROC_Weibo\\Fig%s\\Prediction_ROC_Weibo_%s_%s\\%s.txt"
dir_data_single = "D:\\py\\data\\initialreaction\\results\\201911\\roc\\Prediction_ROC_Single_Weibo\\Fig%s\\Prediction_ROC_Single_Feature_Weibo_%s_%s\\%s.txt"
fig_data = "D:\\py\\data\\initialreaction\\figs\\figS11\\%s"
#weibo_axis_motif
logx = False
logy = False
#Weibo
num_data_type = 1
str_data_type = "Weibo"
xlabel_bak='False Postive (%s)'% str_data_type
str_feature="ROC"

fig_dir = ['1','2','3', '4']
data_dir = ['5','6','7', '8', '9', '10']
file_list = ['1h']
file_list_single = ['feature1','feature2','10m','30m','1h']
lenged_auc = ['S:%.3f','T:%.3f','A:%.3f (10m)','A:%.3f (30m)','A:%.3f (1h)','All:%.3f']
fig_names = ['%s_500_%s' % (str_feature,str_data_type),'%s_400_%s' % (str_feature,str_data_type),'%s_300_%s' % (str_feature,str_data_type),'%s_200_%s' % (str_feature,str_data_type)]
ylabel_bak='True Postive'
ylabel=ylabel_bak
xlabel=xlabel_bak
#ylabel=['1-Hour Cascade Size (%s)','2-Hour Cascade Size(%s)','1-Day Cascade Size(%s)','2-Day Cascade Size(%s)','Final Cascade Size(%s)']



#生成几个图，就几个
y_text_axis=[[-3.2,1.4],[-3.2,1.4],[-3.2,1.4],[-3.2,1.4]]
x_text_axis=[[-1.8,-0.2],[-1.8,-0.2],[-1.8,-0.3],[-1.8,-0.3]]

num_data_dir=0

for f_d in fig_dir:
    logger.info('plotting ROC curve: ' + str_data_type + f_d)
    for d in data_dir:

        x = []
        y = []
        errors = []
        isSave = False
        legend_index = 0
        xlegend=[]
        for file in file_list_single:
            tmp_values_x = []
            tmp_values_y = []
            tmp_values_err = []
            tmp_values_auc =0
            tmp_single_src_file = dir_data_single %(f_d,d,f_d,file)
            #logger.info(tmp_single_src_file)
            f = open(tmp_single_src_file, encoding='UTF-8', mode='r', errors='ignore')
            line =f.readline()
            line_count=0
            # read roc single files
            while line:
                if(line_count==0):
                    words = line.replace('\n', '').split('\t')
                   # tmp_values_auc=float(words[1])
                    xlegend.append(lenged_auc[legend_index] % float(words[1]))
                    legend_index +=1
                    line_count+=1
                    line = f.readline()
                    continue
                if (line_count == 1):
                    line_count += 1
                    line = f.readline()
                    continue
                words = line.replace('\n', '').split('\t')
                tmp_values_x.append(float(words[0]))
                tmp_values_y.append(float(words[1]))
                tmp_values_err.append(float(words[2]))
                line = f.readline()
            f.close()
            line=None
            x.append(tmp_values_x)
            y.append(tmp_values_y)
            errors.append(tmp_values_err)

        # read roc integrated files
        for file in file_list:
            tmp_values_x = []
            tmp_values_y = []
            tmp_values_err = []
            tmp_values_auc = []
            tmp_src_file = dir_data % (f_d, d, f_d, file)
            f = open(tmp_src_file, encoding='UTF-8', mode='r', errors='ignore')
            line = f.readline()
            line_count = 0
            while line:
                if (line_count == 0):
                    words = line.replace('\n', '').split('\t')
                    #tmp_values_auc=float(words[1])#
                    xlegend.append(lenged_auc[legend_index] % float(words[1]))
                    legend_index += 1
                    line_count += 1
                    line = f.readline()
                    continue
                if (line_count == 1):
                    line_count += 1
                    line = f.readline()
                    continue
                words = line.replace('\n', '').split('\t')
                tmp_values_x.append(float(words[0]))
                tmp_values_y.append(float(words[1]))
                tmp_values_err.append(float(words[2]))
                line = f.readline()

            x.append(tmp_values_x)
            y.append(tmp_values_y)
            errors.append(tmp_values_err)
            f.close()

        xlabel = None
        legend = "motif=%s" % d

     #   subplot = int("23%s" % (int(d) - 4))
        subplot = "%s,%s,%s" % (2, 3, int(d) - 4)
        #logger.info(subplot)
        fig_file = None
        if d == data_dir[len(data_dir) - 1]:
            isSave = True
            fig_file = (fig_data % fig_names[num_data_dir]) + ".png"
        if (num_data_dir == (len(fig_dir) - 1) or num_data_dir == (len(fig_dir) - 2)):
            xlabel = xlabel_bak
      #  ylabel =None
#            logger.info(tmp_values_y)
        pars = [xlabel, ylabel, 1, colors[1], fig_file, legend, num_data_type, int(d) - 4,
                x_text_axis[num_data_dir], y_text_axis[num_data_dir],xlegend]
        shaded_Error_Bar_Mean_Error_Params_SubPlot_OneCaption(x, y, errors,
                                                              subplot, pars=pars, logx=logx, logy=logy,
                                                              isSave=isSave)

    num_data_dir += 1



    #    logger.info(tmp_values_x)



sys.exit()