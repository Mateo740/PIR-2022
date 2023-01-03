#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 09:56:45 2023

@author: legatpauline
"""


# On simule un appel à la fmu
#d_init= 0 m
#v_init = 25


# Création d'une FMU random (à revoir)

# D= [0, 0, 0]
# V = [25]
# C = [0, 0, 0]
# d = 0
# import random
# for i in range (0,len(V)):
#     v0= V[i]
#     speeds= []
#     cons = []
#     while len(speeds)<1:
#         v1=random.uniform(15,35)
#         c1= random.random()
#         if v1 > v0 and c1 > 0:
#             speeds+= [v1]
#             cons+= [c1]
#     while len(speeds)!=2:
#         v2=random.uniform(15,35)
#         c2=0
#         if v2 <v0:
#             speeds+= [v2]
#             cons+= [c2]
#     V+= speeds
#     C+= cons
# d+= 100
# D+=  [d,d]
# #
# # print(V)
# # print(C)
# # print(D)
#



# Test avec valeurs prédéfinies comme si on avait rempli les tableaux avec les données FMU
V2 = [26,25,24,27,25.8,25.2,24.8,24.2,20,32,26.9,27.9,25.4,26.7,25.1,24.9,24.6,24.3,24.1,21,18]
C2 = [0 , 0.2 , 0, 0.1, 0, 0.3, 0, 0.3, 0, 0.1, 0, 0.4 ,0, 0.2 ,0,0.1,0,0.3,0,0.4,0]
D2 = [0,0,0,100,100,100,100,100,100, 200,200, 200, 200,200,200,200,200,200,200,200,200]

#Rajout points départ, arrivée et leur distance(=0m) + conso (-1,1)


# generation du graphe

import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

G = nx.DiGraph()


# Construction des noeuds pour 3 vitesses de départ
m = 3
l= 1
k=1

#Rajout point départ + connexion aux vitesse départ 


G.add_node(V2[0],level = 0)
G.add_node(V2[1],level = 0)
G.add_node(V2[2],level = 0)
i=0

for k in range (3,len(V2)):
    if k == m*2+3:
        l+=1
        m = k
    G.add_node(V2[k], level=l)

# layout des noeuds
pos = nx.multipartite_layout(G, subset_key="level")


# construction des côtés
E = []
m = 3

k=0
for k in range (0, len(V2)//2-1):
    E = E + [(V2[k],V2[m],C2[m]), (V2[k],V2[m+1],C2[m+1])]
    m+=2
    k+=1

# print(E)
# print(V2)

# rajout dernier point connecté à tous les derniers du même level




G.add_weighted_edges_from(E)

nx.draw(G, pos, with_labels=True)

# ajout des poids
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

G = nx.DiGraph()


plt.title("Graphe des vitesses")
plt.show()


p1 = nx.shortest_path(G, source=0, target=9, weight="weight")
consumption = nx.shortest_path_length(G, source=0, target=9, weight="weight")
print("The shortest path from 0 to 9: " , p1)
print("The lowest consumption is", round(consumption,2)) #arrondi au dixième

plt.show()