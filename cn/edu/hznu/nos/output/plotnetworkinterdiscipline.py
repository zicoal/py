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
src_dir='D:\\py\\cn\\edu\\hznu\\nos\\data\\'
src_file_papers=src_dir+"discipline_papers.txt"
src_file_citations=src_dir+"interdispline_citation.txt"
src_file_positions=src_dir+"discipline_positions"


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

f = open(src_file_positions,encoding='UTF-8', mode='r',errors='ignore')
line =f.readline()
dict_disciplines_positions={}
linecount=0
while line:
    words=line.replace('\n','').split(':')
    linecount+=1
    str_discipline = words[0].strip()
    str_discipline_position =  words[1].strip()
    dict_disciplines_positions.setdefault(linecount, str_discipline_position)
#    dict_disciplines_positions.setdefault(str_discipline, str_discipline_position)
    line =f.readline()
f.close()

g = nx.DiGraph()


nodes = []
links = []
g.position = {}
g.population = {}
linecount=0
g.labels=[]
dict_disciplines_papers_num = sorted(dict_disciplines_papers_num.items(), key=lambda x: x[1])
for p in  dict_disciplines_papers_num:
    #g.add_node(p[0],size=100.0*p[1]/num_max_papers,fillcolor=colors[0])
#    g.add_node(p[0], size=1000.0 * p[1] / num_max_papers, fillcolor=colors[0])
    g.add_node(p[0])
    linecount+=1
    xy=dict_disciplines_positions[linecount].split(",")
    x=float(xy[0])
    y=float(xy[1])
#    print(p[0]+":"+xy[0]+","+xy[1])
    g.position[p[0]] = (x,y)
    g.labels.append(p[0])
    g.population[p[0]]=5000*p[1]*1.0 / num_max_papers
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
edge_width=[]

num_top_citations = 3
for keys,values in dict_disciplines_citing.items():
    num_total=0
    num_max=0
    top=0
    for key, value in values.items():
        if(num_max<value):
            num_max = value
        num_total+=value
    values = sorted(values.items(), key=lambda x: x[1],reverse=True)
    for key in values:
        if(top<num_top_citations):
#            g.add_edge(keys, key, weight=int(value)*1.0/num_total)
#            g.add_edge(keys, key[0], weight=int(100*1.0*int(key[1])/num_total))
            g.add_edge(keys, key[0])
#            edge_width.append(2*1.0*int(key[1])/num_total)
            edge_width.append(1.0*int(key[1])/num_max)
            print(keys+"->"+ key[0])
            top += 1

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


#pos =nx.circular_layout(g)
#print('position of all nodes:',pos)
nx.draw(g,g.position,
        node_size=[g.population[v] for v in g],
        with_labels=True,
        width=edge_width,
        arrowsize=5,
        arrowstyle="Fancy, head_length=2, head_width=1, tail_width=0.1"
       )

'''
nx.draw_networkx_nodes(g,g.position,
        node_size=[g.population[v] for v in g],
        label="P",
        arrowsize=5,
        arrowstyle="Fancy, head_length=3, head_width=1, tail_width=0.1"
        )
nx.draw_networkx_edges(g,g.position,width=edge_width)
'''
plt.axis('off')
plt.show()

