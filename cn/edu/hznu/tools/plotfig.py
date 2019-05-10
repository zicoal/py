#!/usr/bin/python
# coding:utf-8


from matplotlib import pyplot as plt
import numpy as np

# 阴影误差图
# 参考https://blogs.mathworks.com/pick/2012/08/17/shaded-error-bars/
# 中间的实线是该类别的均值，上、下界是加上、减去n倍该类别的标准差。

def shaded_Error_Bar(category, values, n):
    values_down = [x.mean() - n * (np.array(x).std()) for x in values]  # 下界
    values_up = [x.mean() + n * (np.array(x).std()) for x in values]  # 上界
    values_mean = [x.mean() for x in values]  # 均值

    plt.plot(category, values_mean, 'red')
    plt.plot(category, values_down, 'pink')
    plt.plot(category, values_up, 'pink')

    plt.fill_between(category, values_down, values_up, color='red', alpha=0.25)

    plt.show()