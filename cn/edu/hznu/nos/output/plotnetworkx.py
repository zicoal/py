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


src_dir='/home/zico/data/mag/processed/'
src_file_papers=src_dir+"discipline_papers.txt"
src_file_citations=src_dir+"interdispline_citation.txt"

dest_file_papers=src_dir+"normalized_discipline_papers.txt"
dest_file_citations_citing=src_dir+"normalized_citing_interdispline_citation.txt"
dest_file_citations_cited=src_dir+"normalized_cited_interdispline_citation.txt"

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
f = open(dest_file_papers, encoding='UTF-8', mode='w', errors='ignore')

for p in  dict_disciplines_papers_num:
    f.write('%s\t%s\n' % (p[0],100.0*p[1]/num_max_papers))
    nodes.append({"name":p[0],"symbolSize":100.0*p[1]/num_max_papers})

f.close()
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


num_top_citations = 3
for keys,values in dict_disciplines_citing.items():
    values = sorted(values.items(), key=lambda x: x[1],reverse=True)
    top=0
    for key in values:
        if(top<num_top_citations):
            links.append({"source": keys, "target": key[0]})
            top += 1


'''
#output citing
f = open(dest_file_citations_citing, encoding='UTF-8', mode='w', errors='ignore')
for keys,values in dict_disciplines_citing.items():
    num_total=0
    for key, value in values.items():
        num_total+=value
    for key, value in values.items():
        f.write('%s\t%s\t%s\n' % (keys,key,100.0*int(value)*1.0/num_total))
        links.append({"source": keys, "target": key})
f.close()

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


