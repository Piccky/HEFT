from examples.XMLParser import getorders, getdict, commcost, getvm
import networkx as nx
# from examples.my_scheduler import getorders, getdag, commcost
from heft.util import reverse_dict
import matplotlib.pyplot as plt
import math
from examples.listoperation import getVmList, recruise
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
result = {}
for i in range(0, len(G), 1):
    for j in range(0, len(jL[vm[i]]), 1):
        result.update({jL[vm[i]][j]: {'vm': vm[i], 'pos': j, 'starttime': sL[vm[i]][j], 'endtime': eL[vm[i]][j]}})
print(result)

"""Add waitcost into the schedule result"""

dag = getdict()
reverse_dag = reverse_dict(dag)
for i in range(0, len(G), 1):
    for j in range(1, len(jL[vm[i]]), 1):
        if jL[vm[i]][j] in dag:
            temp = 999999
            for k in range(0, len(dag[jL[vm[i]][j]]), 1):
                if result[dag[jL[vm[i]][j]][k]]['endtime'] < temp:
                    temp = result[dag[jL[vm[i]][j]][k]]['endtime']
            sL[vm[i]][j] = temp

"""Add communication cost to the schedule"""
for i in range(0, len(G), 1):
    for j in range(0, len(jL[vm[i]]) - 1, 1):
        if jL[vm[i]][j] in reverse_dag:
            temp = 0
            for k in range(0, len(reverse_dag[jL[vm[i]][j]]), 1):
                if temp < commcost(jL[vm[i]][j], reverse_dag[jL[vm[i]][j]][k]
                        , result[jL[vm[i]][j]]['vm'], result[reverse_dag[jL[vm[i]][j]][k]]['vm']):
                    temp = commcost(jL[vm[i]][j], reverse_dag[jL[vm[i]][j]][k]
                                    , result[jL[vm[i]][j]]['vm'], result[reverse_dag[jL[vm[i]][j]][k]]['vm'])

            eL[vm[i]][j] += temp

print('-------------------------------------')
print('Print the original list:')
for i in range(0, len(G), 1):
    print('vm[', vm[i], ']:', '\n', jL[vm[i]], '\n', sL[vm[i]], '\n', eL[vm[i]])

for i in range(0, len(G), 1):
    sL[vm[i]], eL[vm[i]] = recruise(getVmList, sL[vm[i]], eL[vm[i]], jL[vm[i]])

print('------------------------------------')
print('Refresh the list:')
for i in range(0, len(G), 1):
    print('vm[', vm[i], ']:', '\n', jL[vm[i]], '\n', sL[vm[i]], '\n', eL[vm[i]])

"""Build a new DAG for computing InstanceHour"""
"""Set nodes aG"""
# //0-45  75-115  123-188  250-285  290-330  335-370

print('Print each node[starttime,endtime]:')

for i in range(0, len(G), 1):
    for j in range(0, len(sL[vm[i]]) + 1, 1):
        if j == 0:
            G[i].add_node(j, starttime=sL[vm[i]][0], endtime=sL[vm[i]][0])
            print(G[i].node[j]["starttime"], G[i].node[j]["endtime"])
            continue
        if j == len(sL[vm[i]]):
            G[i].add_node(j, starttime=eL[vm[i]][j - 1], endtime=eL[vm[i]][j - 1])
            print(G[i].node[j]["starttime"], G[i].node[j]["endtime"])
            continue
        G[i].add_node(j, starttime=eL[vm[i]][j - 1], endtime=sL[vm[i]][j])
        print(G[i].node[j]["starttime"], G[i].node[j]["endtime"])
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
        print('vm[', vm[i], ']start time:', G[i].node[path[i][j]]['endtime'], 'end time:',
              G[i].node[path[i][j + 1]]['starttime']
              , G[i].get_edge_data(path[i][j], path[i][j + 1]))
        temp[i] += G[i].get_edge_data(path[i][j], path[i][j + 1])['weight']

total = 0
for i in range(0, len(temp), 1):
    total += temp[i]
print('Total instance hour(With Commcost):', temp, "\n", "total:", total)


