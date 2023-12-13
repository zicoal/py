import matplotlib
matplotlib.use('TkAgg')
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

#font_path=r"c:\windows\fonts\simsun.ttc"
#font = FontProperties(fname=font_path, size=10)

mpl_fonts = set(f.name for f in FontManager().ttflist)
matplotlib.rc("font", family='SimSun')

#print('all font list get from matplotlib.font_manager:')
#for f in sorted(mpl_fonts):
#    print('\t' + f)
rca_thresholds = [1,2]
#equations = "score1-5"
question_type = "data1"
questions = [
         'Q3_1','Q3_2','Q3_3','Q3_4','Q4_1','Q4_2','Q4_3','Q4_4','Q4_5',
         'Q5_1','Q5_2','Q5_3','Q5_4','Q5_5','Q6_1','Q6_2','Q6_3',
         'Q7_1','Q7_2','Q7_3','Q7_4','Q7_5','Q7_6','Q7_7','Q7_8	',
         'Q8_1','Q8_2','Q8_3','Q8_4','Q8_5','Q8_6',
         'Q9_1','Q9_2','Q9_3','Q9_4','Q9_5','Q9_6',
         'Q10_1','Q10_2','Q10_3','Q11_1','Q11_2','Q11_3',
         'Q12_1','Q12_2','Q12_3','Q13_1','Q13_2','Q13_3','Q13_4','Q13_5','Q13_6','Q13_7',
         'Q14_1','Q14_2','Q14_3','Q14_4','Q14_5','Q14_6','Q14_7','Q14_8','Q14_9',
         'Q15_1','Q15_2','Q15_3','Q15_4','Q15_5','Q15_6',
         'Q16_1','Q16_2','Q16_3','Q16_4','Q16_5','Q16_6','Q16_7','Q17']

edge_weight_manipulte = 3

for rca_threshold in rca_thresholds:
    f_weights = 'D:\\pydata\\data\\jiyingru\\%s\\weights_number_min_%.1f.csv' % (question_type, rca_threshold)
    f_fig = 'D:\\pydata\\data\\jiyingru\\%s\\figs\\fig_%.1f.png' % (question_type, rca_threshold)
    #f_code= 'D:\\py\\data\\jonathan\\weights_number_min_%.1f.xlsx' % rca_threshold

    logger.info("RCA:%.1f,Equation:%s" % (rca_threshold,question_type))

    logger.info("loading data...")
    time_start=time.time()

    df= pd.read_csv(f_weights)

    country_quest_phi_weight_network = df.loc[::, ['QA', 'QB', 'weights']]
    time_end = time.time()

    logger.info("data loaded...time:%d s'", time_end - time_start)


    #
    #rows = 2
    #cols = 2
    #k=0

     #   k+=1

    data = df.values.tolist()

    g = nx.Graph()
    for i in range(len(data)):
        g.add_edge(data[i][0], data[i][1], weight=data[i][2])
    logger.info('Questions:%d,nodes/edges:%d/%d, time:%d s',  len(questions),len(g.nodes), len(g.edges),time_end - time_start)
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
   #plt.title("rca = %.1f" % rca_threshold)
    #    plt.axis("off")
   # plt.show()
    plt.savefig(f_fig,dpi=800)

