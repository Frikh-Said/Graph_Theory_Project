import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def Dfs(matrix,source):

    mat = np.array(matrix)
    G = nx.from_numpy_array(mat, create_using=nx.DiGraph)
    nodesNumber=mat.shape[0]
    print(nodesNumber)
    mapping = {}
    for i in range(int(nodesNumber)):
        mapping[i] = chr(65 + i)
    nx.relabel_nodes(G, mapping, copy=False)
    # affichage d'arbre DFS si le graphe est direct
    tree = nx.dfs_tree(G, source=source)
    print(tree.edges())
    # create table of nodes DFS
    tab = []
    flag=0
    for edg in tree.edges():
        if(flag == 0) :
            tab.append(edg[0])
        flag = 1
        tab.append(edg[1])
    nx.relabel_nodes(tree, mapping, copy=False)
    nx.draw(tree, with_labels=True)
    return plt.show()

mat=[[0,1,0],
     [0,0,1],
     [1,0,0]]
source="B"

Dfs(mat,source)
