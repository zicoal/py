from numpy import *
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random
import array

'''
a=[2,1]
b=[2,2]
c = np.array([1,2,3,10])
#print(c.shape[0])
#print (np.dot(a,b))

G = nx.DiGraph()
G.add_node(0)
G.add_node(1)
G.add_node(2)
G.add_nodes_from([3,4,5,6])
G.add_cycle([1,2,3,4,0])
G.add_edge(1,3)
G.add_edges_from([(3,5),(3,6),(6,7)])
nx.draw(G)
#plt.savefig("youxiangtu.png")
nx.draw(G)
#plt.show()
#print(nx)

#for node in G.nodes:
#   print(node)
for u,v in G.edges:
    print(str(u) +"->"+str(v))
print(list(G.predecessors(3)))

#print(G.edges)
#print(G.nodes)
#print(G.adj)
#print(G.degree)
#print(ones(100))
x=9
y=30
z=x*1.0/y
Phi=p_tmp=ones(10)*z
#print(Phi)
Phi[1]=0
#print(Phi[1])
#print(Phi)
#print(G.in_degree[1])

s=[1,2,3,4]
ss= "".join(str(list(s)))
#print(ss)
f=random.random()
print(f)
#for node, nbs in G.adjacency():
#    for neighbor,eat in nbs.items():
#        print(node ,"->" ,neighbor)

d = np.array([[1089, 1093]])
e = np.array([[1000, 4443]])
answer = np.exp(-3 * 1089)
answer1 = np.exp(-3 * 100)
print(answer1)
print(answer)
res = answer.sum()/answer1.sum()
'''

def bb():
    pp = range(3)
    print(1)
    for i in pp:
        print(i*i)

myTree = ['a', ['b', ['d',[],[]], ['e',[],[]] ], ['c', ['f',[],[]], []] ]
print(myTree)
print('left subtree = ', myTree[1])
print('root = ', myTree[0])
print('right subtree = ', bb)

print('--------------')
def recurPrintPath(dic):
    for key in dic.keys():
        print(key)
        #判断下一级是否还是字典，如果是字典继续递归
        if type(dic[key]) == type({}):
            recurPrintPath(dic[key])
        else:
            print(dic[key])
            print ('--------------')

def add(t, path):
  for node in path:
    t = t[node]

test_dict = {'a': {'b': {'c': 1}}, 'd': 2}
recurPrintPath(test_dict)
cols=5
for i in range(0, cols):
    print(i)
