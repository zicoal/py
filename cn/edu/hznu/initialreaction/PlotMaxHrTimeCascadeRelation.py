import numpy as np
from pandas import *
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

from pylab import *
import time
import logging
import os.path
import seaborn as sns
from IPython.core.pylabtools import figsize
from collections import defaultdict
import networkx as nx
from cn.edu.hznu.tools import common as cm

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

src_file = dir+"hr.txt"

src_weibo_file = dir+"Weibo_RT_2.txt"

fig_file = dir+"output\\Hr_time_size_max_%s.png"
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
user_top_hr_index= defaultdict(str)
hr_index= defaultdict(int)
num_hr=defaultdict(int)
tmp_hr = []
time_start=time.time()

while line:
#    logger.info(tmp_src_file)
    num_line_count+=1
#    if(num_line_count==1):
#        line =f.readline()
#        continue
    words = line.replace('\n', '').split('\t')
#    Hs = int(words[2].strip())
    id= words[0].strip()
    Hr = int(words[1].strip())
    user_hr[id] = Hr

    tmp_hr.append((id,Hr))
#    sum_hr[Hr]+=Hs

    if(num_line_count%100000==0):
        logger.info(num_line_count)

    num_hr[Hr]+=1
#    x.append(Hs)
#    y.append(Hr)

    line = f.readline()
f.close()

time_end=time.time()
logger.info("Read H_R Data Done! Time Cost:%d s.", time_end-time_start)

#tmp_hr.append((Hr, Hr))


tmp_hr = sorted(tmp_hr, key=lambda b: b[1], reverse=True)

num_top_hr=1200#0.001*len(tmp_hr)
tmp_num_top_hr=0
min_hr=1000000
for xi in tmp_hr:
    tmp_num_top_hr+=1
#    if (hr_index.get(xi[1]) is None):
#        hr_index[xi[1]] = xi[1]
    user_top_hr_index[xi[0]]= xi[1]
    if(min_hr>xi[1]):
        min_hr=xi[1]
    if(tmp_num_top_hr>num_top_hr):
        break
    '''
    if (hr_index.get(xi[1]) is None):
        hr_index[xi[1]] = xi[1]
    if(min_hr>xi[1]):
        min_hr=xi[1]
    if(tmp_num_top_hr>num_top_hr):
        break
    '''
print(min_hr)

#print(tmp_num_top_hr)
#exit()

'''
print('----')
print(len(tmp_hr))
print(num_top_hr)
print(len(hr_index))
print(len(tmp_hr))
exit()
'''
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

fig_file = fig_file % (default_popular_size)

f_weibo = open(src_weibo_file,encoding='UTF-8', mode='r',errors='ignore')
line =f_weibo.readline()

num_hr_cascade_size= defaultdict(int)
num_hr_level= defaultdict(int)
num_hr_count=defaultdict(int)
list_hr_cascade_size={}#defaultdict(int)
list_hr_level= {}#defaultdict(int)

max_retweet_size=0
max_retweet_size_by_node=0
max_retweet_count=0
while line:
    retweets=line.replace('\n','').split(';')
    if len(retweets)>max_retweet_size:
        max_retweet_size =  len(retweets)
    num_line_count+=1
    #logger.warn(len(retweets))
    if(num_line_count%10000==0):
        time_end = time.time()
        logger.info("reading lines:%d,Time Cost:%d s",num_line_count,time_end - time_start)
    if(len(retweets)<default_popular_size):
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
   # print(tmp_retweets)
   # exit()
    tmp_tweet_num_count=0
    chk_t0=0
    chk_t1=1
    chk_id0=0 #root
    chk_id1=1
 #   dist_count_list = []

    g = nx.DiGraph()
    g.clear()

    nodes_appearance = defaultdict(str)
    nodes_sequence = []

    hr_first_arrival_time= defaultdict(str)

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
#        if(hr_first_arrival_time.get(id2) is None):
#            hr_first_arrival_time[id]=t2
        if(nodes_appearance.get(id2) is None):
            nodes_sequence.append((id2,t2))
            nodes_appearance[id2]=t2
#                graph.add_one_edge(g, id1, id2)
        tmp_tweet_num_count+=1

#    print(nodes_sequence)
    nodes_sequence=sorted(nodes_sequence,key=lambda x:x[1], reverse=False)
#   print(nodes_sequence)
    if(chk_t0==chk_t1 and chk_id0!=chk_id1):
       # logger.info("%s,%s",tmp_retweets[0],tmp_retweets[1])
        error_count+=1
#    elif(tmp_tweet_num_count>=default_motif_size):
    else:
        max_hr=0
        tmp_level=0.0

        for node in nodes_sequence:
            if node[0]!=chk_id0: #not root
#                dist= nx.shortest_path_length(g,node,chk_id0)
                if( not user_top_hr_index.get(node[0]) is  None):
                    hr=user_top_hr_index.get(node[0])
                    if(hr>max_hr):
#                        level = nx.shortest_path_length(g, chk_id0, node[0])+1
                        level = nodes_appearance[node[0]]-chk_t0 ##actually, this level is time
                        max_hr = hr
                        tmp_level = level
#                        max_retweet_count+=1
#                        if(max_retweet_size_by_node<len(retweets)):
#                            max_retweet_size_by_node= len(retweets)
        if max_hr>0:
            list_hr_level.setdefault(max_hr, []).append(tmp_level)
            list_hr_cascade_size.setdefault(max_hr, []).append(len(retweets))
                    #logger.warn("%s/%s,%d,%d",chk_id0,node[0],hr,max_retweet_size_by_node)
                    #break
#                logger.info("%s -> %s: %d",chk_iidd0,node,dist)
    line=f_weibo.readline()
logger.error("error lines:%d/%d",error_count,num_line_count)
#logger.error("all number of hr:%d",max_retweet_count)
time_end=time.time()
logger.info("Read Weibo Data Done! Time Cost:%d s.", time_end-time_start)
logger.info("max_retweet_size: %d,max_retweet_size_by_node:%d",max_retweet_size,max_retweet_size_by_node)
f_weibo.close()

#tmp_x1 = sorted(tmp_x1, key=lambda x2: x2[0])



x=[]
y1=[]
y2=[]
y1_error=[]
y2_error=[]

for xi in list_hr_level.items():
    x.append(xi[0])
x = sorted(x)
result_hr_level= cm.get_mean_std(list_hr_level)
result_hr_cascade_size= cm.get_mean_std(list_hr_cascade_size)
for xi in x:
#    y1.append(np.sum(list_hr_level[xi]))
#    y2.append(np.sum(list_hr_cascade_size[xi]))
    y1.append(result_hr_level[xi][0])
    y2.append(result_hr_cascade_size[xi][0])
    y1_error.append(result_hr_level[xi][1])
    y2_error.append(result_hr_cascade_size[xi][1])
#y1.append(num_hr_level[xi] * 1.0 / num_hr_count[xi])
#y2.append(num_hr_cascade_size[xi] * 1.0 / num_hr_count[xi])

#fig = plt.figure()

ax1 = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)

ax1.semilogx(x, y1,'o-',label=('$\Delta t$'),color=colors[1], linewidth='2')
ax1.errorbar(x, y1, yerr=y1_error, fmt='-o',color=colors[1])
ax1.set_ylabel(' Retweeing Time',size ='50')
ax1.set_title("Cascade Size (>%s) and Retweeing Time vs. $H_R$" % default_popular_size)
ax1.set_xlabel('$H_R$',size ='50')
ax1.set_xlim(5, 105)

ax2 = ax1.twinx()  # this is the important function
ax2.semilogx(x, y2,'o-',label=('Cascade Size'),color=colors[3], linewidth='2')
ax2.errorbar(x, y2, yerr=y2_error, fmt='-o',color=colors[3])
ax2.set_ylabel('Cascade Size',size ='50')
ax2.set_xlim(5, 105)
#ax1.legend(loc="upper right")
ax1.legend(loc="best")


#plt.gca().xaxis.set_major_locator(plt.NullLocator())$$
#plt.gca().yaxis.set_major_locator(plt.NullLocator())
#plt.subplots_adjust(top = 2, bottom = 2, right = 2, left = 20, hspace = 2, wspace = 2)
#plt.margins(0,0)

plt.savefig(fig_file,dpi=400,bbox_inches='tight')
#plt.draw()
plt.show()

