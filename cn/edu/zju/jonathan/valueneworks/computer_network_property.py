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
from cn.edu.tools import gini

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

rca_threshold=2.1
#equations = "score1-5"
equations = "eq-nonlinear"


#get the mapped score
def getscore (x):
    b = 6
    c = 10
    return x**2 - b*x +c

#logger.info(getscore(5))
#exit(0)


f_country_value= 'D:\\py\\data\\jonathan\\%s\\country_network_Gini_%.1f.xlsx' % (equations, rca_threshold)
f_weights = 'D:\\py\\data\\jonathan\\%s\\weights_number_min_%.1f.xlsx' % (equations, rca_threshold)
add_column_name = 'rca=%d' % rca_threshold
logger.info("RCA:%.1f,Equation:%s" % (rca_threshold,equations))
country_value = pd.DataFrame(columns=["country", 'value'])
if os.path.isfile(f_country_value)==False:

    writer = pd.ExcelWriter(f_country_value)
    country_value.to_excel(writer,  index=False)
    writer.save()
    writer.close()


logger.info("loading data...")
time_start=time.time()
df = pd.read_csv(f_weights)
#df = pd.read_excel(f1)
#df = df.loc[::, ['id','country', 'q1', 'q2', 'q3', 'q4',
#                 'q5', 'q6', 'q7', 'q8',
#                 'q9', 'q10', 'q11', 'q12',
#                 'q13', 'q14', 'q15', 'q16']]
#df_code= pd.read_excel(f_code)
#df_code = df_code.loc[::, ['q', 'answer', 'coded_value']]

time_end = time.time()

logger.info("data loaded...time cost:%d s'", time_end - time_start)
countries = {}
data = df.values.tolist()
countries = [data[i][0] for i in range(len(data))]
countries = sorted(list(set(countries)))

#logger.info(data[0])
#logger.info(data[1])
#logger.info(data[2])
#exit(0)

#logger.info(countries)
#logger.info("total # of countries: %d", len(countries))
#logger.info(countries)
#exit(0)
#code = [data[i][3] for i in range(len(data))]

#embbing answers to numerical values
#answer_values ={}
#data_answers = df_code.values.tolist()
#for i in range(len(data_answers)):
#   q = data_answers[i][0]
#   answer= data_answers[i][1]
#   coded_value= data_answers[i][2]
#   if(answer_values.get(q)==None):
#       answer_values[q]={}
#   answer_values[q][answer] = coded_value

#logger.info(answer_values)
#exit(0)

country_weights=[]
for country in countries:
    df_one_country = df.loc[df['country'] == country]
    weights = [df_one_country[i][3] for i in range(len(df_one_country))]
    country_weights.append( gini.gini_coefficient(weights))
    #country_value.loc[len(country_value)] =[country,weight]

df1 = pd.read_excel(f_country_value)
col_names  = df1.columns. tolist()
col_names.append(add_column_name)
df1.reindex(columns= col_names)
df1[add_column_name]=country_weights
df1.to_excel(f_country_value)


'''
writer2 = pd.ExcelWriter(f_country_value, engine='openpyxl', mode='a', if_sheet_exists='overlay')
book = load_workbook(f_country_value)
writer2.book = book
writer2.sheets = dict((ws.title, ws) for ws in book.worksheets)
df2 = pd.DataFrame(pd.read_excel(f_country_value, sheet_name='Sheet1'))
df_rows2 = df2.shape[0]
country_value.to_excel(writer2, sheet_name='Sheet1', startrow=df_rows2 + 1, index=False, header=False)
writer2.save()
writer2.close()
'''


time_end = time.time()
logger.info('The end,cost time:%d s', time_end - time_start)
