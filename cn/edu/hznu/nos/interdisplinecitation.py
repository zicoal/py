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
#src_dir='/home/zico/py/data/'
#src_root_file='/home/zico/py/discipline.txt'
#dest_dir='/home/zico/py/data/processed/'
#dest_file_papers=dest_dir+"papers.txt"

#server
#src_dir='/home/zico/mag/data/microsoft-2017-nov/'
src_root_file='/home/zico/mag/data/discipline.txt'
src_dir='/home/zico/mag/data/processed/'
src_file_papers=src_dir+"papers.txt"
dest_file_interdispline_citation= src_dir+"interdispline_citation.txt"



f_citations = open(dest_file_interdispline_citation, encoding='UTF-8', mode='w', errors='ignore')

f = open(src_root_file,encoding='UTF-8', mode='r',errors='ignore')
line =f.readline()

dict_disciplines= {}

#reading disciplines
while line:
    words=line.replace('\n','').split('\t')

    rootdesc=words[0].strip()

    if (len(rootdesc) == 0):
        line = f.readline()
        continue

    dict_disciplines.setdefault(rootdesc, 0)

    line =f.readline()
f.close()

time_end = time.time()
logger.info('Read Roots Done, cost time:%d s', time_end - time_start)

#reeading papers
f = open(src_file_papers,encoding='UTF-8', mode='r',errors='ignore')
line =f.readline()
num_totallines=0
dict_paper_discipline= {}

while line:
    num_totallines += 1
    if(num_totallines%2!=0):
        #paper line
        words = line.split('\t')
        p_id= words[0].strip()
        p_discipline = words[2].strip()
        if(len(p_discipline)==0):
            line = f.readline()
            continue
        dict_paper_discipline.setdefault(p_id, p_discipline)

    line =f.readline()
    if (num_totallines % 1000000 == 0):
        time_end = time.time()
        logger.info('Reading papers : %d, cost time:%d s', num_totallines, time_end - time_start)
f.close()

time_end = time.time()
logger.info('Read Papers Done, #total papers: %d, cost time:%d s',num_totallines/2, time_end - time_start)

#reeading citaton
f = open(src_file_papers,encoding='UTF-8', mode='r',errors='ignore')
line =f.readline()
num_linecount=0
dict_discipline_ctations= {}
p_discipline = ''
while line:
    num_linecount += 1
    if(num_linecount%2!=0):
        #paper line
        words = line.split('\t')
        p_discipline = words[2].strip()
        if (len(p_discipline) == 0):
            line = f.readline()
            continue
    elif(num_linecount%2==0):
        #citation line
        words = line.replace('[', '').replace(']', '').split(',')
        for ref in words:
            if(len(ref.strip())==0):
                continue
            if dict_paper_discipline.get(ref.strip()) is not None:
                ref_discipline = dict_paper_discipline.get(ref.strip())
                keys =dict_discipline_ctations.get(ref_discipline)
                if(keys is None):
                    dict_discipline_ctations.setdefault(ref_discipline,{})[p_discipline]=1
                elif (p_discipline in keys):
                    dict_discipline_ctations[ref_discipline][p_discipline] +=1
                else:
                    dict_discipline_ctations.setdefault(ref_discipline,{})[p_discipline]=1
    line =f.readline()
    if (num_linecount % 1000000 == 0 or num_linecount==num_totallines):
        time_end = time.time()
        logger.info('Reading citations : %d, process:%f%%, cost time:%d s', num_linecount, num_linecount*100.0/num_totallines, time_end - time_start)
f.close()

str_interdiscipline=""
for keys,dict_discipline_ctations_values in dict_discipline_ctations.items():
    for key, value in dict_discipline_ctations_values.items():
        #a<-b
        str_interdiscipline = str_interdiscipline+("%s\t%s\t%d\n" % (keys,key,value))

f_citations.write(str_interdiscipline)

f_citations.close()
time_end = time.time()
logger.info(' Done, #total papers: %d, cost time:%d s',num_totallines/2, time_end - time_start)
