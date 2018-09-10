import logging
import numpy as np
from cn.edu.hznu.tools import entropy
from collections import defaultdict



#unnormalized
'''
A -> B
A -> C
B -> C
B -> D
C -> D
D -> C
E -> F
F -> C





C->D




will be created as
graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
'''

def add_one_edge(g,key,v):
    g.setdefault(key,[]).append(v)
    return g

#depth-first iteration
def get_motif_distance_count_list(g,root,dist_count_list=defaultdict(int),level=0,vistited=defaultdict(str)):
    #    print(vistited.get(root))
    if vistited.get(root) is None:
        vistited[root] = 1
    if g.get(root) is None:
        return None
    for node in g[root]:
       # print("%s->%s" % (root,node))
        newroot= node
        if vistited.get(node) is None:
            vistited[node] = 1
            dist_count_list[level + 1]+=1
            get_motif_distance_count_list(g, newroot, dist_count_list, level + 1, vistited)
    return None


def get_motif_distance_list(g,root,dist_list=(int),level=0,vistited=defaultdict(str)):
    #    print(vistited.get(root))
    if vistited.get(root) is None:
        vistited[root] = 1
    if g.get(root) is None:
        return None
    for node in g[root]:
#        print("%s->%s" % (root,node))
        newroot= node
        if vistited.get(node) is None:
            vistited[node] = 1
            dist_list.append(level + 1)
            get_motif_distance_list(g, newroot, dist_list, level + 1, vistited)
    return None

def get_motif_betweeness_list(g,root,dist_betweeness_list=defaultdict(str),level=0,vistited=defaultdict(str)):
    #    print(vistited.get(root))
    if vistited.get(root) is None:
        vistited[root] = 1
        dist_betweeness_list.setdefault(root, 1)
    if g.get(root) is None:
        return None
    for node in g[root]:
#        print("%s->%s" % (root,node))
#        newroot= node
        if vistited.get(node) is None:
            vistited[node] = 1
            if(dist_betweeness_list.get(node) is None):
                dist_betweeness_list.setdefault(node,1)
            else:
                l=dist_betweeness_list.get(node)+1
                dist_betweeness_list.setdefault(node, l)
            get_motif_betweeness_list(g, node, dist_betweeness_list, level + 1, vistited)
    return None

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None



def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
'''
gi={}
add_one_edge(gi,'A','B')
add_one_edge(gi,'A','C')
add_one_edge(gi,'B','C')
add_one_edge(gi,'B','D')
add_one_edge(gi,'C','D')
add_one_edge(gi,'D','C')
add_one_edge(gi,'E','F')
add_one_edge(gi,'F','C')
print(gi)
'''


gi={}
add_one_edge(gi,'A','B')
add_one_edge(gi,'A','C')
add_one_edge(gi,'B','D')
add_one_edge(gi,'D','E')
print(gi)

#dist_count_list=defaultdict(int)
#visit_flag=defaultdict(int)
#get_motif_distance_count_list(gi,'A',dist_count_list,0,visit_flag)
#get_motif_distance_list(gi,'A',dist_count_list,0,visit_flag)
#for i in dist_count_list.items():
#    print(i[0],i[1])

betweeness_list=defaultdict(str)
visit_flag=defaultdict(int)
get_motif_betweeness_list(gi,'A',betweeness_list,0,visit_flag)


for i in betweeness_list.items():
    print(i[0],i[1])

#dist_list=[]
#get_motif_distance_list(gi,'A',dist_list,0,visit_flag)
#for i in dist_list:
#    print( i )
