#!/usr/bin/python
# coding:utf-8

import os
import logging
import time
from matplotlib import pyplot as plt
import numpy as np
from cn.edu.hznu.tools import plotfig as pf







category = [x for x in range(100)]  # 类别：0~99
values = list(np.random.rand(100, 10) * 10)  # 类别值：100×10  每一类都有10个数

pf.shaded_Error_Bar(category, values, 1)
