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
src_dir='/home/zico/mag/data/microsoft-2017-nov/'
src_root_file='/home/zico/mag/data/discipline.txt'
dest_dir='/home/zico/mag/data/processed/'
dest_file_papers=dest_dir+"papers.txt"



f_papers = open(dest_file_papers, encoding='UTF-8', mode='w', errors='ignore')

f = open(src_root_file,encoding='UTF-8', mode='r',errors='ignore')
line =f.readline()

dict_disciplines= {}

#reading disciplines
while line:
    words=line.replace('\n','').split('\t')

    rootdesc=words[0].strip()

    dict_disciplines.setdefault(rootdesc, rootdesc)

    line =f.readline()
f.close()

time_end = time.time()
logger.info('Read Roots Done, cost time:%d s', time_end - time_start)


list_files = os.listdir(src_dir)

num_no_discipline_papers=0
num_no_reference_papers=0
num_multi_disciplines_papers=0

num_file_count=0
num_total_files = len(list_files)
num_total_papers=0

for file in list_files:
    num_file_count += 1
    s_file=src_dir +file
    if(os.path.isdir(s_file)):
        continue
    f = open(s_file, 'r')
    json_papers = json.load(f)
#    for paper in range(len(json_papers)):
#        print(json_papers[paper]['Id'])
#        exit(0)
    tmp_str_paper = ""
    tmp_str_refs = ""
    num_total_papers+=len(json_papers)
    for paper in json_papers:

        if (paper.get('RId') == None):
            num_no_reference_papers += 1
            continue

        if (paper.get('F') == None):
            num_no_discipline_papers += 1
            continue
        else:
            fields = paper['F']
            tmp_num_disciplines=0
            tmp_discipline=""
            for field in fields:
                field_name=field['FN'].lower()
                if (dict_disciplines.get(field_name) is not None):
                    tmp_num_disciplines += 1
                    tmp_discipline=field_name
#           print(tmp_num_disciplines)
            if tmp_num_disciplines>1:
                num_multi_disciplines_papers += 1
                continue
            else:
                #output files
                # two lines
                # paper info
                # refs_id
                refs = paper['RId']
                tmp_str_paper = tmp_str_paper + ("%s\t%s\t%s\n%s\n" % (paper['Id'],paper['Y'],tmp_discipline,refs))
    f_papers.write(tmp_str_paper)
    if (num_file_count % 1000 == 0) or (num_file_count == num_total_files):
        time_end = time.time()
        logger.info('Reading : %d, ratio: %f%%, total_papers:%d, num_multi_disciplines_papers: %d,num_no_discipline_papers:%d,num_no_reference_papers:%d, cost time:%d s', num_file_count,
                    num_file_count * 1.0 / num_total_files * 100.0, num_total_papers, num_multi_disciplines_papers, num_no_discipline_papers,num_no_reference_papers, time_end - time_start)

    f.close()

f_papers.close()
