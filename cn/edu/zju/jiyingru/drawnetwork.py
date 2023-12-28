import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontManager
from pylab import mpl
import math
import os
import networkx as nx
import numpy as np
import pandas as pd
from random import *
import time
import logging
from matplotlib.font_manager import FontProperties
import xlsxwriter
from openpyxl import load_workbook
from xlsxwriter import Workbook
import matplotlib

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

rca_threshold=1.8


matplotlib.rcParams['font.sans-serif'] = ['Arial']
#rca_thresholds = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6,
#                  1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3,
#                  2.4,2.5,2.6,2.7,2.8,2.9,3]
rca_thresholds = [1.5]
#equations = "score1-5"
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

time_start = time.time()

edge_weight_manipulte = 3
for m in range(len(data_types)):

    for rca_threshold in rca_thresholds:

        fig = plt.figure(figsize=(5,5))

        f_weights = 'D:\\pydata\\data\\jiyingru\\%s\\weights_number_min_%.1f.csv' % (data_types[m], rca_threshold)
        f_fig = 'D:\\pydata\\data\\jiyingru\\%s\\figs\\fig_%.1f.png' % (data_types[m], rca_threshold)

        logger.info("Data:%s,RCA:%.1f" % (data_types[m],rca_threshold))

        logger.info("loading data...")

        df= pd.read_csv(f_weights)

        country_quest_phi_weight_network = df.loc[::, ['QA', 'QB', 'weights']]
        time_end = time.time()



        #
        #rows = 2
        #cols = 2
        #k=0

         #   k+=1

        data = df.values.tolist()

        g = nx.Graph()
        for i in range(len(data)):
            g.add_edge(data[i][0], data[i][1], weight=data[i][2])
        logger.info('Questions:%d,nodes/edges:%d/%d, time:%d s',  len(questions[m]),len(g.nodes), len(g.edges),time_end - time_start)
        #plt.subplot(rows, cols, k)

        edgewidth = [g.get_edge_data(*e)['weight']*edge_weight_manipulte for e in g.edges()]

     #   plt.xlabel('\u5e73\u5747\u503c')

    #   plt.rcParams['font.family'] = 'SimSun'
        nx.draw(g,pos=nx.spring_layout(g),
                node_color='r',
                edge_color='b',
                with_labels = True,
                node_size = 150,
                font_size=3,
                width =edgewidth )

    #    mpl.rcParams['font.']=['times-new-roman']
        #plt.title("RCA = %.1f" % rca_threshold)
        # plt.title("ss", fontsize=100)
        fig.suptitle(f"RCA = {rca_threshold:.1f}")
        # plt.axis("off")

        # plt.savefig(f'./{rca_threshold}.png', dpi=800)
        plt.savefig(f_fig, dpi=800)

        logger.info("One figure obtained...time:%d s'", time_end - time_start)

