import matplotlib.pyplot as plt
import math

import networkx as nx
import numpy as np
import pandas as pd
from random import *
import time
import logging
from scipy.stats import pearsonr

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

f1 = 'D:\\py\\data\\chenjuanjuan\\k-shell.xlsx'
f_correlation = 'D:\\py\\data\\chenjuanjuan\\correlation.csv'

logger.info("loading data...")
time_start=time.time()
df = pd.read_excel(f1)
df = df.loc[::, ['一层节点数量', '二层节点数量', '三层节点数量', 'Performance']]
#logger.info(df['id'].value_counts())

#ids = [int(data[i][0]) for i in range(len(data))]
#ids = sorted(list(set(ids)))



correlation = pd.DataFrame(columns=['beta', 'correlation'])

data = df.values.tolist()
layer1=[]
layer2=[]
layer3=[]
performance = []

#reorganize data
for i in range(len(data)):
    if (np.isnan(float(data[i][0]))):
        layer1.append(0)
    else:
        layer1.append(int(data[i][0]))

    if (np.isnan(float(data[i][1]))):
        layer2.append(0)
    else:
        layer2.append(int(data[i][1]))

    if (np.isnan(float(data[i][2]))):
        layer3.append(0)
    else:
        layer3.append(int(data[i][2]))

    performance.append(float(data[i][3]))


beta=-10
line = 0

x=[]
y=[]

while (beta < 30):

    score = [1**beta*layer1[i]+2**beta*layer2[i]+3**beta*layer3[i] for i in range(len(layer1))]
    c = pearsonr(score,performance)
    correlation.loc[line] = [beta, c[0]]
    x.append(beta)
    y.append(c[0])
    if abs(beta) <= 0.99:
        step =0.1
    elif abs(beta) <= 10:
        step = 1
    elif abs(beta) <= 30:
        step = 10
    line += 1
    beta += step


plt.semilogx(x,y)
#plt.plot(x,y)
plt.xlabel('$ \\beta $')
plt.ylabel('correlation')
plt.show()

        #for c in code:
        #    d = company_code_part.loc[(company_code_part['行业代码'] == 'J')]
        #    for c

logger.info("writing results to file..")
correlation.to_csv(f_correlation,index=False)
time_end = time.time()
logger.info('The end,cost time:%d s', time_end - time_start)
