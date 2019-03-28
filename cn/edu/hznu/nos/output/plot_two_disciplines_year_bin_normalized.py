# !/usr/bin/python
# coding:utf-8


import json
import os
import logging
import time
import networkx as nx
import numpy as np
from  matplotlib import pyplot as plt
#import matplotlib.patches.ArrowStyle
from pyecharts import Graph
from pyecharts import Style
from pyecharts import Bar
from pyecharts import Line

time_start=time.time()

logger = logging.getLogger()
logger.setLevel(logging.INFO)


# 定义handler的输出格式
#logger to console
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)

#---linux---
#src_dir='/home/zico/data/mag/processed/'
#src_file_papers=src_dir+"discipline_papers.txt"
#src_file_citations=src_dir+"interdispline_citation.txt"

#---win---
src_dir='D:\\py\\cn\\edu\\hznu\\nos\\'
src_file_citations=src_dir+"data\\inter_citation_year.txt"
dest_fig_citation_patten=src_dir+"figs\\%s\\bin=%s\citation_patten_%s_%s_%s_%s.png"

#--linux--
#src_dir='/home/zico/py/cn/edu/hznu/nos/'
#src_file_citations=src_dir+"data/inter_citation_year.txt"
#dest_fig_citation_patten=src_dir+"figs/citation_patten_%s_%s_%s_%s_%s.png"

colors= ['bisque','lightgreen','slategrey','lightcoral','gold',
         'c','cornflowerblue','blueviolet','tomato','olivedrab',
         'lightsalmon','sage','lightskyblue','orchid','hotpink',
         'silver', 'slategray', 'indigo', 'darkgoldenrod','orange']


dict_disciplines_papers_num= {}

#reading disciplines

str_observation_discipline1='physics'
str_observation_discipline2='chemistry'
num_max_papers_ci=0
num_linecount=0

dict_year_discipline_citation={}
dict_disciplines=[]

start_year=1949
end_year=2017
num_bin = 3 #每x年做一次bin

num_top_influence=20  #相互影响最大的前x名

f = open(src_file_citations,encoding='UTF-8', mode='r',errors='ignore')
line =f.readline()
while line:
        words=line.replace('\n','').split('\t')

        str_discipline_cited = words[0].strip()
        str_discipline_citing = words[1].strip()
        if(str_discipline_cited not in dict_disciplines):
            dict_disciplines.append(str_discipline_cited)
        cite_year =  int(words[2].strip())

        cite_year_binned= int((cite_year - start_year) / num_bin) * num_bin + int(num_bin / 2) + start_year

        num_citations =  int(words[3].strip())

        if(cite_year<start_year or cite_year>end_year):
            num_linecount += 1
            line = f.readline()
            continue
        cite_year = cite_year_binned
        if (dict_year_discipline_citation.get(cite_year) is None):
            d1_cited_discipline=dict_year_discipline_citation.setdefault(cite_year,{})
            d1_cited_discipline.setdefault(str_discipline_citing,{})[str_discipline_cited] = num_citations
        else:
            d1_cited_discipline = dict_year_discipline_citation.get(cite_year)
            d1_cited_discipline.setdefault(str_discipline_citing, {})[str_discipline_cited] = num_citations

        num_linecount+=1
        line =f.readline()
time_end = time.time()
logger.info('Reading citations : %d, cost time:%d s', num_linecount, time_end - time_start)
f.close()

#--normalized starts--
##output physics->chemistry and physics<-chemistry
# normalized by sum

list_dicsipline_done=[]
i = 0
for tmp_citing_displine in dict_disciplines:
    if(tmp_citing_displine != str_observation_discipline1):
        continue
    for tmp_cited_displine in dict_disciplines:
        x1 = []
        y1 = []
        x2 = []
        y2 = []
        if ((tmp_cited_displine == tmp_citing_displine) or (tmp_cited_displine in list_dicsipline_done)):
            continue
        i += 1

        tmp_dict_year_impact_1={}
        tmp_dict_year_impact_2={}

        for  keyx, valuex  in dict_year_discipline_citation.items():
            for keyxx, valuexx in valuex.items():
                 if(keyxx==tmp_citing_displine):
                     tmp_sum = 0
                     tmp_target = 0
                     for keyxxx, valuexxx in valuexx.items():
                         tmp_sum += valuexxx
                         if (keyxxx == tmp_cited_displine):
                             tmp_target = valuexxx
                     tmp_dict_year_impact_1.setdefault(keyx,tmp_target * 1.0 / tmp_sum)
#                     x1.append(keyx)
#                     y1.append((tmp_target * 1.0 / tmp_sum))

        for  keyx, valuex  in dict_year_discipline_citation.items():
            for keyxx, valuexx in valuex.items():
                 if(keyxx==tmp_cited_displine):
                     #physics
                     tmp_sum = 0
                     tmp_target = 0
                     for keyxxx, valuexxx in valuexx.items():
                         tmp_sum += valuexxx
                         if (keyxxx == tmp_citing_displine):
                             tmp_target = valuexxx
                     tmp_dict_year_impact_2.setdefault(keyx,tmp_target * 1.0 / tmp_sum)
#                     x2.append(keyx)
#                     y2.append((tmp_target * 1.0 / tmp_sum))

        tmp_dict_year_impact_1 = sorted(tmp_dict_year_impact_1.items(), key=lambda x: x[0])
        tmp_dict_year_impact_2 = sorted(tmp_dict_year_impact_2.items(), key=lambda x: x[0])

        for p in tmp_dict_year_impact_1:
            x1.append(p[0])
            y1.append(p[1])

        for p in tmp_dict_year_impact_2:
            x2.append(p[0])
            y2.append(p[1])

        plt.figure().set_size_inches(8.4, 5.5)
        plt.plot(x1, y1, linewidth='2', label=("%s -> %s" %(tmp_citing_displine.capitalize(),tmp_cited_displine.capitalize())), color=colors[1], linestyle='-', marker='o')
        plt.plot(x2, y2, linewidth='2', label=("%s -> %s" % (tmp_cited_displine.capitalize(),tmp_citing_displine.capitalize())), color=colors[2], linestyle='-', marker='^')
        plt.legend(loc='best')
        plt.title('Citing Pattern (Normalized)',size ='20')
        plt.xlabel('Year',size ='20')
        plt.ylabel('# of Citations',size ='20')
        tmp_dest_fig_citation_patten=dest_fig_citation_patten % ('normalized',num_bin,tmp_citing_displine,tmp_cited_displine,start_year,end_year);
        plt.savefig(tmp_dest_fig_citation_patten)
        #plt.show()
        list_dicsipline_done.append(tmp_citing_displine)
        time_end = time.time()
        logger.info('Plotting %s - %s (Normalized), cost time:%d s', tmp_citing_displine, tmp_cited_displine,time_end - time_start)
logger.info("Total number of figures: %d.",i)
#plt.show()
#--normalized ends--