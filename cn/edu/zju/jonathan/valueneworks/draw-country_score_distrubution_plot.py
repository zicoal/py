import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

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
import scipy.stats as stats
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



def getscore (x):
    b = 6
    c = 10
    return x**2 - b*x +c

#questions = ['q1', 'q2', 'q3', 'q4',
#             'q5', 'q6', 'q7', 'q8',
#             'q9', 'q10', 'q11', 'q12',
#             'q13', 'q14', 'q15', 'q16']

questions = ['q1', 'q2', 'q4', 'q5',
              'q6', 'q7', 'q8','q9',
             'q10', 'q11', 'q12', 'q15']
new_questions = [f"q{i+1}" for i in range(len(questions))]
show_countries = ['Germany', "France",'Sweden','Croatia',"Zambia","South Africa","Iraq","Hong Kong","India","Japan", "United States","United Kingdom",]

question_meaning={}
#mpl.rcParams['']
rgbcolor= [(255/255,159/255,127/255),(50/255,196/255,233/255),(252/255,114/255,147/255)]
f1 = 'D:\\pydata\\data\\jonathan\\MCS_recoded.csv'
f_question_meaning = 'D:\\pydata\\data\\jonathan\\Questionnaire.xlsx'

f_dir =f'D:\\pydata\\data\\jonathan\\results\\rca_based\\q{len(questions)}\\figs\\score_distribution\\'
f_figs_dir = f_dir + 'fig_score_distribution_%s.png'


str_linear="[f(x)=x]"
str_nonlinear="[$f(x) = (x-3)^2+11$]"


time_start = time.time()

countries = {}
df= pd.read_csv(f1)
df_question= pd.read_excel(f_question_meaning)

for q in new_questions:
    tmp = df_question[q].values.tolist()
    question_meaning[q] = tmp[0]

#print(question_meaning)
time_end = time.time()

data = df.values.tolist()
countries = [data[i][1] for i in range(len(data))]
countries = sorted(list(set(countries)))

logger.info("Country Loaded! #countries:%d, time:%d s'", len(countries), time_end - time_start)

#show_countries = ['Germany', "South Africa",'Hong Kong','Australia',"United States","United Kingdom"]


#colors = ["orange","skyblue","green","gray","deeppink","violet"]
colors = [ 'y','gray', 'violet', '#A0CBE2', '#3CB371', 'b', 'orange', 'DeepPink', 'c', '#838B8B', 'purple',
          'olive', '#A0CBE2', '#4EEE94'] * 500

rows = 3
cols = round(len(questions) / rows)
#print(cols)
bar_width=0.8
bins = [i / 10 for i in range(5, 56, 10)]
x_ticks =np.arange(1,6,1)
for country in show_countries:

     f_fig = f_figs_dir % country

     df_one_country = df.loc[df['country'] == country]

     k = 0

     fig = plt.figure(figsize=(24, 18));
     plt.clf()
     fig, axs = plt.subplots(nrows=rows, ncols=cols, num=1)

     #ax = ax.ravel()
#     bins=np.arange(0.5, 5.5, 1)
     sample_num = len(df_one_country)
 #    print(sample_num)
     for q in questions:

         df_one_question =pd.DataFrame()
         df_one_question[q] = df_one_country[q]

         data_one_question = df_one_question.values.tolist()
         df_one_question['q'] = pd.cut(df_one_question[q],bins)

         df_one_question_non_linear =pd.DataFrame()
         new_score = []
         score = []
         for i in range(len(data_one_question)):
#                score.append(data_one_question[i])
                new_score.append(getscore(data_one_question[i][0]))
         df_one_question_non_linear[q] = new_score
         df_one_question_non_linear['q'] = pd.cut(df_one_question_non_linear[q],bins)

         frequency_linear = df_one_question['q'].value_counts().sort_index()
         frequency_nonlinear = df_one_question_non_linear['q'].value_counts().sort_index()
         ix = np.unravel_index(k, axs.shape)
         plt.sca(axs[ix])
         #sns.set(style="whitegrid")
         #ax[ix].xticks(X)
         x = np.arange(0, 5 * 2, 2)
         width = bar_width
         x1 = x - width/2
         x2 = x + width/2
         if k == 0:
             axs[ix].bar(x1, frequency_linear.values / sample_num, width=width, color=colors[1], label="Original")
             axs[ix].bar(x2, frequency_nonlinear.values / sample_num, width=width, color=colors[2], label='Polarization')
             axs[ix].legend(loc="best", frameon=False, fontsize=18)
             # print("%%%%%%%", frequency_linear.index.astype(str))
             # print("$$$$$$$", frequency_linear.values)
         else:
             axs[ix].bar(x1, frequency_linear.values / sample_num, width=width, color=colors[1])
             axs[ix].bar(x2, frequency_nonlinear.values / sample_num, width=width, color=colors[2])

         avg_original = np.mean(df_one_question[q])
         avg_polarization =   np.mean(df_one_question_non_linear[q])

         axs_twin = axs[ix].twinx()
         axs_twin.set_ylim(1,5)
         if (k==1):
             axs_twin.axhline(avg_original, color=colors[1], linewidth=4, linestyle="--",label="Original" )
             axs_twin.axhline(avg_polarization, color=colors[2], linewidth=4, linestyle="--",label="Polarization" )
#             axs_twin.legend(loc="best", frameon=False, fontsize=28)
         else:
             axs_twin.axhline(avg_original, color=colors[1], linewidth=4, linestyle="--" )
             axs_twin.axhline(avg_polarization, color=colors[2], linewidth=4, linestyle="--")

         #  plt.xticks(x, frequency_linear.index.astype(str), fontsize=11)
         plt.xticks(x, x_ticks.astype(str), fontsize=20)
         axs[ix].set_title(f"{new_questions[questions.index(q)]}:{question_meaning[new_questions[questions.index(q)]]}", fontsize=20)
         xylims = plt.axis()
         if k == len(questions) - 2:
             axs[ix].text(xylims[0] - 4,xylims[2] - 1.12, f"{country}", fontsize=30)
         k += 1
     plt.savefig(f_fig,dpi=200, bbox_inches='tight')
     plt.close()
     time_end = time.time()
     logger.info("country:%s，time:%d s", country, time_end - time_start)

