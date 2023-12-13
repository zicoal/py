from warnings import simplefilter
import matplotlib.pyplot as plt
import math
import os
import networkx as nx
import numpy as np
import pandas as pd
from random import *
import time
import logging
import xlsxwriter
from openpyxl import load_workbook
from xlsxwriter import Workbook

simplefilter(action='ignore', category=FutureWarning)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
# 定义handler的输出格式
#logger to console
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
#fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(ch)

q_start_columm=1
rca_thresholds = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6,
                  1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3,
                  2.4,2.5,2.6,2.7,2.8,2.9,3,3.1,
                  3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4,4.1]
rca_threshold=2.1

#equations = "score1-5"


#get the mapped score
#equations = "eq-nonlinear"
#def getscore (x):
#    b = 6
#    c = 10
#    return x**2 - b*x +c

#get the mapped score
equations = "eq-linear"
def getscore (x):
    return x
#exit(0)




logger.info("loading data...")
time_start = time.time()
data_types =["data1",'data2']
data_files = ['ESGstudy1Data','ESGstudy2Data']
questions =[
        [
         'Q3_1','Q3_2','Q3_3','Q3_4','Q4_1','Q4_2','Q4_3','Q4_4','Q4_5',
         'Q5_1','Q5_2','Q5_3','Q5_4','Q5_5','Q6_1','Q6_2','Q6_3',
         'Q7_1','Q7_2','Q7_3','Q7_4','Q7_5','Q7_6','Q7_7','Q7_8	',
         'Q8_1','Q8_2','Q8_3','Q8_4','Q8_5','Q8_6',
         'Q9_1','Q9_2','Q9_3','Q9_4','Q9_5','Q9_6',
         'Q10_1','Q10_2','Q10_3','Q11_1','Q11_2','Q11_3',
         'Q12_1','Q12_2','Q12_3','Q13_1','Q13_2','Q13_3','Q13_4','Q13_5','Q13_6','Q13_7',
         'Q14_1','Q14_2','Q14_3','Q14_4','Q14_5','Q14_6','Q14_7','Q14_8','Q14_9',	
         'Q15_1','Q15_2','Q15_3','Q15_4','Q15_5','Q15_6',
         'Q16_1','Q16_2','Q16_3','Q16_4','Q16_5','Q16_6','Q16_7','Q17'],
        [
          'Q1_1','Q1_2','Q1_3','Q1_4','Q2_1','Q2_2','Q2_3','Q2_4','Q2_5','Q2_6','Q2_7',
          'Q3_1','Q3_2','Q3_3','Q3_4','Q3_5','Q3_6','Q3_7','Q3_8','Q3_9','Q3_10','Q3_11','Q3_12','Q3_13',
          'Q4_1','Q4_2	Q4_3','Q4_4','Q5_1','Q5_2','Q5_3','Q5_4','Q5_5','Q5_6',
          'Q6_1','Q6_2','Q6_3','Q6_4','Q6_5','Q6_6','Q7_1','Q7_2','Q7_3','Q7_4','Q7_5','Q7_6','Q7_7','Q7_8','Q7_9',
          'Q8_1','Q8_2','Q8_3','Q8_4','Q8_5','Q8_6','Q9_1','Q9_2','Q9_3','Q9_4','Q10_1','Q10_2']
        ]

for m in range(len(data_types)):

    f1 = 'D:\\pydata\\data\\jiyingru\\%s\\%s.xlsx' % (data_types[m],data_files[m])

    df = pd.read_excel(f1)

    time_end = time.time()
    logger.info("data loaded...time cost:%d s'", time_end - time_start)

    cols = ['id']
    cols = cols + questions[m]
    logger.info(cols)

    for rca_threshold in rca_thresholds:
        f_rca= 'D:\\pydata\\data\\jiyingru\\%s\\rca_number_%.1f.csv' % (data_types[m], rca_threshold)
        f_weights = 'D:\\pydata\\data\\jiyingru\\%s\\weights_number_min_%.1f.csv' % (data_types[m], rca_threshold)
        logger.info("data:%s,RCA:%.1f,Equation:%s" % (data_types[m],rca_threshold,equations))

        if os.path.isfile(f_rca):
            os.remove(f_rca)
            os.remove(f_weights)

        paticipant_quest_rca = pd.DataFrame(columns=['id', 'Q', 'RCA'])
        quest_phi_weight_network = pd.DataFrame(columns=['QA', 'QB', 'weights'])

        paticipant_quest_rca.to_csv(f_rca, mode="w" ,index=False)

        quest_phi_weight_network.to_csv(f_weights, mode="w" , index=False)


        time_end = time.time()
        paticipant_quest_rca = pd.DataFrame(columns=[ 'id', 'Q', 'RCA'])
        quest_phi_weight_network = pd.DataFrame(columns=['QA', 'QB', 'weights'])

        logger.info('data:%s,RCA:%.1f,participants:%d, time:%d s', data_types[m], rca_threshold, len(df), time_end - time_start)
        data_one_country = df.values.tolist()
        df_values=  pd.DataFrame(columns=cols)
        '''
        df_values =  pd.DataFrame(columns=['id','Q3_1','Q3_2','Q3_3','Q3_4','Q4_1','Q4_2','Q4_3','Q4_4','Q4_5',
             'Q5_1','Q5_2','Q5_3','Q5_4','Q5_5','Q6_1','Q6_2','Q6_3',
             'Q7_1','Q7_2','Q7_3','Q7_4','Q7_5','Q7_6','Q7_7','Q7_8	',
             'Q8_1','Q8_2','Q8_3','Q8_4','Q8_5','Q8_6',
             'Q9_1','Q9_2','Q9_3','Q9_4','Q9_5','Q9_6',
             'Q10_1','Q10_2','Q10_3','Q11_1','Q11_2','Q11_3',
             'Q12_1','Q12_2','Q12_3','Q13_1','Q13_2','Q13_3','Q13_4','Q13_5','Q13_6','Q13_7',
             'Q14_1','Q14_2','Q14_3','Q14_4','Q14_5','Q14_6','Q14_7','Q14_8','Q14_9',
             'Q15_1','Q15_2','Q15_3','Q15_4','Q15_5','Q15_6',
             'Q16_1','Q16_2','Q16_3','Q16_4','Q16_5','Q16_6','Q16_7','Q17'])
        '''
        for i in range(len(data_one_country)):
            q_values = [data_one_country[i][0]] #id
            for j in range(len(questions[m])):
                    v= getscore(data_one_country[i][j+q_start_columm])
                    q_values.append(v)
            df_values.loc[len(df_values)] = q_values
        paticipants = [data_one_country[i][0] for i in range(len(df))]
        paticipants = sorted(list(set(paticipants))) #去重

        #计算每个问题的全局权重
        question_part={}
        df_temp = df_values.drop(['id'], axis=1)
    #        logger.info(df_temp)
        sum_quesitons=df_temp.sum()
        sum_all= sum(sum_quesitons)
        sum_participants=df_temp.sum(axis=1)

        question_participant = {}
        for i in range(len(questions[m])):
            q = questions[m][i]
            question_part[q] = sum_quesitons[i] / sum_all
            question_participant[q]=[]
        #计算单一question的RCA
        i=0
        for participant in paticipants:
            #ignore invalid users : did not response at all
            if (sum_participants[i] >0):
                for j in range(len(questions[m])):
                    participant_question_ratio= df_values.loc[i,questions[m][j]] /sum_participants[i]
                    rca = 1 if participant_question_ratio/(question_part[questions[m][j]]) >= rca_threshold else 0
                    paticipant_quest_rca.loc[len(paticipant_quest_rca)] = [participant,questions[m][j], rca]

                   ###记录有效rca对应的人
                    if rca == 1:
                        list_participants=question_participant.get(questions[m][j])
                        list_participants.append(participant)
                        question_participant[questions[m][j]]=list_participants
            i += 1
        #计算phi
        for i in range(len(questions[m])-1):
            for j in range(i+1, len(questions[m])):
                #两个集合的交集
                set_participants= set(question_participant[questions[m][i]]) & set(question_participant[questions[m][j]])
                if (len(set_participants)>0):
                    phi_ij = len(set_participants) / len(question_participant[questions[m][j]])
                    phi_ji = len(set_participants) / len(question_participant[questions[m][i]])
                    #@Todo: check  min or max
                    phi = phi_ij if phi_ij < phi_ji else phi_ji
                    quest_phi_weight_network.loc[len(quest_phi_weight_network)] = [questions[m][i], questions[m][j],phi]
                #else:
                #    quest_phi_weight_network.loc[len(quest_phi_weight_network)] = [y,questions[i], questions[j], 0]

        #write to file

        #time_end = time.time()
        quest_phi_weight_network.to_csv(f_weights, mode="a",  index=False, header=False)

        paticipant_quest_rca.to_csv(f_rca, mode="a",  index=False, header=False)


time_end = time.time()
logger.info('The end,cost time:%d s', time_end - time_start)
