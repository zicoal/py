

#!/usr/bin/python
# coding:utf-8

import os,sys
import logging
import time
import string
from matplotlib import pyplot as plt
import numpy as np


fig_file = "D:\\py\\data\\initialreaction\\figs\\AUC_Single_All"


#y=[1,2,3,4,5,6]#给出在y轴上的位置
y=[1,2,3,4,5,6]#给出在y轴上的位置
label=['All','Initial Attention \n(90-min)  ','Initial Attention \n(60-min)  ','Initial Attention \n(30-min) ','Initial Time','Initial Structure']#直方图信息
colors=['red','tomato','tan','orange','skyblue','limegreen']


#x_weibo=[0.917,0.881,0.836,0.759,0.817,0.727]#给出具体每个直方图的数值_10min
x_weibo=[0.919,0.897,0.88,0.848,0.829,0.734]#给出具体每个直方图的数值_90min
#x_weibo=[0.909,0.876,0.886,0.808,0.821,0.761]#给出具体每个直方图的数值 500
#x_weibo=[0.923,0.881,0.856,0.772,0.84,0.714]#给出具体每个直方图的数值
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


#x_twitter=[0.968,0.95,0.917,0.907,0.855,0.564]#给出具体每个直方图的数值10-min
x_twitter=[0.974,0.972,0.968,0.947,0.861,0.529]#给出具体每个直方图的数值90-min
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

plt.savefig(fig_file + ".png", dpi=200, bbox_inches='tight')
plt.savefig(fig_file + ".pdf", format='pdf', dpi=400, bbox_inches='tight')
#plt.savefig(fig_file, dpi=400, bbox_inches='tight')
#plt.show()#显示图像

sys.exit()