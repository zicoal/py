# !/usr/bin/python
# coding:utf-8


import json
import os
import logging
import time
from pyecharts import Graph
from pyecharts import Style

style = Style(
    title_color="#000",
    title_pos="center",
    width=1300,
    height=800,
#    background_color='#404a59'
)



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
src_file_papers=src_dir+"discipline_papers.txt"
src_file_citations=src_dir+"interdispline_citation.txt"


colors= ['bisque','lightgreen','slategrey','lightcoral','gold',
         'c','cornflowerblue','blueviolet','tomato','olivedrab',
         'lightsalmon','sage','lightskyblue','orchid','hotpink',
         'silver', 'slategray', 'indigo', 'darkgoldenrod','orange']


dict_disciplines_papers_num= {}

#reading disciplines
nodes = []
links = []

f = open(src_file_papers,encoding='UTF-8', mode='r',errors='ignore')
line =f.readline()
num_max_papers=0
while line:
    words=line.replace('\n','').split('\t')

    str_discipline = words[0].strip()
    num_discipline_papers =  int(words[1].strip())
    dict_disciplines_papers_num.setdefault(str_discipline, num_discipline_papers)
    if(num_discipline_papers > num_max_papers ):
        num_max_papers = num_discipline_papers
    line =f.readline()
f.close()

dict_disciplines_papers_num = sorted(dict_disciplines_papers_num.items(), key=lambda x: x[1])

#for key,value in dict_disciplines_papers_num.items():
for p in  dict_disciplines_papers_num:
    nodes.append({"name":p[0],"symbolSize":100.0*p[1]/num_max_papers})

dict_disciplines_cited= {}
dict_disciplines_citing= {}


f = open(src_file_citations,encoding='UTF-8', mode='r',errors='ignore')
line =f.readline()
while line:
    words=line.replace('\n','').split('\t')

    str_discipline_cited = words[0].strip()
    str_discipline_citing = words[1].strip()
    num_interdiscipline_citation =  int(words[2].strip())

    dict_disciplines_cited.setdefault(str_discipline_cited,{})[str_discipline_citing] = num_interdiscipline_citation
    dict_disciplines_citing.setdefault(str_discipline_citing,{})[str_discipline_cited] = num_interdiscipline_citation

    line =f.readline()

f.close()

for keys,values in dict_disciplines_citing.items():
    for key, value in values.items():
        links.append({"source": keys, "target": key})

graph = Graph("InterDiscipline Citing Relationship", **style.init_style)
graph.add(
    "",
    nodes,
    links,
    is_label_show=True,
    graph_layout="circular",
    line_width =2,
    label_text_color=None,
    line_curve =  0.1,
    graph_edge_symbol= "arrow"
)
graph.render()


