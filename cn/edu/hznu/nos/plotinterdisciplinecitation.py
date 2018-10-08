#!/usr/bin/python
# coding:utf-8

import json
import os
import logging
import time



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

#pc
#src_dir='D:\\data\\mag\\big\\processed\\'
#src_root_file='/home/zico/py/discipline.txt'
#dest_dir='/home/zico/py/data/processed/'
#dest_file_papers=dest_dir+"papers.txt"

#server
#src_dir='/home/zico/mag/data/microsoft-2017-nov/'
src_dir='/home/zico/py/data/processed/'
src_file_papers=src_dir+"interdispline_citation.txt"
dest_file_interdispline_citation_pic= src_dir+"interdiscipline_citation.png"
dest_file_singledispline_citation= src_dir+"singlediscipline_citation.txt"


f_citations = open(dest_file_singledispline_citation, encoding='UTF-8', mode='w', errors='ignore')

f = open(src_file_papers,encoding='UTF-8', mode='r',errors='ignore')
line =f.readline()

dict_disciplines_cited= {}

#reading disciplines
while line:
    words=line.replace('\n','').split('\t')

    discipline_cited=words[0].strip()
    discipline_citing=words[1].strip()
    num_discipline_cited=int(words[2].strip())
    if (len(discipline_cited)==0 or len(discipline_cited)==0):
        line = f.readline()
        continue
    if(dict_disciplines_cited.get(discipline_cited) is None):
        dict_disciplines_cited.setdefault(discipline_cited, num_discipline_cited)
    else:
        dict_disciplines_cited[discipline_cited]+=num_discipline_cited

    line =f.readline()
f.close()

time_end = time.time()
logger.info('Read disciplines citations Done, cost time:%d s', time_end - time_start)

#reeading papers

str_interdiscipline=""
for key,value in dict_disciplines_cited.items():
        #a<-b
        str_interdiscipline = str_interdiscipline+("%s\t%d\n" % (key,value))

f_citations.write(str_interdiscipline)

f_citations.close()
time_end = time.time()
#logger.info(' Done, #total papers: %d, cost time:%d s',num_totallines/2, time_end - time_start)
