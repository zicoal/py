import matplotlib.pyplot as plt
import math
import dijkstra_distance

import networkx as nx
import numpy as np
import pandas as pd
from random import *
import time

f1 = 'D:\\py\\data\\zinan\\Data_for_Digital_Proximity.xlsx'
f_weights = 'D:\\py\\data\\zinan\\weights_number_max.xlsx'
f_primixity = "D:\\py\\data\\zinan\\primixity_max.xls"

print("reading data:")
df = pd.read_excel(f1)
df = df.loc[::, ['证券简称', 'year', '行业代码1', '行业代码2', '公司年总收入', '公司年产品收入'
                    , '收入占比']]
# print(df['year'].value_counts())
data = df.values.tolist()
# print(datas
#name = [data[i][0] for i in range(len(data))]
#name = list(set(name))
# print(name)
year = [int(data[i][1]) for i in range(len(data))]
year = sorted(list(set(year)))
#code = [data[i][3] for i in range(len(data))]


# print(year)

current_year =2021

df_one_year=[]
industry_weights = pd.read_excel(f_weights)
company_promixity = pd.DataFrame(columns=['证券简称', 'year', 'proximity'])

for y in year:
    #current_year = y
    print("current running year:", y)
    if (y==current_year):
        industry_weights_one_year = industry_weights.loc[industry_weights['year'] == current_year]
        df_one_year = df.loc[df['year'] == current_year]
        data_one_year = df_one_year.values.tolist()
        code= [data_one_year[i][2] + str(data_one_year[i][3]) for i in range(len(data_one_year))]
        codes = sorted(list(set(code))) #去重
        df_one_year.insert(loc=len(df_one_year.columns), column='行业代码', value=code)
        companies = [data_one_year[i][0] for i in range(len(df_one_year))]
        companies = sorted(list(set(companies))) #去重
        company_codes = {}
        #construct company_codes in certain year
        for i in range(len(data_one_year)):
            c = data_one_year[i][2] + str(data_one_year[i][3])
            company = data_one_year[i][0]
            if (company_codes.get(company) == None):
                 company_codes[company] =  [c]
            else:
                cc = company_codes[company]
                cc.append(c)
                company_codes[company] = cc
        # print(company_codes)

        # construct code_code matrix by dict in certain year
        graph = {}
        code_digital_proxmity = {}
        for c in codes:
            graph[c] = {}
        for _, row in industry_weights.iterrows():
            code1 = row['行业代码1']
            code2 = row['行业代码2']
            weight = 1/math.log(row['weights'])

            c1=graph.get(code1)
            c1[code2] = weight
            graph[code1]=c1

            c2 = graph.get(code2)
            c2[code1] = weight
            graph[code2] = c2
        # print(graph)

        #这里暂停
        #caluclating distance....
        print("\tcaluclating distance")
        for c in codes:
            parent_dict, distance_dict = dijkstra_distance(graph, c)

        #caluclating proxmity....
        print("\tcaluclating proxmity")





#company_promixity.to_excel(f_primixity,index=False)


#df_one_year2= df_one_year.loc[(df_one_year['行业代码1'] == 'J') & (df_one_year['行业代码2'] == 66)]
#print(df_one_year2)
'''
nodes = {}

for i in range(len(data)):
    #current_year = int(data[i][1])
    # 暂时只计算最后一年的
    for y in range(data[i][1]):
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
'''