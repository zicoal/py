#!/usr/bin/python
# coding:utf-8

import os
import logging
import time
import string
from matplotlib import pyplot as plt
import numpy as np


fig_file = "D:\\py\\data\\initialreaction\\figs\\AUC_Single_All.png"


#y=[1,2,3,4,5,6]#给出在y轴上的位置
y=[1,2,3,4,5,6]#给出在y轴上的位置
label=['All','Initial Attention \n(1-hour)  ','Initial Attention \n(30-min)  ','Initial Attention \n(10-min) ','Initial Time','Initial Structure']#直方图信息
colors=['red','pink','tan','orange','blue','green']

x_weibo=[0.923,0.881,0.856,0.772,0.84,0.714]#给出具体每个直方图的数值
subplot = 121
axes = plt.subplot(subplot)
axes.barh(y,x_weibo,color=colors,height=0.5,alpha=0.6,tick_label=label)#绘制水平直方图
plt.title('Weibo')
count=0
y_xis=[0.07,0.24,0.40,0.56,0.73,0.9]
x_shift=0.16
for num in x_weibo:
    if(len(str(x_weibo[count])))<5:
        x_shift = 0.12
    else:
        x_shift = 0.16
    plt.text(x_weibo[count]-x_shift,y_xis[count],str(num), transform=axes.transAxes, color='black')
    count+=1


x_twitter=[0.971,0.964,0.943,0.917,0.898,0.601]#给出具体每个直方图的数值
subplot = 122
label=['','','','','','']#直方图信息
axes = plt.subplot(subplot)
axes.barh(y,x_twitter,color=colors,height=0.5,alpha=0.6,tick_label=label)#绘制水平直方图
plt.title('Twitter')
count=0
for num in x_twitter:
    plt.text(x_twitter[count]-0.2,y_xis[count],str(num), transform=axes.transAxes, color='black')
    count+=1

plt.text(-0.45,-0.13, "Area Under Curve", transform=axes.transAxes,
         color='black', size='13')

#plt.text(-0.45,-0.2, "Area Under Curve", transform=axes.transAxes,
#         color='black', size='10',weight="bold" )

plt.savefig(fig_file, dpi=400, bbox_inches='tight')
#plt.show()#显示图像
