import numpy as np
from pandas import *
from matplotlib import pyplot as plt
from pylab import *
import time
import logging
import os.path
from IPython.core.pylabtools import figsize
import math
from cn.edu.hznu.tools import entropy
from cn.edu.hznu.tools import graph
from collections import defaultdict



#define logger
#logger to console
logger = logging.getLogger()
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)

dir = "D:\\zico's conference & presentation\\201806BOSTON\\ms\\data\\"

#src_weibo_file=dir +"Weibo_RT_2.txt"
src_weibo_file=dir +"Weibo_RT_2.txt"
src_twitter_file=dir +"Twitter_RT_2.txt"
dest_dir=dir +"\\output\\"


f_weibo = open(src_weibo_file,encoding='UTF-8', mode='r',errors='ignore')

line =f_weibo.readline()
time_start=time.time()

default_motif_size =5 -1
default_popular_size =500
error_count = 0
num_line_count=0


while line:
    retweets=line.replace('\n','').split(';')
    num_line_count+=1
    #logger.warn(len(retweets))
    if(len(retweets)<default_motif_size):
        line = f_weibo.readline()
        continue
    g = {}
    t0=0
    num_tweets_count=0
    tmp_retweets=[]
    for ret in retweets:
        one_retweet= ret.split(",")
 #       id1 = one_retweet[0]
 #       id2 = one_retweet[1]
 #       t1  = float(one_retweet[2])
        t2  = float(one_retweet[3])
        tmp_retweets.append((t2, ret))
    #Reordering the sequence by
    tmp_retweets=sorted(tmp_retweets,key=lambda x:x[0])
    tmp_tweet_num_count=0
    chk_t0=0
    chk_t1=1
    chk_id0=0
    chk_id1=1
    dist_count_list = []
    visit_flag = defaultdict(str)
    et=0
    for ret in tmp_retweets:
        one_retweet = ret[1].split(",")
#        logger.warn(ret)
#        logger.warn(one_retweet)
#        logger.warn(ret[1])
#        logger.warn(one_retweet[0])
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
        elif (tmp_tweet_num_count >= default_motif_size):
            break
        if (tmp_tweet_num_count < default_motif_size):
            graph.add_one_edge(g, id1, id2)

        tmp_tweet_num_count+=1

    if(chk_t0==chk_t1 and chk_id0!=chk_id1):
       # logger.info("%s,%s",tmp_retweets[0],tmp_retweets[1])
        error_count+=1
    if(tmp_tweet_num_count>=default_motif_size):
        graph.get_motif_distance_list(g,chk_id0,dist_count_list,0,visit_flag)
        et=entropy.get_entorpy(dist_count_list)
#        logger.error(g)
#        logger.error(et)
#        logger.error(tmp_tweet_num_count)
#        exit()
    line=f_weibo.readline()
logger.error("error lines:%d/%d",error_count,num_line_count)
time_end=time.time()
logger.info("Read Weibo Data Done! Time Cost:%d s.", time_end-time_start)
f_weibo.close()
