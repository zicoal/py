import numpy as np
from pandas import *
from matplotlib import pyplot as plt
from pylab import *
import time
import logging
import os.path
import seaborn as sns
from IPython.core.pylabtools import figsize
from collections import defaultdict

#insert paper into db
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
dir = "D:\\zico's conference & presentation\\201806BOSTON\\ms\\data\\"

src_file = dir+"Hs_Hr.txt"
fig_file = dir+"output\\Hs_hr_log.png"
colors= ['black','bisque','lightgreen','slategrey','lightcoral','gold',
         'c','cornflowerblue','blueviolet','tomato','olivedrab',
         'lightsalmon','sage','lightskyblue','orchid','hotpink',
         'silver', 'slategray', 'indigo', 'darkgoldenrod','orange']

plt.rcParams['figure.figsize'] = (10, 8)

f = open(src_file,encoding='UTF-8', mode='r',errors='ignore')
line= f.readline()

x = []
y = []

num_line_count=0

x1= defaultdict(int)
y1= defaultdict(int)
num=defaultdict(int)
tmp_x1 = []
while line:
#    logger.info(tmp_src_file)
    num_line_count+=1
    if(num_line_count==1):
        line =f.readline()
        continue
    words = line.replace('\n', '').split('\t')
    Hs = int(words[2].strip())
    Hr = int(words[1].strip())

    #x.append(math.log10(Hs))
    #y.append(math.log10(Hr))

    if(num_line_count%100000==0):
        logger.info(num_line_count)

#    if(x1.get(Hs) is None):
#        x1[Hs]= Hs
#        y1[Hs] = Hr
#    else:
    if (x1.get(Hs) is None):
        x1[Hs]= Hs
        tmp_x1.append((Hs,Hs))
    y1[Hs] += Hr

    num[Hs]+=1
#    x.append(Hs)
#    y.append(Hr)

    line = f.readline()
f.close()
tmp_x1 = sorted(tmp_x1, key=lambda x2: x2[0])
for i in tmp_x1:
#    x.append(i[0])
#    y.append(y1[i[0]]*1.0/num[i[0]])
    x.append(math.log10(i[0]))
    y.append(math.log10(y1[i[0]]*1.0/num[i[0]]))

#plt.loglog(x, y, linewidth='1', label=("Hs Hr Relationship"), color=colors[1], linestyle=':', marker='o')
#plt.loglog(x, y,  label=("Hs Hr Relationship"), color=colors[1], marker='ro')
#plt.loglog(x, y,  label=("Hs Hr Relationship"))
plt.plot(x, y,  'om',label=("$H_S$ vs. $H_R$ Relationship"))

A=1
slope=0.6
x2=[]
k=0
for i in x:
    k+=1
    if k<5:
        continue
    if k> 50:
        break
    x2.append(i)
#y2= [A*slope*a for a in x2]
#plt.plot(x2, y2,  '-',label=('slope=%s' % slope), color=colors[0], linewidth='5')
#plt.loglog(x1, y1, linewidth='3', label=('slope=%s' % slope), color=colors[0], linestyle='-', marker='.')

A=1
#slope=0.7
#y2= [A*slope*a for a in x2]
#plt.plot(x2, y2,  '-',label=('slope=%s' % slope), color=colors[1], linewidth='5')

A=-0.25
slope=0.9
y2= [A+slope*a for a in x2]
plt.plot(x2, y2,  '-',label=('slope=%s' % slope), color=colors[0], linewidth='5')
#fig = plt.figure(1, (10, 6))
#plt.figure(figsize=(12,6))
#ax = plt.gca()  # 获取当前图像的坐标轴信息
#ax.yaxis.get_major_formatter().set_powerlimits((0,1)) # 将坐标轴的base number设置为一位。



plt.legend(loc='upper left')
#plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0., handleheight=1.675)
#plt.title('Temporal Growth Pattern',size ='30')
plt.xlabel('log($H_S$)',size ='30')
plt.ylabel('log($H_R$)',size ='30')

#plt.gca().xaxis.set_major_locator(plt.NullLocator())$$
#plt.gca().yaxis.set_major_locator(plt.NullLocator())
#plt.subplots_adjust(top = 2, bottom = 2, right = 2, left = 20, hspace = 2, wspace = 2)
#plt.margins(0,0)

plt.savefig(fig_file,dpi=400,bbox_inches='tight')
#plt.draw()
#plt.show()
