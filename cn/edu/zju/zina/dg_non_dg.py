import networkx as nx
import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd
from random import *
import time

f1 = 'D:\\py\\enterprise.xlsx'
f2 = 'D:\\py\\graph.csv'

df = pd.read_excel(f1)
df = df.loc[::, ['证券简称', 'year', '行业代码1', '行业代码2', 'income_total', 'income_dg_total'
                    , 'income_dg1', 'income_dg2', 'income_dg3', 'income_dg4', 'income_dg5']]
# print(df['year'].value_counts())
data = df.values.tolist()
# print(datas)
name = [data[i][0] for i in range(len(data))]
name = list(set(name))
# print(name)
year = [int(data[i][1]) for i in range(len(data))]
year = sorted(list(set(year)))
code = [data[i][3] for i in range(len(data))]
# print(year)

nodes = {}

for i in range(len(data)):
    current_year = int(data[i][1])
    # 暂时只计算最后一年的
    if (current_year == year[len(year) - 1]):
        info = {}
        info['year'] = int(data[i][1])
        info['code'] = data[i][2] + str(data[i][3])
        info['income_total'] = data[i][4]
        info['income_dg_total'] = data[i][5]
        info['income_dg_prop'] = data[i][5] / data[i][4]
        info['income_dg_prop_1'] = data[i][6] / data[i][4]
        info['income_dg_prop_2'] = data[i][7] / data[i][4]
        info['income_dg_prop_3'] = data[i][8] / data[i][4]
        info['income_dg_prop_4'] = data[i][9] / data[i][4]
        info['income_dg_prop_5'] = data[i][10] / data[i][4]
        nodes[data[i][0]] = info

edge_list = []
for key in nodes.keys():
    info = nodes.get(key)
    if (info['income_dg_prop_1'] > 0):
        edge_list.append((info['code'], 'dg1'))
    elif (info['income_dg_prop_2'] > 0):
        edge_list.append((info['code'], 'dg2'))
    elif (info['income_dg_prop_3'] > 0):
        edge_list.append((info['code'], 'dg3'))
    elif (info['income_dg_prop_4'] > 0):
        edge_list.append((info['code'], 'dg4'))
    elif (info['income_dg_prop_5'] > 0):
        edge_list.append((info['code'], 'dg5'))

g = nx.MultiGraph()
g.add_nodes_from(['dg1', 'dg2', 'dg3', 'dg4', 'dg5'])
g.add_edges_from(edge_list)
pos = nx.shell_layout(g)
# pos = nx.spring_layout(g)
nx.draw(g, pos, with_labels=True, node_size=200, width=0.6)
plt.show()

# g = nx.Graph()
# plt.figure(figsize=(20,5))

# 也可以
# list = [('a','b',5.0),('b','c',3.0),('a','c',1.0)]
# g.add_weight_edges_from(list)

# nx.draw(g)
# plt.show()
