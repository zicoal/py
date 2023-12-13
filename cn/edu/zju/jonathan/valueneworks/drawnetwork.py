import matplotlib
matplotlib.use('TkAgg')
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
#equations = "score1-5"
equations = "eq-nonlinear"

f1 = 'D:\\pydata\\data\\jonathan\\Climat_Survey_2022_marapril_microdata.xlsx'
f_code= 'D:\\pydata\\data\\jonathan\\code.xlsx'
f_rca= 'D:\\pydata\\data\\jonathan\\%s\\rca_number_%.1f.csv' % (equations, rca_threshold)
f_weights = 'D:\\pydata\\data\\jonathan\\%s\\weights_number_min_%.1f.csv' % (equations, rca_threshold)
f_fig = 'D:\\pydata\\data\\jonathan\\%s\\figs\\fig_%.1f.png' % (equations, rca_threshold)
#f_code= 'D:\\py\\data\\jonathan\\weights_number_min_%.1f.xlsx' % rca_threshold

logger.info("RCA:%.1f,Equation:%s" % (rca_threshold,equations))

logger.info("loading data...")
time_start=time.time()
questions=['q1', 'q2', 'q3', 'q4',
                 'q5', 'q6', 'q7', 'q8',
                 'q9', 'q10', 'q11', 'q12',
                 'q13', 'q14', 'q15', 'q16']
#df = pd.read_excel(f1)
#df = df.loc[::, ['id','country', 'q1', 'q2', 'q3', 'q4',
#                 'q5', 'q6', 'q7', 'q8',
#                 'q9', 'q10', 'q11', 'q12',
#                 'q13', 'q14', 'q15', 'q16']]

df= pd.read_csv(f_weights)

#country_paticipant_quest_rca = pd.DataFrame(columns=["country", 'id', 'Q', 'RCA'])
country_quest_phi_weight_network = df.loc[::, ["country", 'QA', 'QB', 'weights']]
time_end = time.time()

logger.info("data loaded...time cost:%d s'", time_end - time_start)
countries = {}
data = df.values.tolist()
countries = [data[i][0] for i in range(len(data))]
##countries = sorted(list(set(countries)))

countries = ['Germany', "Algeria",'Armenia','Austria']

logger.info(len(countries))
logger.info(countries)

rows = 2
cols = 2
k=0

edge_weight_manipulte =1
for c in countries:
    k+=1
    df_one_country = df.loc[df['country'] == c]
    data_one_country = df_one_country.values.tolist()
    g = nx.Graph()
    for i in range(len(data_one_country)):
        g.add_edge(data_one_country[i][1],data_one_country[i][2],weight=data_one_country[i][3])

    logger.info('Country: %s(%d/%d),nodes/edges:%d/%d, time cost:%d s', c, k, len(countries),len(g.nodes), len(g.edges),time_end - time_start)
    plt.subplot(rows, cols, k)

    edgewidth = [g.get_edge_data(*e)['weight']*edge_weight_manipulte for e in g.edges()]

    nx.draw(g,pos=nx.spring_layout(g),
            node_color='r',
            edge_color='b',
            with_labels = True,
            node_size = 100,
            font_size=5,
            width =edgewidth)
    plt.title(c)

plt.axis("off")
plt.savefig(f_fig,dpi=800)
#plt.show()
#nx.draw_networkx_nodes(graph, pos,
#    node_size=[len(v) * the_base_size for v in graph.nodes()],
#    node_color="w")

