# Test avec valeurs prédéfinies comme si on avait rempli les tableaux avec les données FMU
V = [26,25,24,27,25.8,25.2,24.8,24.2,20,32,26.9,27.9,25.4,26.7,25.1,24.9,24.6,24.3,24.1,21,18]
C = [0 , 0.2 , 0, 0.1, 0, 0.3, 0, 0.3, 0, 0.1, 0, 0.4 ,0, 0.2 ,0,0.1,0,0.3,0,0.4,0]
D = [0,0,0,100,100,100,100,100,100, 200,200, 200, 200,200,200,200,200,200,200,200,200]
# generation du graphe

import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

G = nx.DiGraph()


# Construction des noeuds pour 3 vitesses de départ
m = 3
l= 1
k=1

# 1st node added manually (level -1) and named "B"
G.add_node('B',level = -1)

# 3 starting speeds added given the 3 first values of V2 vector (level 0)
G.add_node(V[0],level = 0)
G.add_node(V[1],level = 0)
G.add_node(V[2],level = 0)

i=0

for k in range (3,len(V2)):
    if k == m*2+3:
        l+=1
        m = k
    G.add_node(V[k], level=l)

# Last node added manually (level L+1 = last level) and named "E"
G.add_node('E',level = l+1)



# layout des noeuds
pos = nx.multipartite_layout(G, subset_key="level")


# construction des côtés
E = []
m = 3

k=0
for k in range (0, len(V2)//2-1):
    E = E + [(V[k],V[m],C[m]), (V[k],V[m+1],C[m+1])]
    m+=2
    k+=1


# print(E)
# print(V2)
G.add_weighted_edges_from(E)

G.add_weighted_edges_from([('B',26,1),('B',25,1),('B',24,1)])
G.add_weighted_edges_from([(32,'E',-1),(26.9,'E',-1),(27.9,'E',-1),(25.4,'E',-1),(26.7,'E',-1),(25.1,'E',-1),(24.9,'E',-1),(24.6,'E',-1),(24.3,'E',-1),(24.1,'E',-1),(21,'E',-1),(18,'E',-1)])
nx.draw(G, pos, with_labels=True,node_size=1000)

# ajout des poids
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

p1 = nx.shortest_path(G, source='B', target='E', weight="weight")
consumption = nx.shortest_path_length(G, source='B', target='E', weight="weight")
print("The shortest path is: " , p1)
print("The lowest consumption is", round(consumption,2)) #arrondi au dixième

plt.show()




