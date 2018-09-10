import numpy as np
from pandas import *
from matplotlib import pyplot as plt
from pylab import *
import time
import logging
import os.path
import seaborn as sns
from IPython.core.pylabtools import figsize
import math

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
#logger.addHandler(fh)


dir="D:\\data\\MAG\\output\\"

src_file = dir+"attention\\attention_%s_%s.txt"
root_file =dir +"RootInfo.txt"
fig_file = dir+"paper_growth_citation_dist\\graph\\attention_no_log_since_%s.png"
#fig_file = dir+"paper_growth_citation_dist\\graph\\attention_since_%s.png"
colors= ['black','bisque','lightgreen','slategrey','lightcoral','gold',
         'c','cornflowerblue','blueviolet','tomato','olivedrab',
         'lightsalmon','sage','lightskyblue','orchid','hotpink',
         'silver', 'slategray', 'indigo', 'darkgoldenrod','orange']


f = open(root_file,encoding='UTF-8', mode='r',errors='ignore')
line =f.readline()
root_info=[]
time_start=time.time()

plt.rcParams['figure.figsize'] = (18, 10)

while line:
    words=line.replace('\n','').split('\t')

    rootid=words[0].strip()
    rootdesc=words[1].strip()

#    root_info.setdefault(rootid, rootdesc)
    root_info.append((rootid, rootdesc))

    line =f.readline()
f.close()

time_end = time.time()
logger.info('Read Roots Done, cost time:%d s', time_end - time_start)
num_root=0

t0=1980
tn=2010

root_info=sorted(root_info,key=lambda x:x[0])
for root in root_info:
    tmp_src_file=src_file % (root[0],t0)
    #print(root[1])
#    logger.info(tmp_src_file)
    f = open(tmp_src_file,encoding='UTF-8', mode='r',errors='ignore')
    line =f.readline()
    x=[]
    y=[]
    N_t=0
    N_t_1=0
    N_0=0
    N_1=0

#    logger.info('plot one root start:%d,,root:%s ,cost time:%d s', num_root,root[0],time_end - time_start)
    while line:

        words = line.replace('\n', '').split('\t')

        year = int(words[0].strip())
        citation= int(words[1].strip())


        if(year<t0 or len(words)==0 or year>tn):
            line = f.readline()
            continue

        if(year ==t0):
            N_0=citation
            N_t += citation
            N_t_1 += citation
            line = f.readline()
            continue
        if(year ==(t0+1)):
            N_1=N_0+citation

        N_t+=citation
#        r = 0
#        logger.info("ROOT:%s,Nt:%d,Nt-1:%d,N1:%d,N0:%d.r:%lf", root[0],N_t, N_t_1, N_1, N_0, r)
        r=(N_t*1.0/N_t_1)/(N_1*1.0/N_0)
#        r = (N_t * 1.0 / N_t_1)
#        r=(math.log2(N_t)-math.log2(N_t_1))/(math.log2(N_1)-math.log2(N_0))

        #if (year == (t0 + 1)):
         #   logger.info("Nt:%d,Nt-1:%d,N1:%d,N0:%d.r:%lf",N_t,N_t_1,N_1,N_0,r)
        N_t_1 += citation

        x.append(year)
        y.append(r)

        line = f.readline()

    plt.plot(x, y, linewidth='1', label=("%s" %  root[1]), color=colors[num_root], linestyle=':', marker='o')
    num_root += 1
    f.close()
   # logger.info('plot one root done:%d,,root:%s ,cost time:%d s', num_root,root[1],time_end - time_start)



#Eq. (13))
'''
alpha=0.25
x=np.arange(t0+1,tn)
y= [ math.exp(-1*alpha*(a-t0-1)) for a in x]
plt.plot(x, y, linewidth='3', label=('y=exp(-%st)' % (alpha)), color=colors[len(colors)-1], linestyle='-', marker='.')

alpha=0.24
y= [ math.exp(-1*alpha*(a-t0-1)) for a in x]
plt.plot(x, y, linewidth='3', label=('y=exp(-%st)' % (alpha)), color=colors[len(colors)-2], linestyle='-', marker='.')

alpha=0.23
y= [ math.exp(-1*alpha*(a-t0-1)) for a in x]
plt.plot(x, y, linewidth='3', label=('y=exp(-%st)' % (alpha)), color=colors[len(colors)-3], linestyle='-', marker='.')

alpha=0.22
y= [ math.exp(-1*alpha*(a-t0-1)) for a in x]
plt.plot(x, y, linewidth='3', label=('y=exp(-%st)' % (alpha)), color=colors[len(colors)-4], linestyle='-', marker='.')

alpha=0.21
y= [ math.exp(-1*alpha*(a-t0-1)) for a in x]
plt.plot(x, y, linewidth='3', label=('y=exp(-%st)' % (alpha)), color=colors[len(colors)-5], linestyle='-', marker='.')
'''
#ax = plt.gca()  # 获取当前图像的坐标轴信息
#ax.yaxis.get_major_formatter().set_powerlimits((0,1)) # 将坐标轴的base number设置为一位。



plt.legend(loc='upper right')
#plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0., handleheight=1.675)
plt.title('Collective Attractiveness',size ='30')
plt.xlabel('Year',size ='30')
plt.ylabel('Attractiveness',size ='30')

#plt.gca().xaxis.set_major_locator(plt.NullLocator())
#plt.gca().yaxis.set_major_locator(plt.NullLocator())
#plt.subplots_adjust(top = 2, bottom = 2, right = 2, left = 20, hspace = 2, wspace = 2)
#plt.margins(0,0)
plt.savefig(fig_file % t0,dpi=400,bbox_inches='tight')
#plt.draw()
#plt.show()
