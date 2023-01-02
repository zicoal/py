import matplotlib.pyplot as plt
import math

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
f_rca= 'D:\\py\\data\\zinan\\rca_number.xlsx'
f_weights = 'D:\\py\\data\\zinan\\weights_number_max.xlsx'

logger.info("loading data...")
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

current_year =2012

df_one_year=[]
company_code_part = pd.DataFrame(columns=['证券简称', 'year', '行业代码', 'RCA'])
industry_weights = pd.DataFrame(columns=['行业代码1', '行业代码2', 'year', 'weights'])

for y in year:
    current_year = y
    time_end = time.time()
    logger.info('current running year: %d, time past:%d s', y, time_end - time_start)
    if (y==current_year):
        df_one_year = df.loc[df['year'] == y]
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
            #logger.info(c,code_company.get(c))

        #logger.info(data_one_year)

        #计算RCA
        for i in range(len(data_one_year)):
            #company_code_part[data_one_year[i][0]]=
            #cols = df_one_year.shape[1] #列数
           # logger.info(cols)
            code1 = data_one_year[i][2] + str(data_one_year[i][3])
            company_part = data_one_year[i][6] #产品年收入
            #binary computing RCA
            rca = 1 if company_part/(code_part[code1]*100) >=1 else 0
            company_code_part.loc[len(company_code_part)] = [data_one_year[i][0],current_year,code1,rca]

            ####此处暂停
            if rca == 1:
                list_companies=code_company.get(code1)
                list_companies.append(data_one_year[i][0])
                code_company[code1]=list_companies

        #计算phi
        for i in range(len(codes)-1):
            for j in range(i+1, len(codes)):
                set_companies = set(code_company[codes[i]]) & set(code_company[codes[j]])
                #@Todo
                if (len(set_companies)>0):
                    phi_ij = len(set_companies) / len(code_company[codes[j]])
                    phi_ji = len(set_companies) / len(code_company[codes[i]])
                    phi_max = phi_ij if phi_ij > phi_ji else phi_ji
                    industry_weights.loc[len(industry_weights)] = [codes[i], codes[j], current_year, phi_max]
                else:
                    industry_weights.loc[len(industry_weights)] = [codes[i], codes[j], current_year, 0]


        #for c in code:
        #    d = company_code_part.loc[(company_code_part['行业代码'] == 'J')]
        #    for c
logger.info("writing results to file..")
industry_weights.to_excel(f_weights,index=False)
company_code_part.to_excel(f_rca,index=False)
time_end = time.time()
logger.info('The end,cost time:%d s', time_end - time_start)
#logger.info(code_company)
        #    logger.info(c+":"+str(code_part[c]))
        #logger.info(sum(code_part.values()))
        #for company_industry in data_one_year:
#logger.info(company_code_part.loc[0:10])
#logger.info(df_one_year)

#df_one_year2= df_one_year.loc[(df_one_year['行业代码1'] == 'J') & (df_one_year['行业代码2'] == 66)]
#logger.info(df_one_year2)
'''

'''