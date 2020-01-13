#!/usr/bin/python
# coding:utf-8

import os,sys
import logging
import time
import string
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


fig_file = "D:\\py\\data\\initialreaction\\figs\\fig2-1"
#fig_file = "D:\\py\\data\\initialreaction\\figs\\AUC_Single_No_All"


#y=[1,2,3,4,5,6]#给出在y轴上的位置
y=[0.3,0.5,0.7,0.9,1.1]#给出在y轴上的位置
h=0.1
label1=['Initial Structure','Initial Time','Initial Attention (30m)',]#直方图信息
label2=['Initial Attention (60m)','Initial Attention (90m)']#直方图信息
#label=['Initial Attention \n(90-min)  ','Initial Attention \n(60-min)  ','Initial Attention \n(30-min) ','Initial Time','Initial Structure']#直方图信息
colors=['tomato','tan','orange','skyblue','limegreen']
colors1=['limegreen','skyblue','orange']
colors2=['tan','tomato']


#x_weibo=[0.917,0.881,0.836,0.759,0.817,0.727]#给出具体每个直方图的数值_10min
x_weibo=[0.897,0.88,0.848,0.829,0.734]#给出具体每个直方图的数值_90min
#x_weibo=[0.909,0.876,0.886,0.808,0.821,0.761]#给出具体每个直方图的数值 500
#x_weibo=[0.923,0.881,0.856,0.772,0.84,0.714]#给出具体每个直方图的数值
subplot = 221
axes = plt.subplot(subplot)
label=['','','','','']#直方图信息
axes.barh(y,x_weibo,color=colors,height=h,alpha=0.6,tick_label=label)#绘制水平直方图
#axes.barh(y,x_weibo,color=colors,height=h,alpha=0.6)#绘制水平直方图


plt.text(-0.15,1.25,'A1',fontsize=10)
count=0
y_xis=[0.08,0.28,0.49,0.68,0.895]
x_shift=0.16
for num in x_weibo:
    if(len(str(x_weibo[count])))<5:
        x_shift = 0.1
    else:
        x_shift = 0.12
    plt.text(x_weibo[count]-x_shift,y_xis[count]-0.018,str(num), transform=axes.transAxes, fontsize='small', color='black')
    count+=1

plt.xlabel("Area Under Curve",fontsize=6)
#plt.tick_params(axis='y',labelsize=8)
plt.tick_params(labelsize=7)

patches = [mpatches.Patch(color=colors1[i], label="{:s}".format(label1[i]) ) for i in range(len(colors1)) ]
ax=plt.gca()
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width , box.height* 0.8])
plt.legend(handles=patches,  loc='upper left',  fontsize=4.5, ncol=3, bbox_to_anchor=(-0.02, 1.12), frameon=False)

#x_twitter=[0.968,0.95,0.917,0.907,0.855,0.564]#给出具体每个直方图的数值10-min
x_twitter=[0.972,0.968,0.947,0.861,0.529]#给出具体每个直方图的数值90-min
subplot = 222

axes = plt.subplot(subplot)
axes.barh(y,x_twitter,color=colors,height=h,alpha=0.6,tick_label=label)#绘制水平直方图
#plt.title('A2',fontsize=10)
#plt.text(-0.15,1.25,'A2',fontsize=10, fontweight='semibold')
plt.text(-0.15,1.25,'A2',fontsize=10)
count=0


for num in x_twitter:
    if(len(str(x_twitter[count])))<5:
        x_shift = 0.17
    else:
        x_shift = 0.18
    plt.text(x_twitter[count]-x_shift,y_xis[count]-0.018,str(num), transform=axes.transAxes, fontsize='small', color='black')
#    plt.text(x_twitter[count]-x_shift,y_xis[count],str(num), transform=axes.transAxes, color='black')
    count+=1
plt.xlabel("Area Under Curve",fontsize=6)
plt.tick_params(labelsize=7)

#plt.text(-0.45,-0.13, "Area Under Curve", transform=axes.transAxes,
#         color='black', size='13')

#plt.text(-0.45,-0.2, "Area Under Curve", transform=axes.transAxes,
#         color='black', size='10',weight="bold" )

patches = [mpatches.Patch(color=colors2[i], label="{:s}".format(label2[i]) ) for i in range(len(colors2)) ]
ax=plt.gca()
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width , box.height* 0.8])
plt.legend(handles=patches,  loc='upper left',  fontsize=4.5, ncol=3, bbox_to_anchor=(0.0, 1.12), frameon=False)

plt.savefig(fig_file + ".png", dpi=200, bbox_inches='tight')
plt.savefig(fig_file + ".pdf", format='pdf', dpi=600, bbox_inches='tight')
#plt.savefig(fig_file, dpi=400, bbox_inches='tight')
#plt.show()#显示图像

sys.exit()
