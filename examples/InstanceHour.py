from examples.XMLParser import getorders
import networkx as nx
import matplotlib.pyplot as plt
# Unresolved import:nx
orders = getorders()
G = nx.DiGraph()
# G.add_node("spam")
# G.add_edge(1, 2)
# print(G.nodes())
"""Put the schedule result into lists"""
ajlist = []
aslist = []
aelist = []

for eachP in orders:
#     # print(eachP, orders[eachP])
    if eachP == 'a':
        # for eachJob in orders[eachP]:
        # list0.append(orders[eachP])
        # print(orders[eachP][1])第二个[1]内表示第i个Event
        for i in orders[eachP]:
            ajlist.append(orders['a'][orders[eachP].index(i)][0])
            aslist.append(orders['a'][orders[eachP].index(i)][1])
            aelist.append(orders['a'][orders[eachP].index(i)][2])
print(ajlist, '\n', aslist, '\n', aelist)
"""Build a new DAG for computing InstanceHour"""
"""Set nodes"""
for i in range(0,len(ajlist)+1,1):
    if i == 0:
        G.add_node(i, starttime=aslist[0], endtime=aslist[0])
        continue
    if i == len(ajlist):
        G.add_node(i, starttime=aelist[i-1], endtime=aelist[i-1])
        continue
    G.add_node(i, starttime=aelist[i-1], endtime=aslist[i])
    # print(G.node[i]["starttime"],G.node[i]["endtime"])
# print(G.nodes)
"""Set edges"""
for i in range(len(ajlist), 0, -1):
    # print('i=:',i)
    for j in range(0, i):
        # print('j=:',j)
        # weight = round((G.node[ajlist[i]]["endtime"] - G.node[ajlist[j]]["starttime"]) / 6)
        # print(weight)
        G.add_edge(j, i, weight=int((G.node[i]["endtime"]-G.node[j]["starttime"])/60)+1)
        # print(j,i,':',G.get_edge_data(j,i))
# print(G.edges)

# print(nx.shortest_path_length(G, source=ajlist[0],weight=nx.get_edge_attributes(G,'weight') ,target=ajlist[len(ajlist)-1]))
# nx.draw(G)
# print(nx.min_cost_flow(G))
# path = nx.all_pairs_dijkstra_path(G)
"""Find the minimum path"""
path = nx.dijkstra_path(G,0,len(ajlist), weight='weight')
print(path)
# weight=nx.get_edge_attributes(G,'weight')
temp = 0
for i in range(0,len(path)-1,1):
    print(G.get_edge_data(path[i],path[i+1]))
    # print (G[path[i]][path[i+1]]['weight'])
    # print(weight[(path[i],path[i+1])])
print (temp)
"""Draw the DAG"""
nx.draw(G,pos = nx.random_layout(G),node_color = 'b',edge_color = 'r',with_labels = True,font_size =12,node_size =40)
plt.show()
#  # temp = 0
# #     Result = 9999
# ajlist=[0,75,123,250,290,335]
# aelist=[45,115,188,285,330,370]
#
# num = len(ajlist)
# def compInstanceHour(list1, list2, i, temp, Result):
#
#     for k in range(i-1, -1, -1):
#
#         temp += round((list1[i-1] - list2[k]) / 60)
#         if k == 0:
#             # temp += round((list1[i] - list2[k])/60)
#             if temp < Result:
#                 Result = temp
#                 continue
#         # i = k
#         # temp = temp + compInstanceHour(list1, list2, i, temp, Result)
#         return compInstanceHour(list1, list2, k, temp, Result)
#     return Result
#
# Result=compInstanceHour(aelist,aslist,num,0,9999)
# print(Result)
# print (round(100/60)
#     if eachP == 'b':
#         list1.append(orders[eachP])
#     if eachP == 'c':
#         list2.append(orders[eachP])
#     if eachP == 'd':
#         list3.append(orders[eachP])
#     if eachP == 'e':
#         list4.append(orders[eachP])
# print(list0,'\n',list1,'\n',list2,'\n',list3)
# print(list[0][1])
# for eachP in orders:
#     print(len(orders[eachP]))
# print (orders['a'])