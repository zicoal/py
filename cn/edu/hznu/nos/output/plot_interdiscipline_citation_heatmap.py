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
from pyecharts import HeatMap
import seaborn as sns
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

style = Style(
    title_color="#000",
    title_pos="center",
    width=1300,
    height=800,
#    background_color='#404a59'
)
#---win---
src_dir='D:\\py\\cn\\edu\\hznu\\nos\\data\\'
src_file_citations=src_dir+"inter_citation_year.txt"
dest_file_citations=src_dir+"inter_citation_weight_all.txt"


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

dict_discipline_citation={}
while line:
        words=line.replace('\n','').split('\t')

        str_discipline_cited = words[0].strip()
        str_discipline_citing = words[1].strip()

        cite_year =  int(words[2].strip())
        num_citations =  int(words[3].strip())

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
f_citation.write(str_scitation)
f_citation.close()

#heatmap = HeatMap()
#heatmap.add(
    #    "Full Map of Interdiscipline",
    #x_axis,
    #y_axis,
    #data,
    #is_visualmap=True,
    #visual_text_color="#000",
    #visual_orient="horizontal",
#**style.init_style
# )
#heatmap.render("heatmap.html")



time_end = time.time()
logger.info('Plotting Physics - Chemistry (Normalized), cost time:%d s', time_end - time_start)
