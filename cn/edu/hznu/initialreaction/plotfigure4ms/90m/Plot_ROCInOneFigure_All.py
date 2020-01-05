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
    '''
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
                     color='black', size='12',  weight="light")
#            plt.text(xlabel_axis[0], xlabel_axis[1], xlabel, \
#                     family="fantasy", color='black', size='12', weight="light")
    '''
    plt.xlabel(pars[0],fontsize='5')
    if (isSave is not True):
        plt.ylabel(pars[1],fontsize='8')
    #    if (pars[10] is not None):

    plt.tick_params(labelsize=5)
    plt.text(-0.25,1.1,'B' + pos[2],fontsize=10)
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

#            x= -0.01
            #x= (xy[1] )*0.001
            if(isSave==True):
                x=-0.03

            x=0.65
            y=0.5

#            y= (xy[3] )*0.9
            axes.text(x,y,pars[5], \
                    color = 'black', weight = "light", size=7)
            #axes.text(x,y,pars[5], \
             #       family = "fantasy", color = 'black', style = "italic", weight = "light", size=7)

#            axes.text(x,y,pars[5], \
#                    family = "fantasy", color = 'black', style = "italic", weight = "light")

        else:
            axes.text(0.9, 92, pars[5])


  #  print(subplot_pos)

    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                        wspace=0.3, hspace=None)

    if(isSave==True):


        plt.savefig(fig_file+ ".png", dpi=200,  bbox_inches='tight')
        plt.savefig(fig_file + ".pdf", format='pdf', dpi=400, bbox_inches='tight')

        plt.close('all')

dir = "D:\\py\\data\\initialreaction\\results\\201911\\Result_Updata_1.5Hour\\%s"
dir_data =[dir % "Prediction_ROC\\Fig4\\5_200\\%s.txt",\
           dir % "Prediction_ROC\\Fig8\\5_200\\%s.txt"]

dir_data_single =[dir % "Prediction_ROC_Single\\Fig4\\5_200\\%s.txt",\
           dir % "Prediction_ROC_Single\\Fig8\\5_200\\%s.txt"]

'''
dir_data =[dir % "Prediction_ROC_Weibo\\Fig4\\Prediction_ROC_Weibo_5_4\\%s.txt",\
           dir % "Prediction_ROC_Twitter\\Fig4\\5_200\\%s.txt",\
           dir % "Prediction_ROC_Simulation\\Fig4\\Random_5_200\\%s.txt",\
           dir % "Prediction_ROC_Simulation\\Fig8\\Small_World_5_200\\%s.txt",\
           dir % "Prediction_ROC_Simulation\\Fig12\\Scale_Free_5_200\\%s.txt"]

dir_data_single =[dir % "Prediction_ROC_Single_Weibo\\Fig4\\Prediction_ROC_Single_Feature_Weibo_5_4\\%s.txt",\
           dir % "Prediction_ROC_Single_Twitter\\Fig4\\5_200\\%s.txt",\
           dir % "Prediction_ROC_Simulation_Single\\Fig4\\Random_5_200\\%s.txt",\
           dir % "Prediction_ROC_Simulation_Single\\Fig8\\Small_World_5_200\\%s.txt",\
           dir % "Prediction_ROC_Simulation_Single\\Fig12\\Scale_Free_5_200\\%s.txt"]
'''

fig_data = "D:\\py\\data\\initialreaction\\figs\\roc"
#weibo_axis_motif
logx = False
logy = False
#Simulation
num_data_type = 1
str_data_type = "All"
xlabel_bak='False Postive Rate'
str_feature="ROC"

file_list = ['1.5h','1.5h','7','7','7']
file_list_single = [['feature1','feature2','30m','1h','1.5h',],\
                    ['feature2','feature3','30m','1h','1.5h'],\
                    ['feature1','feature2','1m','2m','3m'],\
                    ['feature1','feature2','1m','2m','3m'],\
                    ['feature1','feature2','1m','2m','3m']]
lenged_auc = [
    ['S:%.3f','T:%.3f','A:%.3f (30m)','A:%.3f (60m)','A:%.3f (90m)','All:%.3f'],\
    ['S:%.3f','T:%.3f','A:%.3f (30m)','A:%.3f (60m)','A:%.3f (90m)','All:%.3f'],\
    ['S:%.3f','T:%.3f','A:%.3f (3t)','A:%.3f (5t)','A:%.3f (7t)','All:%.3f'],\
    ['S:%.3f','T:%.3f','A:%.3f (3t)','A:%.3f (5t)','A:%.3f (7t)','All:%.3f'],\
    ['S:%.3f','T:%.3f','A:%.3f (3t)','A:%.3f (5t)','A:%.3f (7t)','All:%.3f']]
ylabel_bak='True Postive Rate'
ylabel=ylabel_bak
xlabel=xlabel_bak
#ylabel=['1-Hour Cascade Size (%s)','2-Hour Cascade Size(%s)','1-Day Cascade Size(%s)','2-Day Cascade Size(%s)','Final Cascade Size(%s)']

#legend_seq = ['(B1) Weibo','(B2) Twitter','(c) RN', '(d) SW', '(e) SF', '(f)']
legend_seq = ['','','(c) RN', '(d) SW', '(e) SF', '(f)']


#生成几个图，就几个
#y_text_axis=[[-3.2,1.4],[-3.2,1.4],[-3.2,1.4],[-3.2,1.4],[-3.2,1.4]]
#x_text_axis=[[-1.8,-0.2],[-1.8,-0.2],[-2.2,-0.3],[-2.2,-0.3],[-3.2,1.4]]

y_text_axis=[[-3.2,1.4],[-1.15,0.4],[-3.2,1.4],[-3.2,1.4],[-3.2,1.3]]
x_text_axis=[[-1.8,-0.2],[-1.8,-0.2],[-2.2,-0.3],[-2.2,-0.3],[-1.3,-0.3]]

num_data_dir=0

l_index = 0
for f_d in dir_data:
    logger.info('plotting ROC curve: ' + str_data_type + f_d)

    x = []
    y = []
    errors = []
    isSave = False
    xlegend=[]
    legend_index=0
    for file in file_list_single[num_data_dir]:
        tmp_values_x = []
        tmp_values_y = []
        tmp_values_err = []
        tmp_values_auc =0
        tmp_single_src_file = dir_data_single[num_data_dir]  % file
       #logger.info(tmp_single_src_file)

        f = open(tmp_single_src_file, encoding='UTF-8', mode='r', errors='ignore')
        line =f.readline()
        line_count=0
        # read roc single files
        while line:
            if(line_count==0):
                words = line.replace('\n', '').split('\t')
               # tmp_values_auc=float(words[1])
                auc=lenged_auc[num_data_dir]
                xlegend.append(auc[legend_index] % float(words[1]))
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
    #for file in file_list:
    tmp_values_x = []
    tmp_values_y = []
    tmp_values_err = []
    tmp_values_auc = []

    tmp_src_file = dir_data[num_data_dir]  % file_list[num_data_dir]

    f = open(tmp_src_file, encoding='UTF-8', mode='r', errors='ignore')
    line = f.readline()
    line_count = 0
    while line:
        if (line_count == 0):
            words = line.replace('\n', '').split('\t')
            auc=lenged_auc[num_data_dir]
            xlegend.append(auc[legend_index] % float(words[1]))
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

    xlabel = xlabel_bak
#   legend = "n=%s" % d
    legend = legend_seq[l_index]
    l_index+=1
    #   subplot = int("23%s" % (int(d) - 4))
    '''
    subplot = "%s,%s,%s" % (3, 2, num_data_dir+1)
    if (num_data_dir == (len(dir_data) - 1)):
        subplot = "%s,%s,%s" % (3,1, 3)
    '''
    subplot = "%s,%s,%s" % (2, 2, num_data_dir+1)
#    if (num_data_dir >1):# (len(dir_data) - 1)):
#        subplot = "%s,%s,%s" % (2,3, num_data_dir+2)
    fig_file = None
    logger.info(subplot)
  #  if num_data_dir == dir_data[len(dir_data) - 1]:
  #      isSave = True
  #      fig_file = fig_data
#    if (num_data_dir == (len(data_dir) - 1) or num_data_dir == (len(data_dir) - 2)):
    if (num_data_dir == (len(dir_data) - 1)):
        xlabel = xlabel_bak
        isSave = True
        fig_file = fig_data
    #ylabel =None
#            logger.info(tmp_values_y)
    pars = [xlabel, ylabel, 1, colors[1], fig_file, legend, num_data_type,  num_data_dir+1,
            x_text_axis[num_data_dir], y_text_axis[num_data_dir],xlegend]
    shaded_Error_Bar_Mean_Error_Params_SubPlot_OneCaption(x, y, errors,
                                                          subplot, pars=pars, logx=logx, logy=logy,
                                                          isSave=isSave)

    num_data_dir += 1



    #    logger.info(tmp_values_x)



sys.exit()