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
#equations = ["eq-nonlinear"]
#weighted = ["unweighted"]

equations = ["eq-linear","eq-nonlinear"]
weighted = ["weighted"]




logger.info("loading data...")
time_start=time.time()
questions_original = ['q1', 'q2', 'q3', 'q4',
             'q5', 'q6', 'q7', 'q8',
             'q9', 'q10', 'q11', 'q12',
             'q13', 'q14', 'q15', 'q16']

questions = ['q1', 'q2', 'q4', 'q5',
              'q6', 'q7', 'q8','q9',
             'q10', 'q11', 'q12', 'q15']

#rca_thresholds = [1, 1.1, 1.2,  1.4, 1.5, 1.6]
rca_thresholds = [1.4,1.5,1.6]
#rca_thresholds = [1.0]

f1 = 'D:\\pydata\\data\\jonathan\\MCS_recoded.csv'



#country_paticipant_quest_rca = pd.DataFrame(columns=["country", 'id', 'Q', 'RCA'])
##countries = sorted(list(set(countries)))


#show_countries = ['Germany', "France",'Sweden','Croatia',"Iraq","Zambia","Hong Kong","United States","United Kingdom"]
show_countries = ['Germany', "France",'Sweden','Croatia',"Zambia","South Africa","Iraq","Hong Kong","India","Japan", "United States","United Kingdom",]
#show_countries = ["Zambia","United States",'Germany' ]



logger.info(show_countries)


rows = 3
cols = round(len(show_countries) / rows)


str_linears=["[f(x)=x]","[$f(x) = (x-3)^2+1$]"]


f_dir ='D:\\pydata\\data\\jonathan\\%s\\q%d\\weights_number_min_%.1f.csv'



f_figs_dir =f'D:\\pydata\\data\\jonathan\\results\\rca_based\\q{len(questions)}\\figs\\networks\\fig_%s_%s_rca_%.1f.png'
f_prefix ="country_network_"
colors = ['DeepPink', 'orange', 'DarkCyan', 'b', '#3CB371',  'y', 'c', '#A0CBE2', '#838B8B', 'purple',
          'olive', '#A0CBE2', '#4EEE94'] * 500


edge_weight_manipulte =2
node_weight_manipulte =5
e = 0

for equation in equations:

     network_property = str_linears[e]

     network_property_old = equation
     e += 1
     for rca_threshold in rca_thresholds:

       f1 = f_dir  % (network_property_old, len(questions),rca_threshold)
       df = pd.read_csv(f1)
#       print(f1)
#       countries = {}
       #       countries = [data[i][0] for i in range(len(data))]
       country_quest_phi_weight_network = df.loc[::, ["country", 'QA', 'QB', 'weights']]
       data = df.values.tolist()

       for w in weighted:
           f_fig = f_figs_dir % (network_property_old,w, rca_threshold)
           k = 0
           fig = plt.figure(figsize=(22,18));   plt.clf()
           fig, ax = plt.subplots(nrows=rows, ncols=cols, num=1)
#           plt.subplot(rows, cols, k)
           for c in show_countries:

                df_one_country = df.loc[df['country'] == c]
                data_one_country = df_one_country.values.tolist()
                g = nx.Graph()
                for q_node in questions:
                    g.add_node(f"q{questions.index(q_node)+1}")
                time_end =time.time()
                com=None

                if (w =="unweighted"):
                    for i in range(len(data_one_country)):
                        g.add_edge(f"q{questions.index(data_one_country[i][1])+1}", f"q{questions.index(data_one_country[i][2])+1}")
    #                    g.add_edge(data_one_country[i][1], data_one_country[i][2])
                    com = community_louvain.best_partition(g)
                else:
                    for i in range(len(data_one_country)):
                        g.add_edge(f"q{questions.index(data_one_country[i][1])+1}", f"q{questions.index(data_one_country[i][2])+1}", weight=data_one_country[i][3])
#                       g.add_edge(data_one_country[i][1], data_one_country[i][2], weight=data_one_country[i][3])
                    com = community_louvain.best_partition(g,weight='weight')

                # 格式整理
                df_com = pd.DataFrame({'Group_id': com.values(),
                                       'object_id': com.keys()}
                                      )

                df_com.groupby('Group_id').count().sort_values(by='object_id', ascending=False)

                # 颜色设置
                node_colors = [colors[i] for i in com.values()]

                #print(f1)
#                print(f"{c},{com}")
#                print(node_colors)

                # 节点和边大小设置，与度、及点关联
                node_size = []
                edgewidth=None

                if (w == "unweighted"):
                    edgewidth = [edge_weight_manipulte * 0.1 for e in g.edges()]
                    node_size = [g.degree(i) * node_weight_manipulte for i in g.nodes()]
                else:
                    edgewidth = [g.get_edge_data(*e)['weight']*edge_weight_manipulte for e in g.edges()]
                    for cuurent_node in g.nodes:
                        t_nodesize =0
                        for nb_edge in g.edges(cuurent_node):
                            t_nodesize += g[nb_edge[0]][nb_edge[1]]['weight']
                        node_size.append(t_nodesize * node_weight_manipulte*40)
                ix = np.unravel_index(k, ax.shape)
                plt.sca(ax[ix])
                nx.draw_networkx(g, pos=nx.circular_layout(g),
                         node_color=node_colors,
                         edge_color='#2E8B57',
                         with_labels=True,
                         font_color='black',
                         font_size=8,
                         alpha=0.9,
                         node_size=node_size,
                         width=edgewidth,
                         font_weight=0.9,
                         font_family = 'sans-serif',
                         ax=ax[ix])
                ax[ix].set_title(c, fontsize=20)
                ax[ix].set_axis_off()
                k += 1

            #plt.axis("off")
           xylims = plt.axis()
           min_xlim=xylims[0]
           min_ylim=xylims[2]
           plt.text(min_xlim-4, min_ylim,"RCA=%.1f,%s %s" % (rca_threshold,w, network_property), fontsize=18, color='b')
           plt.savefig(f_fig,dpi=800, bbox_inches='tight')
           plt.close()
           time_end =time.time()
           logger.info("File:%s，RCA_%.1f, %s, time:%d s", equation, rca_threshold, w,time_end - time_start)
           #exit(0)
#plt.show()
#nx.draw_networkx_nodes(graph, pos,
#    node_size=[len(v) * the_base_size for v in graph.nodes()],
#    node_color="w")

