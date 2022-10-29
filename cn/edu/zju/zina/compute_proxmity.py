import matplotlib.pyplot as plt
import math
import dijkstra_distance

import networkx as nx
import numpy as np
import pandas as pd
from random import *
import time
import logging


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

f1 = 'D:\\py\\data\\zinan\\Data_for_Digital_Proximity.xlsx'
f_weights = 'D:\\py\\data\\zinan\\weights_number_max.xlsx'
f_primixity = "D:\\py\\data\\zinan\\primixity_max.xlsx"

logger.info("loading data:")
time_start=time.time()

df = pd.read_excel(f1)
df = df.loc[::, ['证券简称', 'year', '行业代码1', '行业代码2', '公司年总收入', '公司年产品收入'
                    , '收入占比']]
# logger.info(df['year'].value_counts())
data = df.values.tolist()
# logger.info(datas
#name = [data[i][0] for i in range(len(data))]
#name = list(set(name))
# logger.info(name)
year = [int(data[i][1]) for i in range(len(data))]
year = sorted(list(set(year)))
#code = [data[i][3] for i in range(len(data))]


# logger.info(year)

current_year =2011

df_one_year=[]
industry_weights = pd.read_excel(f_weights)
company_promixity = pd.DataFrame(columns=['证券简称', 'year', 'digital_proximity','digital_proximity_sales'])

for y in year:
    current_year = y
#    print("current running year:", y)
    time_end = time.time()
    logger.info('current running year: %d, time past:%d s', y, time_end - time_start)
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
        #construct company_codes_sales in certain year
        for i in range(len(data_one_year)):
            c = data_one_year[i][2] + str(data_one_year[i][3])
            company = data_one_year[i][0]
            sales= data_one_year[i][5] #某产品年收入

           # company_codes[company][c] = sales

            if (company_codes.get(company) == None):
                 #company_codes[company] =  [c]
                 code_sales={}
                 code_sales[c] = sales
                 company_codes[company] = code_sales
            else:
                company_codes[company][c]=sales

       # print(company_codes)

        # construct code_code matrix by dict in certain year
        graph = {}
        for c in codes:
            graph[c] = {}
        #direct iterates for dataframe
        for _, row in industry_weights_one_year.iterrows():
            code1 = row['行业代码1']
            code2 = row['行业代码2']
#            logger.info("%s, %s, %lf"code1,code2,row['weights'])
            weight =math.log(1/row['weights'])

            c1=graph.get(code1)
            c1[code2] = weight
            graph[code1]=c1

            c2 = graph.get(code2)
            c2[code1] = weight
            graph[code2] = c2
        # logger.info(graph)


        #caluclating code-code distance....
        logger.info("\tcaluclating distance")
        code_digital_proxmity = {}
        for c in codes:
            parent_dict, distance_dict = dijkstra_distance.dijkstra(graph, c)
 #           logger.info(graph)
            it_dict={}
            max_dist=0
            for key,value in distance_dict.items():
                if("I" in key and value != float("inf")):
                    it_dict[key] = value
                   # logger.info(c, key,value)
            #logger.info(it_dict)
            #exit(0)
            if(len(it_dict)>0):
                max_distance_code = max(it_dict, key=lambda x: it_dict[x])
                max_dist = it_dict[max_distance_code]
            else:
                max_dist = float("inf")
            code_digital_proxmity[c]= 1/(1+max_dist)

        #caluclating proxmity....
        logger.info("\tcaluclating proxmity")
        k = 0
        for k in range(len(companies)):
            proximity = 0
            proximity_sales = 0
            for code, sales in company_codes.get(companies[k]).items():
                proximity = proximity + code_digital_proxmity[code]
                proximity_sales = proximity_sales + code_digital_proxmity[code] * sales
            company_promixity.loc[len(company_promixity)] = \
                [companies[k], current_year,
                 proximity / len(company_codes.get(companies[k])),proximity_sales / len(company_codes.get(companies[k]))]
            k = k+ 1

        #exit(0)



  #这里暂停

  #caluclating proxmity....
logger.info("writing results to file..")
company_promixity.to_excel(f_primixity,index=False)
time_end = time.time()
logger.info('The end,cost time:%d s', time_end - time_start)


#df_one_year2= df_one_year.loc[(df_one_year['行业代码1'] == 'J') & (df_one_year['行业代码2'] == 66)]