#!/usr/bin/python
# coding:utf-8

import  pandas  as pd
import  sys,os
import logging
import time
import string
from matplotlib import pyplot as plt
import numpy as np
import xlrd
from matplotlib.ticker import FuncFormatter
import matplotlib.transforms as mtransforms

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

data_dir="d://BaiduNetdiskDownload//报道-日期.txt"
fig="d://BaiduNetdiskDownload///figs//CasesNewsVsDates.png"
fig_cul="d://BaiduNetdiskDownload//figs//CasesNewsVsDates_Culumative.png"

def formatnum(x, pos):
    return '$%.1f$' % (x/10000000)
#    return '$%.1f$x$10^{6}$' % (x/1000000)

dates=[]
cases=[]
news=[]
cases_cul=[]
news_cul=[]

f = open(data_dir, encoding='UTF-8', mode='r', errors='ignore')
line = f.readline()
line_count = 0
while line:
    if (line_count == 0):
        line_count += 1
        line = f.readline()
        continue
    words = line.replace('号', '').replace('\n', '').split('\t')
    logger.info(words)
#    dates.append(int(words[0]))
    dates.append(line_count-1)
    news_cul.append(int(words[2]))
    if (len(words[3])==0):
        words[3]=0
    cases_cul.append(int(words[3]))
    line_count += 1
    line = f.readline()

plt.rcParams['font.sans-serif']=['SimHei']#用来正常显示中文标签
#plt.rcParams['axes.unicode_minus']=False#用来正常显示负号

fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.set_ylabel('累计确诊病例')
legends="累计确诊病例"
lns1=ax1.plot(dates, cases_cul,'r',label=legends)
#plt.legend(legends,loc='upper left',
#                   fontsize=7, ncol=1, frameon=False)
print(dates)
ax1.tick_params(axis='x',labelsize=6)

labels=[]
labels_show=[]
show_interval=4
show_dataes=[]
num_count=0
labels_show.append("%s-%s" % (1, 1))
show_dataes.append(0)

for i in dates:
    num_count+=1
    if(num_count<=31):
        labels.append("%s-%s" % (1,num_count))
        if(num_count % show_interval==0):
            labels_show.append("%s-%s" % (1, num_count))
            show_dataes.append(i)
    elif (num_count <= (31+29)):
        labels.append("%s-%s" % (2, num_count-31))
        if(num_count % show_interval==0):
            labels_show.append("%s-%s" % (2, num_count-31))
            show_dataes.append(i)
    else:
        labels.append("%s-%s" % (3, num_count-(31+29)))
        if (num_count % show_interval == 0):
            labels_show.append("%s-%s" % (3, num_count-(31+29)))
            show_dataes.append(i)

plt.xticks(show_dataes,labels_show)
plt.xlim(1,len(labels))
time_colors=['gray','coral','darkorchid','khaki']
#time_colors=['gray','coral','khaki','darkorchid']
trans = mtransforms.blended_transform_factory(ax1.transData, ax1.transAxes)


plt.fill_between([1,10], 0, 4000, facecolor=time_colors[0], alpha=0.5, transform=trans)
plt.fill_between([10,20], 0, 4000, facecolor=time_colors[1], alpha=0.5, transform=trans)
plt.fill_between([20,60], 0, 4000, facecolor=time_colors[2], alpha=0.5, transform=trans)
plt.fill_between([60,len(labels)], 0, 4000, facecolor=time_colors[3], alpha=0.5, transform=trans)
#plt.fill_between([1,10], 0, 4000, facecolor=time_colors[0], alpha=0.5, transform=trans)

num_height=50000
plt.text(1.5,num_height,"发酵期")
plt.text(11.5,num_height,"初发期")
plt.text(30,num_height,"爆发期")
plt.text(70,num_height,"平稳期")

ax2 = ax1.twinx()  # this is the important function
ax2.set_ylabel('累计信息总数')



formatter = FuncFormatter(formatnum)
ax2.yaxis.set_major_formatter(formatter)
legends="累计信息总数"
lns2=ax2.plot(dates, news_cul,label=legends)

lns = lns1+lns2
labs = [l.get_label() for l in lns]
ax1.legend(lns,labs,loc='upper left',
                   fontsize=7, ncol=1, frameon=False)
#fig.legend(loc='upper left',
#                   fontsize=7, ncol=1, frameon=False,bbox_to_anchor=(1,1), bbox_transform=ax.transAxes)
plt.text(len(labels)+0.2,183000000,"$ \\times 10^7$")
plt.gcf().autofmt_xdate()#自动适应刻度线密度，包括x轴，y轴

ax1.set_title("全国新冠肺炎确诊病例与舆情发展趋势图(截止至%s月%s日)" %(3,len(labels)-31-29))



#ax2.tick_params(labelsize=10)

plt.savefig(fig_cul, dpi=500, bbox_inches='tight')

f.close()
sys.exit()