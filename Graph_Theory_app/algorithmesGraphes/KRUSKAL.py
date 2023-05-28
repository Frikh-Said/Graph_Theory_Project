import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def KRUSKAL(matrix, nodesNumber, graphType):
    mat = np.array(matrix)

    if graphType == "up":
        G = nx.from_numpy_array(mat, create_using=nx.Graph())
    else:
        G = nx.from_numpy_array(mat, create_using=nx.DiGraph())

    mapping = {}
    for i in range(nodesNumber):
        mapping[i] = chr(65 + i)
    G = nx.relabel_nodes(G, mapping, copy=False)

    # Kruskal tree
    mst = nx.minimum_spanning_tree(G)

    layout = nx.spring_layout(mst)
    nx.draw(mst, layout, with_labels=True)
    labels = nx.get_edge_attributes(mst, 'weight')

    # Get a list of values (contains all weights in the minimum spanning tree)
    list_weight = list(labels.values())
    ACM = sum(list_weight)
    print("ACM=",ACM)

    nx.draw_networkx_edge_labels(mst, pos=layout, edge_labels=labels)
    plt.show()

nodesNumber = 3
graphType = "up"
mat = [[0, 1, 0],
       [0, 0, 1],
       [1, 0, 0]]

KRUSKAL(mat, nodesNumber, graphType)
