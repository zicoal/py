from graph_tool.all import *

g = Graph()  #实例化Graph类创建一个空图
ug = Graph(directed=False) #有向图
ug = Graph()
ug.set_directed(False)
#assert ug.is_directed() == False

g1 = Graph()
g2 = Graph(g1)

#add_vertex()方法添加两个顶点
v1 = g.add_vertex()
v2 = g.add_vertex()

#add_edge()添加了从v1到v2的有向边
e = g.add_edge(v1, v2)

#graph_draw()函数创建network图
graph_draw(g, vertex_text=g.vertex_index, output="two-nodes.pdf")