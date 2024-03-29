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

rca_thresholds = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6,
                  1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3,
                  2.4,2.5,2.6,2.7,2.8,2.9,3,3.1,
                  3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4,4.1]
rca_threshold = 2.1
#equations = "score1-5"
equations = ["eq-nonlinear","eq-linear"]

#logger.info(getscore(5))
#exit(0)


logger.info("program started...")

time_start = time.time()

for equation in equations:

    f_country_value= 'D:\\pydata\\data\\jonathan\\results\\rca_based\\country_network_gini_%s.xlsx' % equation

    f_weights = 'D:\\pydata\\data\\jonathan\\%s\\weights_number_min_%.1f.csv' % (equation, 1)

    df = pd.read_csv(f_weights)
    countries = []
    data = df.values.tolist()
    countries = [data[i][0] for i in range(len(data))]
    # delete bad rows with duplicate headers
    countries = sorted(list(set(countries)))
    #countries.remove("country")
    country_value = pd.DataFrame(columns=["country"])

    #delete old files
    if os.path.isfile(f_country_value):
        os.remove(f_country_value)

    writer = pd.ExcelWriter(f_country_value)
    for country in countries:
        country_value.loc[len(country_value)] = [country]
    country_value.to_excel(writer, index=False)
    writer.save()

    for rca_threshold in rca_thresholds:

        f_weights = 'D:\\pydata\\data\\jonathan\\%s\\weights_number_min_%.1f.csv' % (equation, rca_threshold)
        add_column_name = 'rca=%.1f' % rca_threshold

        df = pd.read_csv(f_weights)

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

            data_one_country = df_one_country.values.tolist()

            #empty
            if (len(df_one_country)==0):
                country_weights.append(-2)
            elif (len(df_one_country) == 1):
                    country_weights.append(-1)
            else:
                weights = [float(data_one_country[i][3]) for i in range(len(df_one_country))]
                #logger.info(country)
                country_weights.append(gini.gini_coefficient(weights))
            #country_value.loc[len(country_value)] =[country,weight]

        df1 = pd.read_excel(f_country_value)
        col_names  = df1.columns. tolist()
        col_names.append(add_column_name)
        df1.reindex(columns= col_names)
        df1[add_column_name]=country_weights
        df1.to_excel(f_country_value,index=False)

        time_end = time.time()
        logger.info("Equation:%s, RCA:%.1f, time:%d s" % (equation,rca_threshold,time_end - time_start))



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
logger.info('Program ended, total cost :%d s', time_end - time_start)