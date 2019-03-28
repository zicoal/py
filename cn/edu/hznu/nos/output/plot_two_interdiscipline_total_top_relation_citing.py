# !/usr/bin/python
# coding:utf-8
# calulate the Top relationships

import json
import os
import logging
import time
import networkx as nx
import numpy as np
from  matplotlib import pyplot as plt
import pandas as pd

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
src_dir='D:\\py\\cn\\edu\\hznu\\nos\\data\\'
src_file_citations=src_dir+"inter_citation_year.txt"
dest_file_citations=src_dir+"inter_citation_weight_all_%s_%s_citing.txt"
dest_file_citations_top=src_dir+"inter_citation_weight_top_%s_%s_%s_citing.txt"

num_top=20

colors= ['bisque','lightgreen','slategrey','lightcoral','gold',
         'c','cornflowerblue','blueviolet','tomato','olivedrab',
         'lightsalmon','sage','lightskyblue','orchid','hotpink',
         'silver', 'slategray', 'indigo', 'darkgoldenrod','orange']


dict_disciplines_papers_num= {}

#reading disciplines

f = open(src_file_citations,encoding='UTF-8', mode='r',errors='ignore')
line =f.readline()
str_observation_discipline1='physics'
str_observation_discipline2='chemistry'
num_max_papers_ci=0
num_linecount=0

begin_year=1949
end_year=2017

dict_discipline_citation={}
dict_discipline_citation_top={}
while line:
        words=line.replace('\n','').split('\t')


        str_discipline_cited = words[0].strip()
        str_discipline_citing = words[1].strip()

        cite_year =  int(words[2].strip())
        num_citations =  int(words[3].strip())

        if(cite_year<begin_year or cite_year>end_year):
            line=f.readline()
            num_linecount += 1
            continue

        #considering citing
        if(dict_discipline_citation.get(str_discipline_citing) is None):
            dict_discipline_citation.setdefault(str_discipline_citing, {})[str_discipline_cited] = num_citations
        else:
            d=dict_discipline_citation.get(str_discipline_citing)
            if(d.get(str_discipline_cited) is None):
                dict_discipline_citation.setdefault(str_discipline_citing, {})[str_discipline_cited] = num_citations
            else:
                dict_discipline_citation[str_discipline_citing][str_discipline_cited] += num_citations

        num_linecount+=1
        line =f.readline()

time_end = time.time()
logger.info('Reading citations : %d, cost time:%d s', num_linecount, time_end - time_start)
f.close()

data=[]
i=0
x_axis =[]
y_axis =[]
dest_file_citations = dest_file_citations % (begin_year,end_year)
dest_file_citations_top = dest_file_citations_top % (num_top,begin_year,end_year)

f_citation = open(dest_file_citations, encoding='UTF-8', mode='w', errors='ignore')
str_scitation=""
for keyx, valuex in dict_discipline_citation.items():
    tmp_sum=0
    for keyxx, valuexx in valuex.items():
        tmp_sum+=valuexx
#        print ("%s\t%s\t%s\n" % (keyx, keyxx, valuexx))
#        exit()
    for keyxx, valuexx in valuex.items():
        str_scitation = str_scitation + ("%s\t%s\t%s\n" % (keyx, keyxx, valuexx*1.0/tmp_sum))
        dict_discipline_citation_top.setdefault("%s\t%s" % (keyx, keyxx),valuexx*1.0/tmp_sum)
f_citation.write(str_scitation)
f_citation.close()

dict_discipline_citation_top = sorted(dict_discipline_citation_top.items(), key=lambda x: x[1],reverse=True)

tmp_count=0
str_scitation=""
f_citation_top = open(dest_file_citations_top, encoding='UTF-8', mode='w', errors='ignore')

for p in dict_discipline_citation_top:
    str_disciplines = p[0].split('\t')
    if (str_disciplines[0].strip()==str_disciplines[1].strip()):
        continue
    else:
        if (tmp_count< num_top):
            tmp_count +=1
            str_scitation = str_scitation + ("%s\t%s\t%.3f\n" % (str_disciplines[0].capitalize(), str_disciplines[1].capitalize(), p[1]))
        else:
            break
f_citation_top.write(str_scitation)
f_citation_top.close()

time_end = time.time()
logger.info('Plotting Physics - Chemistry (Normalized), cost time:%d s', time_end - time_start)
