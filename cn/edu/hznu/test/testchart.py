# !/usr/bin/python
# coding:utf-8


from __future__ import unicode_literals

import json
import os
import logging
import time
from pyecharts import Line
from pyecharts import Bar
from pyecharts import Graph
from pyecharts import Pie
from pyecharts import Style
import random

from pyecharts.conf import PyEchartsConfig
from pyecharts.engine import EchartsEnvironment
from pyecharts.utils import write_utf8_html_file
#import pandas as pd



time_start=time.time()

logger = logging.getLogger()
logger.setLevel(logging.INFO)


bar =Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
#bar.show_config()
#bar.render()

attr =["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 =[5, 20, 36, 10, 10, 100]
v2 =[55, 60, 16, 20, 15, 00]
line =Line("折线图示例")
line.add("商家A", attr, v1, mark_point=["average"])
line.add("商家B", attr, v2, is_smooth=True, mark_line=["max", "average"])
#line.show_config()
#line.render()


nodes =[{"name": "结点1", "symbolSize": 10}, {"name": "结点2", "symbolSize": 20}, {"name": "结点3", "symbolSize": 30}, {"name": "结点4", "symbolSize": 40}, {"name": "结点5", "symbolSize": 50}, {"name": "结点6", "symbolSize": 40}, {"name": "结点7", "symbolSize": 30}, {"name": "结点8", "symbolSize": 20}]
links =[]
for i in nodes:
    for j in nodes:
        links.append({"source": i.get('name'), "target": j.get('name')})
graph =Graph("关系图-环形布局示例")
graph.add("", nodes, links, is_label_show=True, repulsion=800, layout='force', label_text_color=None)
graph.show_config()
graph.render()


nodes = [{"name": "结点1", "symbolSize": 100},
         {"name": "结点2", "symbolSize": 20},
         {"name": "结点3", "symbolSize": 30},
         {"name": "结点4", "symbolSize": 40},
         {"name": "结点5", "symbolSize": 50},
         {"name": "结点6", "symbolSize": 40},
         {"name": "结点7", "symbolSize": 30},
         {"name": "结点8", "symbolSize": 0.1}]
links = []
for i in nodes:
    for j in nodes:
        links.append({"source": i.get('name'), "target": j.get('name'), "value": 100*random.random() })
graph = Graph("关系图-力引导布局示例")
graph.add(
    "",
    nodes,
    links,
    is_label_show=True,
    graph_repulsion=8000,
    graph_layout="circular",
    label_text_color=None,
)
graph.render()


from pyecharts import Bar, Line, Grid

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图示例", height=720)
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True)
line = Line("折线图示例", title_top="50%")
attr = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
line.add(
    "最高气温",
    attr,
    [11, 11, 15, 13, 12, 13, 10],
    mark_point=["max", "min"],
    mark_line=["average"],
)
line.add(
    "最低气温",
    attr,
    [1, -2, 2, 5, 3, 2, 0],
    mark_point=["max", "min"],
    mark_line=["average"],
    legend_top="50%",
)

grid = Grid()
grid.add(bar, grid_bottom="60%")
grid.add(line, grid_top="60%")
grid.render()


style = Style(
    title_color="#fff",
    title_pos="center",
    width=1100,
    height=600,
    background_color='#404a59'
)
pie = Pie('各类电影中"好片"所占的比例', "数据来着豆瓣", title_pos='center')
# 使用 Style.add() 可配置增加图例的风格配置字典
pie_style = style.add(
    radius=[18, 24],
    label_pos="center",
    is_label_show=True,
    label_text_color=None
)

pie.add("", ["剧情", ""], [25, 75], center=[10, 30], **pie_style)
pie.add("", ["奇幻", ""], [24, 76], center=[30, 30], **pie_style)
pie.add("", ["爱情", ""], [14, 86], center=[50, 30], **pie_style)
pie.add("", ["惊悚", ""], [11, 89], center=[70, 30], **pie_style)
pie.render()


'''
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图数据堆叠示例")
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True)
config = PyEchartsConfig(echarts_template_dir='my_tpl',
                         jshost='https://cdn.bootcss.com/echarts/3.6.2')
env = EchartsEnvironment(pyecharts_config=config)
#tpl = env.get_template('/home/zico/py/cn/edu/hznu/test/tpl_demo.html')
tpl = env.get_template('tpl_demo.html')
html = tpl.render(bar=bar)
write_utf8_html_file('my_tpl_demo2.html', html)
'''