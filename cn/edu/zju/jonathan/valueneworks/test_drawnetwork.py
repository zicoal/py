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
from matplotlib.font_manager import FontProperties
import xlsxwriter
from openpyxl import load_workbook
from xlsxwriter import Workbook
import matplotlib
import networkx as nx
from community import community_louvain

logger = logging.getLogger()
logger.setLevel(logging.INFO)
# 定义handler的输出格式
# logger to console
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
# fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(ch)

rca_threshold = 1.8

matplotlib.rcParams['font.sans-serif'] = ['Arial']
#rca_thresholds = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6,
#                  1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3,
#                  2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3]
rca_thresholds = [1.5]
# equations = "score1-5"
data_types = ["eq-linear", 'eq-nonlinear']
data_files = ['ESGstudy1Data', 'ESGstudy2Data']


time_start = time.time()
show_countries = ['Germany', "South Africa", 'Hong Kong', 'Australia', "United States", "United Kingdom"]

edge_weight_manipulte = 5
for m in range(len(data_types)):

    for rca_threshold in rca_thresholds:

        fig = plt.figure(figsize=(5, 5))

        f_weights = 'D:\\pydata\\data\\jonathan\%s\\weights_number_min_%.1f.csv' % (data_types[m], rca_threshold)

        logger.info("Data:%s,RCA:%.1f" % (data_types[m], rca_threshold))

        logger.info("loading data...")

        df = pd.read_csv(f_weights)

        country_quest_phi_weight_network = df.loc[::, ['QA', 'QB', 'weights']]
        time_end = time.time()

        for country in show_countries:

            f_fig = 'D:\\pydata\\data\\jonathan\\%s\\figs\\fig_%s_%.1f.png' % (data_types[m], country, rca_threshold)
           # print(f_fig)
            df_one_country = df.loc[df['country'] == country]

            data = df_one_country.values.tolist()
            g = nx.Graph()
            for i in range(len(data)):
                g.add_edge(data[i][1], data[i][2], weight=data[i][3])
#            logger.info('Questions:%d,nodes/edges:%d/%d, time:%d s', len(questions[m]), len(g.nodes), len(g.edges),
#                        time_end - time_start)
            com = community_louvain.best_partition(g)
            # 节点大小设置，与度关联
            node_size = [g.degree(i) ** 1 * 5 for i in g.nodes()]
            # 格式整理
            df_com = pd.DataFrame({'Group_id': com.values(),
                                   'object_id': com.keys()}
                                  )

            #        edgewidth = [g.get_edge_data(*e)['weight']*edge_weight_manipulte for e in g.edges()]
            df_com.groupby('Group_id').count().sort_values(by='object_id', ascending=False)

            # 颜色设置
            colors = ['DeepPink', 'orange', 'DarkCyan', '#A0CBE2', '#3CB371', 'b', 'orange', 'y', 'c', '#838B8B',
                      'purple',
                      'olive', '#A0CBE2', '#4EEE94'] * 500
            colors = [colors[i] for i in com.values()]

            #   plt.rcParams['font.family'] = 'SimSun'

            nx.draw_networkx(g,
                             pos=nx.spring_layout(g),
                             node_color=colors,
                             edge_color='#2E8B57',
                             font_color='black',
                             node_size=node_size,
                             font_size=5,
                             alpha=0.9,
                             width=0.1,
                             font_weight=0.9
                             )
            fig.suptitle(f"{country},RCA = {rca_threshold:.1f}")
            plt.savefig(f_fig, dpi=800)
            plt.close()
        '''
        nx.draw(g,pos=nx.spring_layout(g),
                node_color='r',
                edge_color='b',
                with_labels = True,
                node_size = 150,
                font_size=3,
                width =edgewidth )
        '''

        logger.info("One figure obtained...time:%d s'", time_end - time_start)
