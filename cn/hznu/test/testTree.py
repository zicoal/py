from numpy import *
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random
import array
import re
# example canbe found at https://gist.github.com/hrldcpr/2012250
#https://www.jb51.net/article/84916.htm
#https://docs.python.org/3/library/collections.html#collections.defaultdict
#https://blog.csdn.net/xiaodongxiexie/article/details/71249837
from collections import defaultdict
def tree(): return defaultdict(tree)
def dicts(t):
    return {k: dicts(t[k]) for k in t}
def add(t, path):
  for node in path:
    t = t[node]

def getPath(t, path):
  for node in path:
    t = t[node]



taxonomy = tree()
taxonomy['Animalia']['Chordata']['Mammalia']['Carnivora']['Felidae']['Felis']['cat']
taxonomy['Animalia']['Chordata']['Mammalia']['Carnivora']['Felidae']['Panthera']['lion']
taxonomy['Animalia']['Chordata']['Mammalia']['Carnivora']['Canidae']['Canis']['dog']
taxonomy['Animalia']['Chordata']['Mammalia']['Carnivora']['Canidae']['Canis']['coyote']
taxonomy['Plantae']['Solanales']['Solanaceae']['Solanum']['tomato']
taxonomy['Plantae']['Solanales']['Solanaceae']['Solanum']['potato']
taxonomy['Plantae']['Solanales']['Convolvulaceae']['Ipomoea']['sweet potato']
#recurPrintPath(taxonomy,'')
a={'Animalia': {'Chordata': {'Mammalia': {'Carnivora': {'Canidae': {'Canis': {'coyote': {}, 'dog': {}}}, 'Felidae':
    {'Panthera': {'lion': {}}, 'Felis': {'cat': {}}}}}}}, 'Plantae': {'Solanales': {'Solanaceae': {'Solanum': {'tomato': {}, 'potato': {}}}, 'Convolvulaceae': {'Ipomoea': {'sweet potato': {}}}}}}
#print(dicts(taxonomy))
add(taxonomy,
    'Animalia>Chordata>Mammalia>Cetacea>Balaenopteridae>Balaenoptera>blue whale'.split('>'))
#m = re.match(taxonomy,'Plantae')
#print(dicts(getPath(taxonomy,'Solanales')))
#print(dicts(getPath(taxonomy,'Solanales')))
'''
s = 'mississippi'
d = defaultdict(int)
for k in s:
    print(d[k])
sorted(d.items())
'''

'''
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
    print(d[k])
'''


