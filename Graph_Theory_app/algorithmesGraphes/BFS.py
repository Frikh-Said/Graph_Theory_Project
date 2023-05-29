import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import networkx as nx

def BFS(matrix,source):
    mat = np.array(matrix)
    plt.clf()
    G = nx.from_numpy_array(mat, create_using=nx.DiGraph)
    nodesNumber=mat.shape[0]
    mapping = {}
    for i in range(int(nodesNumber)):
        mapping[i] = chr(65 + i)
    nx.relabel_nodes(G, mapping, copy=False)
    # affichage d'arbre BFS si le graphe est direct
    tree = nx.bfs_tree(G, source=source)
    print(tree.edges())
    # create table of nodes BFS
    tab = []
    flag = 0
    for edg in tree.edges():
        if (flag == 0):
            tab.append(edg[0])
        flag = 1
        tab.append(edg[1])
    nx.relabel_nodes(tree, mapping, copy=False)
    nx.draw(tree, with_labels=True)
    return plt.show()

# mat=[[0,1,0],
#      [0,0,1],
#      [1,0,0]]
# source="A"

# BFS(mat,source)