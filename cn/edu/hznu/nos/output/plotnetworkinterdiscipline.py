# !/usr/bin/python
# coding:utf-8


import json
import os
import logging
import time
import networkx as nx
import numpy as np
from  matplotlib import pyplot as plt



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


src_dir='/home/zico/data/mag/processed/'
src_file_papers=src_dir+"discipline_papers.txt"
src_file_citations=src_dir+"interdispline_citation.txt"

colors= ['bisque','lightgreen','slategrey','lightcoral','gold',
         'c','cornflowerblue','blueviolet','tomato','olivedrab',
         'lightsalmon','sage','lightskyblue','orchid','hotpink',
         'silver', 'slategray', 'indigo', 'darkgoldenrod','orange']


dict_disciplines_papers_num= {}

#reading disciplines

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

g = nx.DiGraph()

nodes = []
links = []
g.position = {}
g.population = {}

dict_disciplines_papers_num = sorted(dict_disciplines_papers_num.items(), key=lambda x: x[1])
for p in  dict_disciplines_papers_num:
    #g.add_node(p[0],size=100.0*p[1]/num_max_papers,fillcolor=colors[0])
    g.add_node(p[0], size=1000.0 * p[1] / num_max_papers, fillcolor=colors[0])
#    nodes.append({"name":p[0],"symbolSize":100.0*p[1]/num_max_papers})


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

plt.axis('off')
plt.show()

'''
num_top_citations = 3
for keys,values in dict_disciplines_citing.items():
    values = sorted(values.items(), key=lambda x: x[1],reverse=True)
    top=0
    for key in values:
        if(top<num_top_citations):
            links.append({"source": keys, "target": key[0]})
            top += 1

'''

for keys,values in dict_disciplines_citing.items():
    num_total=0
    for key, value in values.items():
        num_total+=value
    for key, value in values.items():
        g.add_edge(keys, key, weight=int(value)*1.0/num_total)

pos=nx.circular_layout(g)
nx.draw_networkx_nodes(g,pos=pos)
nx.draw_networkx_edges(g,pos=pos)
plt.axis('off')
plt.show()
'''
#output cited
f = open(dest_file_citations_cited, encoding='UTF-8', mode='w', errors='ignore')
for keys,values in dict_disciplines_cited.items():
    num_total=0
    for key, value in values.items():
        num_total+=value
    for key, value in values.items():
        f.write('%s\t%s\t%s\n' % (key,keys,100.0*int(value)*1.0/num_total))
f.close()
'''
'''
graph = Graph("InterDiscipline Citing Relationship", **style.init_style)
graph.add(
    "",
    nodes,
    links,
    is_label_show=True,
    graph_layout="circular",
    line_width =2,
    label_text_color=None,
    line_curve =  0.1
#    graph_edge_symbol= "arrow"
)
graph.render()
'''


