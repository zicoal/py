import matplotlib.pyplot as plt
import math

import networkx as nx
import numpy as np
import pandas as pd
from random import *
import time

f1 = 'D:\\py\\data\\zinan\\Data_for_Digital_Proximity.xlsx'
f_rca= 'D:\\py\\data\\zinan\\rca_number.xlsx'
f_weights = 'D:\\py\\data\\zinan\\weights_number_max.xlsx'

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
company_code_part = pd.DataFrame(columns=['证券简称', 'year', '行业代码', 'RCA'])
industry_weights = pd.DataFrame(columns=['行业代码1', '行业代码2', 'year', 'weights'])

for y in year:
    current_year = y
    if (y==current_year):
        df_one_year = df.loc[df['year'] == current_year]
        data_one_year = df_one_year.values.tolist()
        code = [data_one_year[i][2] + str(data_one_year[i][3]) for i in range(len(data_one_year))]
        df_one_year.insert(loc=len(df_one_year.columns), column='行业代码', value=code)
        companies = [data_one_year[i][0] for i in range(len(df_one_year))]
        companies = sorted(list(set(companies))) #去重
        codes = sorted(list(set(code))) #去重
        code_part={}
        sum_all= df_one_year['公司年产品收入'].sum()
        code_company = {}
        for c in code:
            code_part[c] =  df_one_year.loc[(df_one_year['行业代码'] == c)]['公司年产品收入'].sum()/sum_all
            code_company[c]=[]
            #print(c,code_company.get(c))

        #print(data_one_year)

        #计算RCA
        for i in range(len(data_one_year)):
            #company_code_part[data_one_year[i][0]]=
            #cols = df_one_year.shape[1] #列数
           # print(cols)
            code1 = data_one_year[i][2] + str(data_one_year[i][3])
            company_part = data_one_year[i][6] #产品年收入
            #binary computing RCA
            rca = 1 if company_part/(code_part[code1]*100) >=1 else 0
            company_code_part.loc[i] = [data_one_year[i][0],current_year,code1,rca]

            ####此处暂停
            if rca == 1:
                list_companies=code_company.get(code1)
                list_companies.append(data_one_year[i][0])
                code_company[code1]=list_companies
        k = 0
        #计算phi
        for i in range(len(codes)-1):
            for j in range(i+1, len(codes)):
                set_companies = set(code_company[codes[i]]) & set(code_company[codes[j]])
                if (len(set_companies)>0):
                    phi_ij = len(set_companies) / len(code_company[codes[j]])
                    phi_ji = len(set_companies) / len(code_company[codes[i]])
                    phi_max = phi_ij if phi_ij > phi_ji else phi_ji
                    industry_weights.loc[k] = [codes[i], codes[j], current_year, phi_max]
                    k = k+1

        #for c in code:
        #    d = company_code_part.loc[(company_code_part['行业代码'] == 'J')]
        #    for c
industry_weights.to_excel(f_weights,index=False)
company_code_part.to_excel(f_rca,index=False)
#print(code_company)
        #    print(c+":"+str(code_part[c]))
        #print(sum(code_part.values()))
        #for company_industry in data_one_year:
#print(company_code_part.loc[0:10])
#print(df_one_year)

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