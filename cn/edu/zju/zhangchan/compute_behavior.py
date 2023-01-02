import matplotlib.pyplot as plt
import math

import networkx as nx
import numpy as np
import pandas as pd
from random import *
import time
import logging
import compute_area


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

f1 = 'D:\\py\\data\\zhangchan\\pagelevel.csv'
f_weights = 'D:\\py\\data\\zhangchan\\user_behavior.csv'

logger.info("loading data...")
time_start=time.time()
df = pd.read_csv(f1)
df = df.loc[::, ['id', 'page', 'length', 'startTime']]
#logger.info(df['id'].value_counts())

data = df.values.tolist()
# logger.info(datas
#name = [data[i][0] for i in range(len(data))]
#name = list(set(name))
# logger.info(name)
ids = [int(data[i][0]) for i in range(len(data))]
ids = sorted(list(set(ids)))
#logger.info(id)
#code = [data[i][3] for i in range(len(data))]

#exit(0)
# logger.info(year)

current_id =25

df_one_year=[]

user_behavior = pd.DataFrame(columns=['id', 'behavior_value1'])

tmp_id_count = 0
for id in ids:
#for id in [1416]:
    current_id =id
    tmp_id_count += 1
    time_end = time.time()
    if tmp_id_count % 100==0:
        logger.info('current running id: %d,%d/%d, time past:%d s', id, tmp_id_count, len(ids), time_end - time_start)
    if (id==current_id):
        df_one_id = df.loc[df['id'] == id]
        #print(df_one_id)
        df_one_id = df_one_id.copy()
        df_one_id.drop_duplicates('page',keep = 'first', inplace = True)
#        logger.info("=================")
#       print(df_one_id)
#        exit(0)
        df_one = df_one_id.values.tolist()
        staytime = [df_one[i][2] for i in range(len(df_one)) ]
        value= compute_area.getarea(staytime)
        user_behavior.loc[tmp_id_count-1] = [id,value]

        #for c in code:
        #    d = company_code_part.loc[(company_code_part['行业代码'] == 'J')]
        #    for c

logger.info("writing results to file..")
user_behavior.to_csv(f_weights,index=False)
time_end = time.time()
logger.info('The end,cost time:%d s', time_end - time_start)
#plt.hist(f_weights, bins=12, normed=True, color="#FF0000", alpha=.9)
#plt.show()
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