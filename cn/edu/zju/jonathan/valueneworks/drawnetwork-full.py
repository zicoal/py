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
from community import community_louvain


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
equations = ["eq-nonlinear","eq-linear"]
weighted = ["unweighted","weighted"]




#f_code= 'D:\\py\\data\\jonathan\\weights_number_min_%.1f.xlsx' % rca_threshold



logger.info("loading data...")
time_start=time.time()
questions=['q1', 'q2', 'q3', 'q4',
                 'q5', 'q6', 'q7', 'q8',
                 'q9', 'q10', 'q11', 'q12',
                 'q13', 'q14', 'q15', 'q16']


#rca_thresholds = [1, 1.1, 1.2,  1.4, 1.5, 1.6]
rca_thresholds = [1.9]

f1 = 'D:\\pydata\\data\\jonathan\\MCS_recoded.csv'



#country_paticipant_quest_rca = pd.DataFrame(columns=["country", 'id', 'Q', 'RCA'])
##countries = sorted(list(set(countries)))


show_countries = ['Germany', "South Africa",'Hong Kong','Australia',"United States","United Kingdom"]

colors = ["orange","skyblue","green","gray","deeppink","violet"]


logger.info(show_countries)


rows = 2
cols = round(len(show_countries) / rows)


str_linears=["[f(x)=x]","[$f(x) = x^2-6x+10$]"]


f_dir ='D:\\pydata\\data\\jonathan\\%s\\weights_number_min_%.1f.csv'



f_figs_dir ='D:\\pydata\\data\\jonathan\\results\\rca_based\\figs\\networks\\fig_%s_%s_rca_%.1f.png'
f_prefix ="country_network_"
colors = ['DeepPink', 'orange', 'DarkCyan', '#A0CBE2', '#3CB371', 'b', 'orange', 'y', 'c', '#838B8B', 'purple',
          'olive', '#A0CBE2', '#4EEE94'] * 500




edge_weight_manipulte =2
e = 0

for equation in equations:

     network_property = str_linears[e]

     network_property_old = equation
     e += 1
     for rca_threshold in rca_thresholds:

       f1 = f_dir  % (network_property_old, rca_threshold)
       df = pd.read_csv(f1)

#       countries = {}
       #       countries = [data[i][0] for i in range(len(data))]
       country_quest_phi_weight_network = df.loc[::, ["country", 'QA', 'QB', 'weights']]
       data = df.values.tolist()

       for w in weighted:
           f_fig = f_figs_dir % (network_property_old,w, rca_threshold)
           k = 0
           for c in show_countries:
                k+=1
                df_one_country = df.loc[df['country'] == c]
                data_one_country = df_one_country.values.tolist()
                g = nx.Graph()
                #logger.info('Country: %s(%d/%d),nodes/edges:%d/%d, time:%d s', c, k, len(countries),len(g.nodes), len(g.edges),time_end - time_start)
                plt.subplot(rows, cols, k)
                com=None

                if (w =="unweighted"):
                    for i in range(len(data_one_country)):
                        g.add_edge(data_one_country[i][1], data_one_country[i][2])
                    com = community_louvain.best_partition(g)
                else:
                    for i in range(len(data_one_country)):
                        g.add_edge(data_one_country[i][1], data_one_country[i][2], weight=data_one_country[i][3])
                    com = community_louvain.best_partition(g,weight='weight')

                # 节点大小设置，与度关联
                node_size = [g.degree(i) ** 1 * 5 for i in g.nodes()]
                # 格式整理
                df_com = pd.DataFrame({'Group_id': com.values(),
                                       'object_id': com.keys()}
                                      )

                df_com.groupby('Group_id').count().sort_values(by='object_id', ascending=False)

                # 颜色设置
                colors = [colors[i] for i in com.values()]
                edgewidth=None

                if (w == "unweighted"):
                    edgewidth = [edge_weight_manipulte for e in g.edges()]
                else:
                    edgewidth = [g.get_edge_data(*e)['weight']*edge_weight_manipulte for e in g.edges()]

#                nx.draw(g,pos=nx.spring_layout(g),
#                        node_color='r',
#                        edge_color='b',
#                        with_labels = True,
#                        node_size = 100,
#                        font_size=5,
#                        width =edgewidth)
                nx.draw_networkx(g,
                                 pos=nx.spring_layout(g),
                                 node_color=colors,
                                 edge_color='#2E8B57',
                                 font_color='black',
                                 node_size=node_size,
                                 font_size=4,
                                 alpha=0.9,
                                 width=0.1,
                                 font_weight=0.9
                                 )
                plt.title(c)
            #plt.axis("off")
           xylims = plt.axis()
           min_xlim=xylims[0]
           min_ylim=xylims[2]
           plt.text(min_xlim-4, min_ylim-0.4,"RCA=%.1f,%s %s" % (rca_threshold,w, network_property), fontsize=13, color='b')
           plt.savefig(f_fig,dpi=800, bbox_inches='tight')
           plt.close()
           time_end =time.time()
           logger.info("File:%s，RCA_%.1f, %s, time:%d s", equation, rca_threshold, w,time_end - time_start)
           #exit(0)
#plt.show()
#nx.draw_networkx_nodes(graph, pos,
#    node_size=[len(v) * the_base_size for v in graph.nodes()],
#    node_color="w")

