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

src_file = dir+"paper_growth_citation_dist\\generate\\citation_dist_%s.txt"
root_file =dir +"RootInfo.txt"
fig_file = dir+"paper_growth_citation_dist\\graph\\citation_dist.png"
colors= ['black','bisque','lightgreen','slategrey','lightcoral','gold',
         'c','cornflowerblue','blueviolet','tomato','olivedrab',
         'lightsalmon','sage','lightskyblue','orchid','hotpink',
         'peachpuff', 'slategray', 'indigo', 'darkgoldenrod','orange']


f = open(root_file,encoding='UTF-8', mode='r',errors='ignore')
line =f.readline()
root_info=[]
time_start=time.time()

#
while line:
    words=line.replace('\n','').split('\t')

    rootid=words[0].strip()
    rootdesc=words[1].strip()

    root_info.append((rootid, rootdesc))

    line =f.readline()
f.close()

time_end = time.time()
logger.info('Read Roots Done, cost time:%d s', time_end - time_start)
num_root=0
root_info=sorted(root_info,key=lambda x:x[0])
for root in root_info:
    tmp_src_file=src_file % root[0]
#    logger.info(tmp_src_file)
    f = open(tmp_src_file,encoding='UTF-8', mode='r',errors='ignore')
    line =f.readline()
    x=[]
    y=[]
    while line:
        words = line.replace('\n', '').split('\t')

        degree = words[0].strip()
        prop = words[2].strip()
        d =int(degree)
        if d<100000:
            x.append(degree)
            y.append(prop)

        line = f.readline()

    plt.loglog(x, y, linewidth='1', label=("%s" %  root[1]), color=colors[num_root], linestyle=':', marker='o')
    f.close()
    num_root+=1

#Eq. (11)
'''
A=0.2
tuo=-4
x=np.arange(1,10000)
y= [ A*1.0/a*math.pow(1-math.exp(tuo),a*1.0) for a in x]
plt.loglog(x, y, linewidth='1', label='$alpha$ = 0.75', color=colors[len(colors)-1], linestyle=':', marker='o')
'''

A=0.2
r=0.375
t0=240
alpha=0.75
tuo=(1-math.pow(t0,1-alpha))*r/(1-alpha)
x=np.arange(1,500)
y= [ A*1.0/a*math.pow(1-math.exp(tuo),a*1.0) for a in x]
plt.loglog(x, y, linewidth='3', label='$alpha$ = 0.75', color=colors[len(colors)-1], linestyle='-', marker='.')

'''
A=0.2
t0=230
alpha=0.75
tuo=(1-math.pow(t0,1-alpha))*r/(1-alpha)
x=np.arange(1,500)
y= [ A*1.0/a*math.pow(1-math.exp(tuo),a*1.0) for a in x]
plt.loglog(x, y, linewidth='3', label=('r=%s, t0=%s' % (r,t0)), color=colors[len(colors)-2], linestyle='-', marker='.')


t0=220
alpha=0.75
tuo=(1-math.pow(t0,1-alpha))*r/(1-alpha)
x=np.arange(1,500)
y= [ A*1.0/a*math.pow(1-math.exp(tuo),a*1.0) for a in x]
plt.loglog(x, y, linewidth='3', label=('r=%s, t0=%s' % (r,t0)), color=colors[len(colors)-3], linestyle='-', marker='.')


t0=210
alpha=0.75
tuo=(1-math.pow(t0,1-alpha))*r/(1-alpha)
x=np.arange(1,500)
y= [ A*1.0/a*math.pow(1-math.exp(tuo),a*1.0) for a in x]
plt.loglog(x, y, linewidth='3', label=('r=%s, t0=%s' % (r,t0)), color=colors[len(colors)-4], linestyle='-', marker='.')


t0=190
alpha=0.75
tuo=(1-math.pow(t0,1-alpha))*r/(1-alpha)
x=np.arange(1,500)
y= [ A*1.0/a*math.pow(1-math.exp(tuo),a*1.0) for a in x]
plt.loglog(x, y, linewidth='3', label=('r=%s, t0=%s' % (r,t0)), color=colors[len(colors)-5], linestyle='-', marker='.')

'''
'''
r=0.2
t0=200
alpha=0.5
tuo=(1-math.pow(t0,1-alpha))*r/(1-alpha)
x=np.arange(1,500)
y= [ A*1.0/a*math.pow(1-math.exp(tuo),a*1.0) for a in x]
plt.loglog(x, y, linewidth='3',  label=('r=%s, t0=%s' % (r,t0)),color=colors[len(colors)-2], linestyle=':', marker='.')


r=0.35
t0=500
alpha=0.75
tuo=(1-math.pow(t0,1-alpha))*r/(1-alpha)
x=np.arange(1,500)
y= [ A*1.0/a*math.pow(1-math.exp(tuo),a*1.0) for a in x]
plt.loglog(x, y, linewidth='3',  label=('r=%s, t0=%s' % (r,t0)),color=colors[len(colors)-3], linestyle=':', marker='.')


r=0.35
t0=400
alpha=0.75
tuo=(1-math.pow(t0,1-alpha))*r/(1-alpha)
x=np.arange(1,500)
y= [ A*1.0/a*math.pow(1-math.exp(tuo),a*1.0) for a in x]
plt.loglog(x, y, linewidth='3',  label=('r=%s, t0=%s' % (r,t0)),color=colors[len(colors)-4], linestyle=':', marker='.')

r=0.32
t0=400
alpha=0.75
tuo=(1-math.pow(t0,1-alpha))*r/(1-alpha)
x=np.arange(1,500)
y= [ A*1.0/a*math.pow(1-math.exp(tuo),a*1.0) for a in x]
plt.loglog(x, y, linewidth='3',  label=('r=%s, t0=%s' % (r,t0)),color=colors[len(colors)-5], linestyle=':', marker='.')


r=0.32
t0=250
alpha=0.75
tuo=(1-math.pow(t0,1-alpha))*r/(1-alpha)
x=np.arange(1,500)
y= [ A*1.0/a*math.pow(1-math.exp(tuo),a*1.0) for a in x]
plt.loglog(x, y, linewidth='3',  label=('r=%s, t0=%s' % (r,t0)),color=colors[len(colors)-6], linestyle=':', marker='.')

r=0.35
t0=300
alpha=0.75
tuo=(1-math.pow(t0,1-alpha))*r/(1-alpha)
x=np.arange(1,500)
y= [ A*1.0/a*math.pow(1-math.exp(tuo),a*1.0) for a in x]
plt.loglog(x, y, linewidth='3',  label=('r=%s, t0=%s' % (r,t0)),color=colors[len(colors)-7], linestyle=':', marker='.')
'''

plt.legend(loc='upper right')
#plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0., handleheight=1.675)
plt.title('Citation Distribution',size ='30')
plt.xlabel('# of Citations',size ='30')
plt.ylabel('Proportion',size ='30')

#plt.gca().xaxis.set_major_locator(plt.NullLocator())
#plt.gca().yaxis.set_major_locator(plt.NullLocator())
#plt.subplots_adjust(top = 2, bottom = 2, right = 2, left = 20, hspace = 2, wspace = 2)
#plt.margins(0,0)

plt.savefig(fig_file,dpi=400,bbox_inches='tight')
#plt.savefig(fig_file)
#plt.draw()
#plt.show()
