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
# logger to console
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
# fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(ch)


N=329
#add_prefix = "https://www.bilibili.com/video/BV1DJ411S79k?p=%d&vd_source=d94552e1f7e47ccb7a41478dbfcf74be\n"
add_prefix = "https://www.bilibili.com/video/BV1DJ411S79k?p=%d\n"

name = "英文动画 神话故事系列 English Fairy Tales"
file="D:\\temp\\"+name+"\\"+name+".txt"

f = open(file,"w")
for i in range(1,N+1):

    t = add_prefix % i
    f.write(t)

f.close()