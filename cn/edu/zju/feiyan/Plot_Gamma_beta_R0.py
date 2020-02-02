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

data_beta="d://BaiduNetdiskDownload//肺炎相关数据//results//gamma-beta.txt"
data_r0="d://BaiduNetdiskDownload//肺炎相关数据//results//gamma-r0.txt"
fig_file="d://BaiduNetdiskDownload//肺炎相关数据//figs//gamma_beta_r0.png"

def formatnum(x, pos):
    return '$%.1f$' % (x/1000000)
#    return '$%.1f$x$10^{6}$' % (x/1000000)

gamma1=[]
beta=[[],[],[]]
style=["o","*","v","p","D"]
gamma2=[]
r0=[[],[],[],[]]
legends=[]
f = open(data_beta, encoding='UTF-8', mode='r', errors='ignore')
line = f.readline()
line_count = 0

while line:
    words = line.replace('\n', '').split('\t')
#    logger.info(words)
    if (line_count == 0):
        tmp_count=0
        for word in words:
            tmp_count+=1
            if tmp_count % 2==0:
                legends.append(word)
    else:
        tmp_count = 0
        for word in words:
            tmp_count += 1
            tmp_xb=tmp_count % 2
            tmp_sb=tmp_count // 2-1
            if tmp_xb == 0:
                #print("tmp_sb/tmp_count:%s,%s" % (tmp_sb,tmp_count))
                beta[tmp_sb].append(float(word))
            elif tmp_count ==1:
                gamma1.append(float(word))

    line_count += 1
    line = f.readline()
f.close()

#print(gamma1)
#print(beta)

plt.rcParams['font.sans-serif']=['SimHei']#用来正常显示中文标签
#plt.rcParams['axes.unicode_minus']=False#用来正常显示负号


#fig = plt.figure()

ax = plt.subplot(121)
ax.set_ylabel("有效传染率($ \\beta_c / \\mu $)")

tmp_count=0
for betas in beta:
    ax.plot(gamma1, betas,lw=2,marker=style[tmp_count])
    tmp_count+=1

plt.legend(legends,loc='upper right',
                   fontsize=9, ncol=1, frameon=False)
plt.xlabel("采取自我保护措施的概率($ \\gamma $)")
plt.text(-0.35,0.0875,"A",fontsize=15,fontweight="bold")



legends=[]
f = open(data_r0, encoding='UTF-8', mode='r', errors='ignore')
line = f.readline()
line_count = 0
while line:
    line = line.replace("SU","S$ ^{U} $").replace("SA","S$ ^{A} $")
    words = line.replace('N', '').replace('\n', '').split('\t')
#    logger.info(words)
    if (line_count == 0):
        tmp_count=0
        for word in words:
            tmp_count+=1
            if tmp_count % 2==0:
                legends.append("%s,%s" % (words[tmp_count-2],words[tmp_count-1]) )
    else:
        tmp_count = 0
        for word in words:
            tmp_count += 1
            tmp_xb=tmp_count % 2
            tmp_sb=tmp_count // 2-1
            if tmp_xb == 0:
                #print("tmp_sb/tmp_count:%s,%s" % (tmp_sb,tmp_count))
                r0[tmp_sb].append(float(word))
            elif tmp_count ==1:
                gamma2.append(float(word))

    line_count += 1
    line = f.readline()

f.close()
logger.info(legends)
logger.info(gamma2)
logger.info(r0)
#sys.exit()
ax2 = plt.subplot(122)
ax2.set_ylabel("基本再生数($ R_{0} $)")
plt.xlabel("采取自我保护措施的概率($ \\gamma $)")
tmp_count=0
for r01 in r0:
    ax2.plot(gamma2, r01,lw=2,marker=style[tmp_count])
    tmp_count+=1

plt.legend(legends,loc='upper left',
                   fontsize=9, ncol=1, frameon=False)
plt.xlabel("采取自我保护措施的概率($ \\gamma $)")
plt.text(-0.35,2.98,"B",fontsize=15,fontweight="bold")

'''
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
'''
plt.xlim(-0.05,1.05)
xy=plt.axis()
newticks1 = np.arange(-5,105)
x=[i/100.0 for i in newticks1]
y=[1 for i in x]
time_colors=['gray','coral','khaki','skyblue']
#trans = mtransforms.blended_transform_factory(ax2.transData, ax2.transAxes)
ax2.plot(x,y,ls=':',color="purple",lw=3)
#logger.info(xy)
#plt.fill_between([xy[0],xy[1]], 0, 1, facecolor=time_colors[0], alpha=0.5, transform=trans)
#plt.fill_between([xy[0],xy[1]], 1, 3, facecolor=time_colors[3], alpha=0.5, transform=trans)
#plt.fill_between([1,10], 0, 4000, facecolor=time_colors[0], alpha=0.5, transform=trans)

'''
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

'''
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                    wspace=0.36, hspace=0.15)

#plt.show()
plt.savefig(fig_file, dpi=600, bbox_inches='tight')
sys.exit()