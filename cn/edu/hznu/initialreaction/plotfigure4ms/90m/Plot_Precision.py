#!/usr/bin/python
# coding:utf-8

import os,sys
import logging
import time
import string
from matplotlib import pyplot as plt
import numpy as np
#from cn.edu.hznu.tools import plotfig as pf
import numpy as np


color_line= ['pink','gray','lightblue']

data_observation=['30m','1h','1.5h']
data_predict=[['1h','12h','1d','final'],\
              ['2h','12h','1d','final'],\
              ['2h','12h','1d','final']]
str_data_type = ["Weibo","Twitter"]

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
    if (pars[0] is not None):
        xlabel = str_data_type[pars[6]]
        xlabel_axis = [0.35,-0.1]
        plt.text(xlabel_axis[0], xlabel_axis[1],  xlabel,transform=axes.transAxes,
             color='black', size='12', weight="light")

    if (isSave==True):
        if (pars[1] is not None):
            ylabel = pars[1]
            ylabel_axis = pars[8]
            plt.text(ylabel_axis[0], ylabel_axis[1],  ylabel, rotation=90, transform=axes.transAxes,
                 color='black', size='12', weight="light")
    '''

    cl=color_line[0]
    error_params = dict(elinewidth=4, ecolor='coral', capsize=5)  # 设置误差标记参数
    labels = []
    #logger.info("%s,%s",len(error),len(error[0]))
    num_count=0
    small=[]
    medium=[]
    large=[]

    for i in range(len(error)):
        small.append(y[i][0])
        medium.append(y[i][1])
        large.append(y[i][2])

    s = []
    m = []
    l = []

    for i in range(len(small)):
        s.append(small[i])
        m.append(medium[i])
        l.append(large[i])
        if i == len(data_predict[0])-1:
            s.append(0)
            m.append(0)
            l.append(0)
        if i == len(data_predict[0])*2-1:
            s.append(0)
            m.append(0)
            l.append(0)
        #            x_ticker.append(tmp_num_head*x_big_width+tmp_num_head+1+ x_small_width*(tmp_num_tail+b))

    labels = ["1h", "12h", "1d",  "final", "", "2h", "12h", "1d",  "final", "", "2h", "12h", "1d", "final"]

    x = np.arange(len(labels))  # 横坐标
    x = np.arange(len(x))  # 首先用第一个的长度作为横坐标


    if(pars[6]==0):
        plt.text(-4,1.12,'B' + pos[2],fontsize=10)
    else:
        plt.text(-3.5,1.12,'B' + pos[2],fontsize=10)



    if (isSave is not True):
        plt.ylabel("Precision",fontsize='9')

    #logger.info("%s, %s, %s: ",tmp_num_head, x_ticker,x[i])
        #sys.exit()
        #logger.info(i)
#    axes.bar(x_ticker, y[i],color=color_line[0],width=1)
#        axes.bar(x_ticker, y[i], yerr=errors[i],color=color_line[1])

    width = 0.3  # 设置柱与柱之间的宽度
    axes.bar(x, s, width, alpha=0.9, color=color_line[0], label='small')
    axes.bar(x + width, m, width, alpha=0.7, color=color_line[1], label='medium')
    axes.bar(x + width * 2, l, width, alpha=0.7, color=color_line[2], label='large')
    axes.set_xticks(x + width / 2)  # 将坐标设置在指定位置
    axes.set_xticklabels(labels)  # 将横坐标替换成
    axes.tick_params(axis='x', tickdir='in', labelsize=5, length=0)
    axes.tick_params(axis='y', tickdir='out', labelsize=7)




    if (isSave == True):
        labels = []
        xlegend = ['Small','Medium','Large']
        plt.legend(xlegend,
                       loc='upper right',
                       fontsize=7,ncol=3,frameon=False, bbox_to_anchor=(1, 1.12))
#    box = axes.get_position()
#    axes.set_position([box.x0, box.y0, box.width, box.height * 0.8])
    #(a-b)
    '''
    xy = plt.axis()
    logger.info(xy)
    x = (xy[0]) +0.5
    y = 1.01
    axes.text(x, y, pars[12], \
              color='black', weight="light", size=7)
#    axes.text(x, y, ("%s %s" % (pars[12], str_data_type[pars[6]])), \
#              color='black', weight="light", size=7)

    '''

    line_start = 0.05
    line_width = 3.5
    line_start_step = 5
    line_v_width_min = -0.1
    line_v_width_max = -0.15

    for i in range(len(data_observation)):
        plt.vlines(line_start + i * line_start_step, line_v_width_min, line_v_width_max)
        plt.vlines(line_start + i * line_start_step + line_width, line_v_width_min, line_v_width_max)
    #    plt.hlines(line_start + i * line_start_step, line_v_width_min, line_v_width_max)
    plt.ylim(0, 1.05)
#    axes.set_xticks(x[0])
    #axes.set_xticklabels(xtickers)

#    plt.xticks(xt,xtickers)
   # if (pars[6] == 1 or pars[6] == 4):
    #    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
    #               wspace=0.3, hspace=0.15)



    if(isSave==True):
        ax = plt.gca()
        #ax.update_datalim(corners)
        plt.savefig(fig_file+ ".png", dpi=200,  bbox_inches='tight')
        plt.savefig(fig_file + ".pdf", format='pdf', dpi=400, bbox_inches='tight')
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

#weibo_axis_motif
logx = False
logy = False
#Weibo
num_data_type = 2
str_fig_type = ["Weibo","Twitter"]

xlabel_bak=None
ylabel_bak='Precision'

data_motif='5'
data_legend=['(a)','(b)']
data_size='200'
data_dist= 2
#dir_data = "D:\\py\\data\\initialreaction\\results\\201911\\Multi-Classification\\Multi_Classification_Precision_Recall\Fig%s&Fig%s\\Fig_Kappa_Case_%s_%s_%s\\precision_%s-%s.txt"

dir_data = "D:\\py\\data\\initialreaction\\results\\201911\\Result_Updata_1.5Hour\\Multi_Classification_Precision_Recall\Fig%s&Fig%s\\Fig_Kappa_Case_%s_%s_%s\\precision_%s-%s.txt"

fig_data = "D:\\py\\data\\initialreaction\\figs\\precision" #e.g.Weibo_200_Kappa

#fig_names = ['%s_vs_1hour_cascade_%s' % (str_feature,str_data_type),'%s_vs_2hour_cascade_%s' % (str_feature,str_data_type),'%s_vs_1day_cascade_%s' % (str_feature,str_data_type), '%s_vs_2day_cascade_%s' % (str_feature,str_data_type), '%s_vs_10day_cascade_%s' % (str_feature,str_data_type),'%s_vs_final_cascade_%s' % (str_feature,str_data_type)]
color_index=0
#colors = [('red','pink'),('blue','lightblue'),('green','lightgreen'),('black','gray')]


xx=-0.9
xy=-0.2
yx=-1.45
#yx=-0.20
yy=0.6

y_text_axis=[yx,yy]
x_text_axis=[xx,xy]


colors = [('red','pink'),('blue','lightblue'),('green','lightgreen'),('black','gray')]

num_data_dir=1
legend=[]
num_data_type=0
data_len=5

for dt in str_data_type:
    x = []
    y = []
    errors = []
    isSave = False
    for num in range(data_dist,data_dist+1):
        logger.info("Plotting Precison %s : %s" % (dt,data_size))

        tmp_num_motif = 0
        tmp_num_fig1 = len(str_data_type)*num_data_type*data_len+(data_dist+1)
        #logger.info('%s,%s,%s', num_data_type, num, tmp_num_fig1)
        tmp_num_fig2 = tmp_num_fig1+1

        legend = str_fig_type[num_data_type]
        isSave = False
        tmp_num_predict=0
        for data_obs in data_observation:

            for data_to_redict in data_predict[tmp_num_predict]:

                tmp_src_file = dir_data % (tmp_num_fig1,tmp_num_fig2, dt, data_motif,data_size,data_obs,data_to_redict)
                logger.info('plotting file : %s ' % tmp_src_file)
               # sys.exit()
                f = open(tmp_src_file, encoding='UTF-8', mode='r', errors='ignore')
                line =f.readline()
                tmp_values_x=[]
                tmp_values_y=[]
                tmp_error=[]
                line_count=0
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
            tmp_num_predict+=1

    xlabel = str_data_type[num_data_type]
    ylabel = None
    x_num_show=True
    y_num_show=True

    subplot="%s,%s,%s" % (2,2, num_data_type+1)
    fig_file=""
    #logger.info(subplot)
    if (num_data_type==len(str_data_type)-1):
       isSave=True
       fig_file = fig_data
#               xlabel = xlabel_bak
#               ylabel = ylabel_bak
       #xlabel = xlabel_bak
       ylabel = ylabel_bak
    pars=[xlabel,ylabel,1,colors[0],fig_file,legend,num_data_type,x_text_axis,y_text_axis,y_num_show,x_num_show,num_data_type,data_legend[num_data_type]]
    shaded_Error_Bar_Mean_Error_Params_SubPlot_OneCaption(x,y,errors, subplot,pars=pars,logx=logx,logy=logy,isSave=isSave)


        #sys.exit()

    #sys.exit()
    num_data_type +=1

sys.exit()