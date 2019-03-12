# !/usr/bin/python
# coding:utf-8


import json
import os
import logging
import time
import networkx as nx
import numpy as np
from  matplotlib import pyplot as plt
from scipy.optimize import curve_fit


def func(x, a, b, c):
    return a * np.exp(b * x) + c

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
src_file_papers=src_dir+"data\\discipline_papers_year.txt"
dest_fig_growth_yearly=src_dir+"figs\\discpline_growth\growth_dynamical_pattern_yearly_%s_%s_fitting.png"
dest_fig_growth_culmulative=src_dir+"figs\\discpline_growth\growth_dynamical_pattern_culmulative_%s_%s_fitting.png"

#--linux--
#src_dir='/home/zico/py/cn/edu/hznu/nos/'
#src_file_citations=src_dir+"data/inter_citation_year.txt"
#dest_fig_citation_patten=src_dir+"figs/citation_patten_%s_%s_%s_%s_%s.png"

colors= ['bisque','lightgreen','slategrey','lightcoral','gold',
         'c','aliceblue','blueviolet','blue','olivedrab',
         'lightsalmon','palegreen','lightskyblue','orchid','hotpink',
         'silver', 'slategray', 'rosybrown', 'darkgoldenrod','orange']


dict_disciplines_papers_num= {}

#reading disciplines

f = open(src_file_papers,encoding='UTF-8', mode='r',errors='ignore')
line =f.readline()
str_observation_discipline1='physics'
str_observation_discipline2='chemistry'
num_max_papers_ci=0
num_linecount=0

dict_discipline_papers_yearly={}
dict_discipline_papers_cumulative={}
list_disciplines=[]

start_year=1900
end_year=1950

logger.info('Observation Year:%d - %d.', start_year, end_year)

while line:
        words=line.replace('\n','').split('\t')

        str_discipline= words[0].strip()
        num_year= int(words[1].strip())
        num_citations =  int(words[2].strip())
        if(str_discipline not in list_disciplines):
            list_disciplines.append(str_discipline)

        if(num_year<start_year or num_year>end_year):
            num_linecount += 1
            line = f.readline()
            continue

        dict_discipline_papers_yearly.setdefault(num_year, {})[str_discipline] = num_citations
        '''
         if (dict_discipline_papers_yearly.get(num_year) is None):
          #  d1_cited_discipline=dict_discipline_papers_yearly.setdefault(num_year, {})
          dict_discipline_papers_yearly.setdefault(num_year, {})[str_discipline] = num_citations
        else:
            d1_discipline = dict_discipline_papers_yearly.get(num_year)
            d1_discipline[str_discipline] = num_citations
       '''
        num_linecount+=1
        line =f.readline()
time_end = time.time()
logger.info('Reading discipline by years : %d, cost time:%d s', num_linecount, time_end - time_start)
f.close()

#--plot paper growth starts--
##output paper_growth_yearly and cumulatively

dict_discipline_papers_yearly = sorted(dict_discipline_papers_yearly.items(), key=lambda x: x[0])

dict_x_year= {}
dict_y_year = {}
dict_x_cumulative = {}
dict_y_cumulative = {}
dict_citation_cumulative={}


for p in dict_discipline_papers_yearly:
#    print(p[0])
#    print(p[1])
#    exit()
    p_year = p[0]
    tmp_dict_disciplines=p[1]

    for discipline, citations in tmp_dict_disciplines.items():

        dict_x_year.setdefault(discipline, []).append(p[0])
        dict_y_year.setdefault(discipline, []).append(citations)
        dict_x_cumulative.setdefault(discipline, []).append(p[0])

        if(dict_y_cumulative.get(discipline) is None):
            dict_y_cumulative.setdefault(discipline, []).append(citations)
            dict_citation_cumulative[discipline]=citations
        else:
            dict_citation_cumulative[discipline]+=citations
            dict_y_cumulative.setdefault(discipline, []).append(dict_citation_cumulative[discipline])
i=0

dict_citation_cumulative = sorted(dict_citation_cumulative.items(), key=lambda x: x[0])

ax = plt.gca()  # 获取当前图像的坐标轴信息
ax.yaxis.get_major_formatter().set_powerlimits((0,1)) # 将坐标轴的base number设置为一位。
plt.figure().set_size_inches(18.4, 13.5)
for p in dict_citation_cumulative:
    discipline=p[0]
    plt.plot(dict_x_year.get(discipline), dict_y_year.get(discipline), linewidth='1',
             label=("%s" % (discipline.capitalize())), color=colors[i],linestyle='-', marker='o')
    plt.legend(loc='upper left')
    plt.xlim(start_year-5, end_year+5)
    plt.title(('Paper Growth Pattern(%s- %s)' %(start_year,end_year)), size='20')
    plt.xlabel('Year', size='20')
    plt.ylabel('# of Papers', size='20')
    tmp_dest_fig_growth_yearly = dest_fig_growth_yearly % ( start_year, end_year);
    plt.savefig(tmp_dest_fig_growth_yearly,dpi=400,bbox_inches='tight')
    # plt.show()
    i+=1
    time_end = time.time()
    logger.info('Plotting %s (Yearly), cost time:%d s', discipline,
                time_end - time_start)

ax = plt.gca()  # 获取当前图像的坐标轴信息
ax.yaxis.get_major_formatter().set_powerlimits((0,1)) # 将坐标轴的base number设置为一位。

plt.figure().set_size_inches(18.4, 13.5)
i=0
for p in dict_citation_cumulative:
    discipline=p[0]
    plt.plot(dict_x_cumulative.get(discipline), dict_y_cumulative.get(discipline), linewidth='1',
             label=("%s" % (discipline.capitalize())), color=colors[i],linestyle='-', marker='o')
    plt.legend(loc='upper left')
    plt.xlim(start_year-5, end_year+5)
    plt.title(('Paper Cumulative Growth Pattern(%s- %s)' %(start_year,end_year)), size='20')
    plt.xlabel('Year', size='20')
    plt.ylabel('# of Papers', size='20')
    tmp_dest_fig_growth_culmulative = dest_fig_growth_culmulative % (start_year, end_year);
    plt.savefig(tmp_dest_fig_growth_culmulative,dpi=400,bbox_inches='tight')
    # plt.show()
    i+=1
    time_end = time.time()
    logger.info('Plotting %s (Cumulative), cost time:%d s', discipline,
                time_end - time_start)
