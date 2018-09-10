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
b=9.0
c=30.0
D_phi=1.0
D_psi=7.0
phi0=1.0
psi0=b/c

Phi=Phi_tmp=ones(n)*phi0
Psi=Psi_tmp=ones(n)*psi0
g=f=ones(n)*1.0
f_Phi=open('Phi.csv','w')
f_Psi=open('Psi.csv','w')
#diffusion
t=0
T=10
f_Phi.write(",".join(str(x) for x in Phi) + '\n')
f_Psi.write(",".join(str(x) for x in Psi) + '\n')
while t<T:
    for node in H.nodes:
        print(str(Phi[node])+","+str(Psi[node]))
        g[node] = b*Phi[node]-c*Phi[node]*Phi[node]*Psi[node]
        f[node] = 1-Phi[node]-g[node]
        Phi_tmp[node] = -1 * H.out_degree[node]*Phi[node]
        Psi_tmp[node] = -1 * H.out_degree[node]*Psi[node]
    for u,v in H.edges:
        Phi_tmp[v] = Phi_tmp[v] + Phi[u]
        Psi_tmp[v] = Psi_tmp[v] + Psi[u]
    Phi_tmp[node] = f[node] + D_phi * Phi_tmp[node]
    Psi_tmp[node] = g[node] + D_psi * Psi_tmp[node]
    Phi[node] = Phi_tmp[node]
    Psi[node] = Psi_tmp[node]
    f_Phi.write(",".join(str(x) for x in Phi) + '\n')
    f_Psi.write(",".join(str(x) for x in Psi) + '\n')
    t = t+1
f_Phi.close()
f_Psi.close()