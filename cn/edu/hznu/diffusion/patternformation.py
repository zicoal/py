import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import array
import random
from numpy import *

#生成WS网络
n=100 #节点数目
p=0.1 #WS重连概率
G = nx.random_graphs.watts_strogatz_graph(n, 5, p)
print(G.number_of_edges())
H=G.to_directed()
H.add_edges_from(G.edges)
print(H.number_of_edges())
for e in list(H.edges):
    if random.random()>0.6:
        H.remove_edge(*e)
print(H.number_of_edges())
#nx.draw(H)
#plt.show()
#initial parameters
b=9
c=30
D_phi=1
D_psi=7
phi0=1
psi0=b*1.0/c

Phi=Phi_tmp=ones(n)*phi0
Psi=Psi_tmp=ones(n)*psi0

f_Phi=open('Phi.csv','w')
f_Psi=open('Psi.csv','w')
#diffusion
t=0
T=4
f_Phi.write(",".join(str(x) for x in Phi) + '\n')
f_Psi.write(",".join(str(x) for x in Psi) + '\n')
while t<T:
    for node, nbs in H.adjacency():
        g = b*Phi[node]-c*Phi[node]*Phi[node]**Psi[node]
        f = 1-Phi[node]-g
        print(H.out_degree[node])
        Phi_tmp[node] = Psi_tmp[node] =  -1* H.out_degree[node]
        #Psi_tmp[node] =  - G.out_degree[node]
        for neighbor in list(H.predecessors(node)):
            #print(node ,"->" ,neighbor)
            Phi_tmp[node] = Phi_tmp[node] + 1
            Psi_tmp[node] = Psi_tmp[node] + 1
        Phi_tmp[node] = f + D_phi * Phi_tmp[node]
        Psi_tmp[node] = g + D_psi * Psi_tmp[node]
        Phi[node] = Phi_tmp[node]
        Psi[node] = Psi_tmp[node]
    f_Phi.write(",".join(str(x) for x in Phi) + '\n')
    f_Psi.write(",".join(str(x) for x in Psi) + '\n')
    t = t+1
f_Phi.close()
f_Psi.close()