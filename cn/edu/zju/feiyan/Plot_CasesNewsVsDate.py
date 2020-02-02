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

data_dir="d://BaiduNetdiskDownload//肺炎相关数据//results//报道-日期.txt"
fig="d://BaiduNetdiskDownload//肺炎相关数据//figs//CasesNewsVsDates.png"
fig_cul="d://BaiduNetdiskDownload//肺炎相关数据//figs//CasesNewsVsDates_Culumative.png"

def formatnum(x, pos):
    return '$%.1f$' % (x/1000000)
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
    words = line.replace('\n', '').split('\t')
    logger.info(words)
    dates.append(int(words[0])+1)
#    dates.append("1-%s" % (int(words[0])+1))
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

labels=["1-%s" % (int(i)) for i in dates]
plt.xticks(dates,labels)
plt.xlim(1,len(labels))
time_colors=['gray','coral','khaki','skyblue']
trans = mtransforms.blended_transform_factory(ax1.transData, ax1.transAxes)


plt.fill_between([1,10], 0, 4000, facecolor=time_colors[0], alpha=0.5, transform=trans)
plt.fill_between([10,20], 0, 4000, facecolor=time_colors[1], alpha=0.5, transform=trans)
plt.fill_between([20,len(labels)], 0, 4000, facecolor=time_colors[2], alpha=0.5, transform=trans)
#plt.fill_between([1,10], 0, 4000, facecolor=time_colors[0], alpha=0.5, transform=trans)

num_height=6000
plt.text(4.5,num_height,"发酵期")
plt.text(13.5,num_height,"初发期")
plt.text(24,num_height,"爆发期")

ax2 = ax1.twinx()  # this is the important function
ax2.set_ylabel('累计舆情总数')



formatter = FuncFormatter(formatnum)
ax2.yaxis.set_major_formatter(formatter)
legends="累计舆情总数"
lns2=ax2.plot(dates, news_cul,label=legends)

lns = lns1+lns2
labs = [l.get_label() for l in lns]
ax1.legend(lns,labs,loc='upper left',
                   fontsize=7, ncol=1, frameon=False)
#fig.legend(loc='upper left',
#                   fontsize=7, ncol=1, frameon=False,bbox_to_anchor=(1,1), bbox_transform=ax.transAxes)
plt.text(len(labels)+0.2,7800000,"$ \\times 10^6$")
plt.gcf().autofmt_xdate()#自动适应刻度线密度，包括x轴，y轴

ax1.set_title("全国确诊病例与舆情发展趋势图(截止至%s月%s日)" %(1,len(labels)))



#ax2.tick_params(labelsize=10)

plt.savefig(fig_cul, dpi=500, bbox_inches='tight')

f.close()
sys.exit()