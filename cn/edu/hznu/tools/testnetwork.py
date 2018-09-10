import networkx as nx
import matplotlib.pyplot as plt
#g = nx.random_graphs.barabasi_albert_graph(100,3)



g=nx.DiGraph()
g.clear()

a=['A','B']
b=['A','C']
c=['B','D']
d=['D','E']

#g.add_nodes_from(a)
#g.add_nodes_from(b)
#g.add_nodes_from(c)
#g.add_nodes_from(d)
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')
g.add_edge('A','B')
g.add_edge('A','C')
g.add_edge('B','D')
g.add_edge('D','E')
print()

nodes=[]
nodes.append('F')
nodes.append('A')
nodes.append('B')
nodes.append('C')
nodes.append('D')
nodes.append('E')
nodes.append('E')
print(nodes)
print("----")


a=('A','B')
b=('A','C')
c=('B','D')
d=('D','E')

g.add_edges_from([a,b,c,d])

print(g.nodes)
print(g.edges)

C = nx.centrality.betweenness_centrality(g,normalized=False)
#nx.draw_networkx(g)
nx.draw_networkx(g,pos=nx.spring_layout(g))
plt.show()

print(C)
