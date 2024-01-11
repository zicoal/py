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

def get_filepaths(dir):
    filepaths = []
    for filename in os.listdir(dir):
        filepath = os.path.join(dir, filename)
        if os.path.isfile(filepath):
            filepaths.append(filepath)
    return filepaths

rca_threshold=1.8
#equations = "score1-5"
equations = "eq-nonlinear"


questions_original = ['q1', 'q2', 'q3', 'q4',
             'q5', 'q6', 'q7', 'q8',
             'q9', 'q10', 'q11', 'q12',
             'q13', 'q14', 'q15', 'q16']

questions = ['q1', 'q2', 'q4', 'q5',
              'q6', 'q7', 'q8','q9',
             'q10', 'q11', 'q12', 'q15']


f1 = 'D:\\pydata\\data\\jonathan\\MCS_recoded.csv'
f_code= 'D:\\pydata\\data\\jonathan\\code.xlsx'

f_prefix ="country_network_"
f_dir ='D:\\pydata\\data\\jonathan\\results\\rca_based\\q%d\\' % len(questions)
f_figs_dir ='D:\\pydata\\data\\jonathan\\results\\rca_based\\q%d\\figs\\metrics\\fig_%s.png'




rca_thresholds = [1,  1.2,1.4,
                  1.5, 1.6,1.7,
                  1.8, 1.9, 2]

questions_original = ['q1', 'q2', 'q3', 'q4',
             'q5', 'q6', 'q7', 'q8',
             'q9', 'q10', 'q11', 'q12',
             'q13', 'q14', 'q15', 'q16']

questions = ['q1', 'q2', 'q4', 'q5',
              'q6', 'q7', 'q8','q9',
             'q10', 'q11', 'q12', 'q15']
str_linear="[f(x)=x]"
str_nonlinear="[$f(x) = (x-3)^2+1$]"
#rca_thresholds = [1, 1.1, 1.2, 1.3, 1.4,1.5]


file_list = os.listdir(f_dir)
time_start = time.time()

countries = {}
df= pd.read_csv(f1)

time_end = time.time()

data = df.values.tolist()
countries = [data[i][1] for i in range(len(data))]
countries = sorted(list(set(countries)))

logger.info("Country Loaded! #countries:%d, time:%d s'", len(countries), time_end - time_start)

#show_countries = ['Germany', "South Africa",'Hong Kong','Australia',"United States","United Kingdom"]

#show_countries = ['Germany', "France",'Sweden','Croatia',"Hong Kong","Iraq","Zambia","United States","United Kingdom"]
show_countries = ['Germany', "France",'Sweden','Croatia',"Zambia","South Africa","Iraq","Hong Kong","India","Japan", "United States","United Kingdom",]

#colors = ["orange","skyblue","green","gray","deeppink","violet"]
colors = [ 'y','gray', 'violet', '#A0CBE2', '#3CB371', 'b', 'orange', 'DeepPink', 'c', '#838B8B', 'purple',
          'olive', '#A0CBE2', '#4EEE94'] * 500

rows = 3
cols = round(len(rca_thresholds) / rows)
#print(cols)

for f in file_list:

     file = f_dir + f
     if (os.path.isdir(file) or file.find("~")>=0):
         continue
     network_property = f[len(f_prefix):f.index(".")]

     network_property_old = network_property

     if ("eq-linear" in network_property):
         network_property= network_property.replace("eq-linear",str_linear)
     else:
         network_property = network_property.replace("eq-nonlinear",str_nonlinear)
     f_fig = f_figs_dir % (len(questions),network_property_old)

     logger.info("File:%s，time:%d s", network_property, time_end - time_start)

     df = pd.read_excel(file)
     k = 0

     plt.figure(figsize=(10, 8))
     fig, ax = plt.subplots(rows, cols)
     ax = ax.ravel()
     ax[1].set_title(network_property.capitalize())
     max_y=0
     min_y =1
     for rca_threshold in rca_thresholds:

         columns_name = ['country','rca=%.1f' % rca_threshold]
         df_one_rca = df[columns_name]
         data_one_rca = df_one_rca.values.tolist()
         country_rca={}
         for i in range(len(data_one_rca)):
             #if (data_one_rca[i][1]) >=0:
                 country_rca[data_one_rca[i][0]] = data_one_rca[i][1]

         country_rca = sorted(country_rca.items(), key=lambda x: x[1],reverse=True)

         x =[]
         y =[]
         show_country_index={}
         j =0
         for country in country_rca:
             j+=1
             y.append(country[1])
             x.append(j)
             if country[0] in show_countries:
                 show_country_index[country[0]] = j
             if(k==len(rca_thresholds)-1 and max_y<country[1]):
                max_y =   country[1]
             if (k == len(rca_thresholds) - 1 and min_y > country[1]):
                min_y = country[1]
         matplotlib.rcParams['legend.handlelength'] = 0  #delete lines from legends
#         ax[k].plot(x,y,label=("RCA=%.1f" % rca_threshold))
         ax[k].plot(x,y,label=("RCA=%.1f" % rca_threshold))
         ax[k].tick_params(axis="both", labelsize=5)
         ax[k].legend(loc="best", frameon=False, fontsize=8)
#         ax[k].legend(loc="lower left", frameon=False, fontsize=8)
         ax[k].set_xlim([0, 112])
#         ax[k].lines[0].set_color(13)
         j=0
         for i in range(len(show_countries)):
             ax[k].axvline(show_country_index[show_countries[i]],color=colors[i],linewidth=1,linestyle="--")

         k += 1
     if (min_y< 0):
         max_y = 0
     ax[k-1].text(65, max_y* 0.8, ("RCA=%.1f" % rca_threshold), fontsize=8)
     #plt.axis("off")
     legend_elements=[]
     for i in range(len(show_countries)):
         legend_elements.append(Line2D([0], [0], marker='_',color = colors[i], label = show_countries[i]))
     #plt.legend(handles=legend_elements)
     plt.legend(handles=legend_elements,bbox_to_anchor=(-0.8, -0.2), loc='upper center', fontsize=6, frameon=False,ncols= len(show_countries)/2)
    # plt.tight_layout()
     plt.savefig(f_fig,dpi=800, bbox_inches='tight')
     plt.close()
     #exit(0)

#     exit(0)

