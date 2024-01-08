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
import seaborn as sns

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


f1 = 'D:\\pydata\\data\\jonathan\\MCS_recoded.csv'

f_dir =f'D:\\pydata\\data\\jonathan\\results\\rca_based\\q{len(questions)}\\figs\\score_distribution\\'
f_figs_dir = f_dir + 'fig_score_distribution_%s.png'


str_linear="[f(x)=x]"
str_nonlinear="[$f(x) = (x-3)^2+11$]"


time_start = time.time()

countries = {}
df= pd.read_csv(f1)

time_end = time.time()

data = df.values.tolist()
countries = [data[i][1] for i in range(len(data))]
countries = sorted(list(set(countries)))

logger.info("Country Loaded! #countries:%d, time:%d s'", len(countries), time_end - time_start)

#show_countries = ['Germany', "South Africa",'Hong Kong','Australia',"United States","United Kingdom"]

show_countries = ['Germany', "France",'Sweden','Croatia',"Zambia","South Affrica","Iraq","Hong Kong","India","Japan", "United States","United Kingdom",]

#colors = ["orange","skyblue","green","gray","deeppink","violet"]
colors = [ 'y','gray', 'violet', '#A0CBE2', '#3CB371', 'b', 'orange', 'DeepPink', 'c', '#838B8B', 'purple',
          'olive', '#A0CBE2', '#4EEE94'] * 500

rows = 3
cols = round(len(questions) / rows)
#print(cols)

for country in show_countries:

     f_fig = f_figs_dir % country

     df_one_country = df.loc[df['country'] == country]

     k = 0

     fig = plt.figure(figsize=(24, 18));
     plt.clf()
     fig, ax = plt.subplots(nrows=rows, ncols=cols, num=1)

     #ax = ax.ravel()
     for q in questions:

         df_one_question = df_one_country[q]
         data_one_question = df_one_question.values.tolist()
         df_one_question_non_linear =pd.DataFrame()
         new_score = []
         for i in range(len(data_one_question)):
                new_score.append(getscore(data_one_question[i]))
         df_one_question_non_linear[q] = new_score

         ix = np.unravel_index(k, ax.shape)
         plt.sca(ax[ix])
         #sns.set(style="whitegrid")

         b_legend =False
         if k==0:
             b_legend = True
         sns.kdeplot(data=df_one_country[q],label="Original", legend=b_legend, n_levels=5,fill=True, ax=ax[ix])
         sns.kdeplot(data=df_one_question_non_linear[q],label="Polarization", n_levels=5,legend=b_legend, fill=True, ax=ax[ix])

#         sns.histplot(df_one_question_non_linear[q], bins=2, color="orange", kde_kws={"shade": True}, ax=ax[ix])
#         sns.histplot(df_one_country[q], bins=2, color="blue", kde_kws={"shade": True}, ax=ax[ix])

#         matplotlib.rcParams['legend.handlelength'] = 0  #delete lines from legends
#         ax[k].tick_params(axis="both", labelsize=5)

         if k == 0:
            ax[ix].legend(loc="upper left", frameon=False, fontsize=15)
    #         ax[k].legend(loc="lower left", frameon=False, fontsize=8)
#         ax[ix].set_xlim([1, 5])#
#         ax[ix].set_ylim([0, 1])
         k += 1
#     ax[k-1].text(65, max_y* 0.8, ("RCA=%.1f" % rca_threshold), fontsize=8)
     #plt.axis("off")
#     legend_elements=[]
#     for i in range(len(show_countries)):
#         legend_elements.append(Line2D([0], [0], marker='_',color = colors[i], label = show_countries[i]))
     #plt.legend(handles=legend_elements)
#     plt.legend(handles=legend_elements,bbox_to_anchor=(-0.8, -0.2), loc='upper center', fontsize=6, frameon=False,ncols= len(show_countries))
    # plt.tight_layout()
     #ax[0].title(country.capitalize())
     plt.savefig(f_fig,dpi=200, bbox_inches='tight')
     plt.close()
     logger.info("country:%s，time:%d s", country, time_end - time_start)

     exit(0)

#     exit(0)

