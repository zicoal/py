from matplotlib import pyplot as plt
import collections

def draw_hist(myList,Title,Xlabel,Ylabel,Xmin,Xmax,Ymin,Ymax):
    plt.hist(myList,100)
    plt.xlabel(Xlabel)
    plt.xlim(Xmin,Xmax)
    plt.ylabel(Ylabel)
    plt.ylim(Ymin,Ymax)
    plt.title(Title)
    plt.show()

def draw_hist(myList, binnum, Title, Xlabel, Ylabel, Xmin, Xmax, Ymin, Ymax):
     plt.hist(myList, bins=binnum)
     plt.xlabel(Xlabel)
     plt.xlim(Xmin, Xmax)
     plt.ylabel(Ylabel)
     plt.ylim(Ymin, Ymax)
     plt.title(Title)
     plt.show()

##Tree operation
#create tree
def tree():
    return collections.defaultdict(tree)
#print tree
def dicts(t):
    return {k: dicts(t[k]) for k in t}
#add one node to tree
#example. add(taxonomy,
 #   'Animalia>Chordata>Mammalia>Cetacea>Balaenopteridae>Balaenoptera>blue whale'.split('>'))
def add(t, path):
  for node in path:
    t = t[node]