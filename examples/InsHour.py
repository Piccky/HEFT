from examples.XMLParser import getorders, getvm
import networkx as nx
import matplotlib.pyplot as plt
import math
# Unresolved import:nx
orders = getorders()
G = []
sl = []
el = []
jl = []
sL = {}
eL = {}
jL = {}
# print(len(orders))
vm = getvm()
# print(vm[0])
for i in range(0, len(orders), 1):
    G.append(nx.DiGraph())


for eachP in orders:

    for i in orders[eachP]:
            jl.append(orders[eachP][orders[eachP].index(i)][0])
            sl.append(orders[eachP][orders[eachP].index(i)][1])
            el.append(orders[eachP][orders[eachP].index(i)][2])
    sL.update({eachP: sl})
    eL.update({eachP: el})
    jL.update({eachP: jl})
    sl = []
    el = []
    jl = []


def geteL():
    return eL

def getG():
    return G
"""Build a new DAG for computing InstanceHour"""
"""Set nodes G"""
# //0-45  75-115  123-188  250-285  290-330  335-370

for i in range(0, len(G), 1):
    for j in range(0, len(sL[vm[i]])+1, 1):
        if j == 0:
            G[i].add_node(j, starttime=sL[vm[i]][0], endtime=sL[vm[i]][0])
            continue
        if j == len(sL[vm[i]]):
            G[i].add_node(j, starttime=eL[vm[i]][j - 1], endtime=eL[vm[i]][j - 1])
            continue
        G[i].add_node(j, starttime=eL[vm[i]][j - 1], endtime=sL[vm[i]][j])

"""Set edges aG"""
for i in range(0, len(G), 1):
    for j in range(len(sL[vm[i]]), 0, -1):
        for k in range(0, j, 1):
            G[i].add_edge(k, j, weight=math.ceil((G[i].node[j]["starttime"] - G[i].node[k]["endtime"]) / 60))

"""Compute the Instance Hour"""
path = []
for i in range(0, len(G), 1):
    path.append(nx.dijkstra_path(G[i], 0, len(sL[vm[i]]), weight='weight'))
    print(vm[i], ":", path[i])
temp = []
for i in range(len(G)):
    temp.append(0)

"""print vm start time and end time"""
for i in range(0, len(G), 1):
    for j in range(0, len(path[i]) - 1, 1):
        print('vm[', vm[i], ']start time:', G[i].node[path[i][j]]['endtime'], 'end time:', G[i].node[path[i][j + 1]]['starttime']
              , G[i].get_edge_data(path[i][j], path[i][j + 1]))
        temp[i] += G[i].get_edge_data(path[i][j], path[i][j + 1])['weight']

print('total instance hour:', temp)

"""Draw the DAG"""
# for i in range(0, len(G), 1):
#     nx.draw(G[i], pos=nx.random_layout(G[i]), node_color='b', edge_color='r', with_labels=True, font_size=12,
#             node_size=40)
#     plt.show()
