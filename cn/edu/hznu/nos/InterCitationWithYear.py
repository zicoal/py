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
dest_file_interdispline_citation= src_dir+"inter_citation_year.txt"
dest_file_discipline_papers_nums= src_dir+"discipline_papers_year.txt"


#reeading papers
f = open(src_file_papers,encoding='UTF-8', mode='r',errors='ignore')
line =f.readline()
num_totallines=0
dict_paper_discipline= {}
dict_paper_year= {}

dict_disciplines= {}
num_no_disciplines=0

while line:
    num_totallines += 1
    if(num_totallines%2!=0):
        #paper line (odd line)
        words = line.split('\t')
        p_id= words[0].strip()
        p_year = words[1].strip()
        p_discipline = words[2].strip()
        if(len(p_discipline)==0):
            num_no_disciplines += 1
            line = f.readline()
            continue
        if (dict_disciplines.get(p_discipline) is None):
            #dict_disciplines.setdefault(p_discipline, 1)
            #for each discipline in each year,
            dict_disciplines.setdefault(p_discipline,{})[p_year] =1
        else:
            tmp =  dict_disciplines.get(p_discipline)
            if (tmp.get(p_year) is None):
                tmp[p_year] =1
            else:
                dict_disciplines[p_discipline][p_year] +=1

#        dict_paper_year.setdefault(p_id, p_year)
        dict_paper_discipline.setdefault(p_id, p_discipline)

    line =f.readline()
    if (num_totallines % 1000000 == 0):
        time_end = time.time()
        logger.info('Reading papers: %d, cost time:%d s', num_totallines, time_end - time_start)
f.close()

time_end = time.time()
logger.info('Read Papers Done, #total papers: %d, cost time:%d s',num_totallines/2, time_end - time_start)

#reeading citation
f = open(src_file_papers,encoding='UTF-8', mode='r',errors='ignore')
line =f.readline()
num_linecount=0
dict_discipline_ctations= {}
p_discipline = ''
p_year='N/A'
b_valid_label=False
while line:
    num_linecount += 1
    if(num_linecount%2!=0):
        #paper line (odd line)
        words = line.split('\t')
#        if(len(words)<3):
#            print(line)
#            print(num_linecount)
        p_discipline = words[2].strip()
        p_year = words[1].strip()
        if (len(p_discipline) == 0):
            p_discipline = ''
            p_year='N/A'
            b_valid_label = False
        else:
            b_valid_label = True
    elif(num_linecount%2==0 and b_valid_label == True):
        #citation line (even line)
        refs_tmp = line.replace('[', '').replace(']', '').replace('\n', '')
        if (len(refs_tmp.strip()) == 0):
            line = f.readline()
            continue
        refs = refs_tmp.split(',')
        for ref in refs:
            if(len(ref.strip())==0):
                continue
            if dict_paper_discipline.get(ref.strip()) is not None:
                #ref DOES in paper list
                ref_discipline = dict_paper_discipline.get(ref.strip())
                #ref_year = dict_paper_year.get(ref.strip())

                d0_cited_discipline=dict_discipline_ctations.get(ref_discipline)

               # keys=dict_discipline_ctations.get(ref_discipline)

                if(d0_cited_discipline is None):
                    # no citing paper
                    d1_cited_discipline=dict_discipline_ctations.setdefault(ref_discipline, {})
                    d1_cited_discipline.setdefault(p_discipline, {})[p_year] =1
                else:
                    keys_disciplines = dict_discipline_ctations[ref_discipline].keys()
                    if(p_discipline in keys_disciplines):
                        d2_cited_discipline= d0_cited_discipline.get(p_discipline)
                        if(p_year in d2_cited_discipline.keys()):
                            #print(p_year)
                            #print(d2_cited_discipline.keys())
                            #print(keys_cited_year)
                            d2_cited_discipline[p_year]+=1
                        else:
                            d0_cited_discipline.setdefault(p_discipline, {})[p_year] = 1
                    else:
                        #citing discilipine not exsit
                        d0_cited_discipline.setdefault(p_discipline, {})[p_year] = 1

                    #for keyx, valuex in dict_discipline_ctations.items():
                        #    # a<-b
                        #    for keyxx, valuexx in valuex.items():
                        #    for keyxxx, valuexxx in valuexx.items():
                        #       print("%s\t%s\t%s" % (keyx, keyxx, keyxxx))
                        #       print(valuexx)
                        #       print(valuexxx)
                        #       print("%s\t%s\t%s\t%s" % (keyx, keyxx, keyxxx,valuexxx))
                        #       exit()

    line =f.readline()
    if (num_linecount % 1000000 == 0 or num_linecount==num_totallines):
        time_end = time.time()
        logger.info('Reading citations : %d, process:%f%%,num_no_disciplines:%d, cost time:%d s', num_linecount, num_linecount*100.0/num_totallines, num_no_disciplines, time_end - time_start)
f.close()

str_interdiscipline=""


for  keyx, valuex  in dict_discipline_ctations.items():
    # a<-b
    for keyxx, valuexx in valuex.items():
        for keyxxx, valuexxx in valuexx.items():
            str_interdiscipline = str_interdiscipline + ("%s\t%s\t%s\t%s\n" % (keyx, keyxx, keyxxx,valuexxx))


#for keys,dict_discipline_ctations_values in dict_discipline_ctations.items():
#    for key, value in dict_discipline_ctations_values.items():

f_citations = open(dest_file_interdispline_citation, encoding='UTF-8', mode='w', errors='ignore')
f_citations.write(str_interdiscipline)
f_citations.close()

str_discipline_papers=""
for  key, value  in dict_disciplines.items():
        #a<-b
        for key1, value1 in value.items():
            #discipline, year, publications
            str_discipline_papers = str_discipline_papers+("%s\t%s\t%d\n" % (key,key1,value1))

f_papers = open(dest_file_discipline_papers_nums, encoding='UTF-8', mode='w', errors='ignore')
f_papers.write(str_discipline_papers)
f_papers.close()


time_end = time.time()
logger.info(' Done, #total lines: %d,#total papers: %d,#empty_disciplines: %d, cost time:%d s',num_totallines/2,num_totallines/2-num_no_disciplines, num_no_disciplines, time_end - time_start)
