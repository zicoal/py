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
#print(myTree)
#print('left subtree = ', myTree[1])
#print('root = ', myTree[0])
#print('right subtree = ', bb)

#print('--------------')
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
#recurPrintPath(test_dict)
cols=5
for i in range(0, cols):
    print(i)


listStr = [('python','b'), ('python','c'),('python','d')]

bb=''
for cc in listStr:
#    bb=bb.join(("%s\t%s\n" % (cc[0],cc[1]))
   bb='%s%s\t%s\n'   % (bb,cc[0],cc[1])
#website = ''.join(listStr)
#print(website)
print("%s",bb)

t_0=1970
t_n=1972

for t in range(t_0, t_n):
    print( t)

print("%s" % 1)

s=[(734649.7158912, '991033,733498,734649.6596296,734649.7158912'),
(734649.7158902, '1621813,1667501,734649.7158892,734649.7158902'),
(734649.7158912, '1667501,763400,734649.7158902,734649.7158912'),
 (734649.7158902, '1621813,770028,734649.7158892,734649.7158902'),
(734649.8049411, '770028,965991,734649.7158902,734649.8049411'),
(734649.8564005, '2392157,1041855,734649.8563995,734649.8564005'),
 (734649.730162, '763400,1115091,734649.7158912,734649.7301620'),
(734649.8049421, '965991,1193431,734649.8049411,734649.8049421'),
(734649.7158912, '770028,1218427,734649.7158902,734649.7158912'),
 (734649.746331, '2143701,1236736,734649.7463300,734649.7463310'),
(734649.7158892, '991033,1621813,734649.6596296,734649.7158892'),
(734650.429537, '1621813,1672538,734649.7158892,734650.4295370'),
(734649.74633, '1621813,2143701,734649.7158892,734649.7463300'),
(734649.8536458, '1193431,2391884,734649.8049421,734649.8536458'),
(734649.8563995, '1193431,2392157,734649.8049421,734649.8563995')]

s=sorted(s,key=lambda x:x[0])

print(s)
