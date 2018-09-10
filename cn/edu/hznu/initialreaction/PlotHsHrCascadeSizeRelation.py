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
import networkx as nx

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

src_weibo_file = dir+"Weibo_RT_2.txt"

fig_file = dir+"output\\Hr_level_size_defualt_all_%s.png"
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

user_hr= defaultdict(str)
hr_index= defaultdict(int)
num_hr=defaultdict(int)
tmp_x1 = []
time_start=time.time()

while line:
#    logger.info(tmp_src_file)
    num_line_count+=1
    if(num_line_count==1):
        line =f.readline()
        continue
    words = line.replace('\n', '').split('\t')
#    Hs = int(words[2].strip())
    Hr = int(words[1].strip())
    id= words[0].strip()
    user_hr[id] = Hr
#    sum_hr[Hr]+=Hs
    if(hr_index.get(Hr) is None):
        hr_index[Hr]=Hr

    if(num_line_count%100000==0):
        logger.info(num_line_count)

    num_hr[Hr]+=1
#    x.append(Hs)
#    y.append(Hr)

    line = f.readline()
f.close()

time_end=time.time()
logger.info("Read H_R Data Done! Time Cost:%d s.", time_end-time_start)

x=[]
#print(hr_index)
#for xi in hr_index:
#    x.append(xi)
#print(x)
#exit()
default_motif_size =5 -1
default_popular_size =500
error_count = 0
num_line_count=0

fig_file = fig_file % (default_motif_size+1)

f_weibo = open(src_weibo_file,encoding='UTF-8', mode='r',errors='ignore')
line =f_weibo.readline()

num_hr_cascade_size= defaultdict(int)
num_hr_level= defaultdict(int)
num_hr_count=defaultdict(int)

while line:
    retweets=line.replace('\n','').split(';')
    num_line_count+=1
    #logger.warn(len(retweets))
    if(len(retweets)<default_motif_size):
        line = f_weibo.readline()
        continue
    t0=0
    num_tweets_count=0
    tmp_retweets=[]

    for ret in retweets:
        one_retweet= ret.split(",")
        t2  = float(one_retweet[3])
        tmp_retweets.append((t2, ret))
    #Reordering the sequence by
    tmp_retweets=sorted(tmp_retweets,key=lambda x:x[0])
    tmp_tweet_num_count=0
    chk_t0=0
    chk_t1=1
    chk_id0=0 #root
    chk_id1=1
    dist_count_list = []

    g = nx.DiGraph()
    g.clear()

    for ret in tmp_retweets:
        one_retweet = ret[1].split(",")
        id1 = one_retweet[0]
        id2 = one_retweet[1]
        t1 = float(one_retweet[2])
        t2 = float(one_retweet[3])

        if tmp_tweet_num_count==0:
            chk_t0=t2
            chk_id0=id1

        elif tmp_tweet_num_count==1:
            chk_t1=t2
            chk_id1=id1
#        elif (tmp_tweet_num_count >= default_motif_size):
#            break
        g.add_edge(id1,id2)
#                graph.add_one_edge(g, id1, id2)
        tmp_tweet_num_count+=1

    if(chk_t0==chk_t1 and chk_id0!=chk_id1):
       # logger.info("%s,%s",tmp_retweets[0],tmp_retweets[1])
        error_count+=1
#    elif(tmp_tweet_num_count>=default_motif_size):
    else:
        for node in g.nodes():
            if node!=chk_id0: #not root
#                dist= nx.shortest_path_length(g,node,chk_id0)
                level = nx.shortest_path_length(g, chk_id0, node)
                hr=user_hr[node]
                num_hr_level[hr]+=level
                num_hr_count[hr]+=1
                num_hr_cascade_size[hr]+=len(tmp_retweets)
#                logger.info("%s -> %s: %d",chk_id0,node,dist)
    line=f_weibo.readline()
    if(num_line_count%10000==0):
        time_end = time.time()
        logger.info("reading lines:%d,Time Cost:%d s",num_line_count,time_end - time_start)
logger.error("error lines:%d/%d",error_count,num_line_count)
time_end=time.time()
logger.info("Read Weibo Data Done! Time Cost:%d s.", time_end-time_start)
f_weibo.close()

#tmp_x1 = sorted(tmp_x1, key=lambda x2: x2[0])



x=[]
y1=[]
y2=[]

for xi in hr_index:
    x.append(xi)
x = sorted(x)
for xi in x:
    y1.append(num_hr_level[xi]*1.0/num_hr_count[xi])
    y2.append(num_hr_cascade_size[xi] * 1.0 / num_hr_count[xi])


fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.plot(x, y1,'o-',label=('Layer vs. $H_R$'),color=colors[1], linewidth='3')
ax1.set_ylabel('Layer',size ='30')
ax1.set_title("Cascade Size and Layer vs. $H_R$")
ax1.set_xlabel('$H_R$',size ='30')
plt.legend(loc=1)

ax2 = ax1.twinx()  # this is the important function
ax2.plot(x, y2,'o-',label=('Cascade Size vs. $H_R$'),color=colors[2], linewidth='3')
ax2.set_ylabel('Cascade Size',size ='30')
plt.legend(loc=3)


#plt.gca().xaxis.set_major_locator(plt.NullLocator())$$
#plt.gca().yaxis.set_major_locator(plt.NullLocator())
#plt.subplots_adjust(top = 2, bottom = 2, right = 2, left = 20, hspace = 2, wspace = 2)
#plt.margins(0,0)

plt.savefig(fig_file,dpi=400,bbox_inches='tight')
#plt.draw()
plt.show()
