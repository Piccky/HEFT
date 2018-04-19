from examples.XMLParser import getorders, getdict, commcost
import networkx as nx
# from examples.my_scheduler import getorders, getdag, commcost
from heft.util import reverse_dict
import matplotlib.pyplot as plt
import math
# Unresolved import:nx
orders = getorders()
aG = nx.DiGraph()
bG = nx.DiGraph()
cG = nx.DiGraph()
dG = nx.DiGraph()
eG = nx.DiGraph()
fG = nx.DiGraph()
gG = nx.DiGraph()

# G.add_node("spam")
# G.add_edge(1, 2)
# print(G.nodes())
"""Put the schedule result into lists"""
ajlist = []
aslist = []
aelist = []
bjlist = []
bslist = []
belist = []
cjlist = []
cslist = []
celist = []
djlist = []
dslist = []
delist = []
ejlist = []
eslist = []
eelist = []
fjlist = []
fslist = []
felist = []
gjlist = []
gslist = []
gelist = []
result = {}

for eachP in orders:
#     # print(eachP, orders[eachP])
#     if eachP == 'a':
#         # for eachJob in orders[eachP]:
#         # list0.append(orders[eachP])
#         # print(orders[eachP][1])第二个[1]内表示第i个Event
#         for i in orders[eachP]:
#             ajlist.append(orders['a'][orders[eachP].index(i)][0])
#             aslist.append(orders['a'][orders[eachP].index(i)][1])
#             aelist.append(orders['a'][orders[eachP].index(i)][2])
    if eachP == 'a':
        for i in orders[eachP]:
            ajlist.append(orders[eachP][orders[eachP].index(i)][0])
            aslist.append(orders[eachP][orders[eachP].index(i)][1])
            aelist.append(orders[eachP][orders[eachP].index(i)][2])
    if eachP == 'b':
        for i in orders[eachP]:
            bjlist.append(orders[eachP][orders[eachP].index(i)][0])
            bslist.append(orders[eachP][orders[eachP].index(i)][1])
            belist.append(orders[eachP][orders[eachP].index(i)][2])
    if eachP == 'c':
        for i in orders[eachP]:
            cjlist.append(orders[eachP][orders[eachP].index(i)][0])
            cslist.append(orders[eachP][orders[eachP].index(i)][1])
            celist.append(orders[eachP][orders[eachP].index(i)][2])
    if eachP == 'd':
        for i in orders[eachP]:
            djlist.append(orders[eachP][orders[eachP].index(i)][0])
            dslist.append(orders[eachP][orders[eachP].index(i)][1])
            delist.append(orders[eachP][orders[eachP].index(i)][2])
    if eachP == 'e':
        for i in orders[eachP]:
            ejlist.append(orders[eachP][orders[eachP].index(i)][0])
            eslist.append(orders[eachP][orders[eachP].index(i)][1])
            eelist.append(orders[eachP][orders[eachP].index(i)][2])
    if eachP == 'f':
        for i in orders[eachP]:
            fjlist.append(orders[eachP][orders[eachP].index(i)][0])
            fslist.append(orders[eachP][orders[eachP].index(i)][1])
            felist.append(orders[eachP][orders[eachP].index(i)][2])
    if eachP == 'g':
        for i in orders[eachP]:
            gjlist.append(orders[eachP][orders[eachP].index(i)][0])
            gslist.append(orders[eachP][orders[eachP].index(i)][1])
            gelist.append(orders[eachP][orders[eachP].index(i)][2])
for i in range(0,len(ajlist),1):
    result.update({ajlist[i]:{'vm':'a','pos':i,'starttime':aslist[i],'endtime':aelist[i]}})
for i in range(0,len(bjlist),1):
    result.update({bjlist[i]:{'vm':'b','pos':i,'starttime':bslist[i],'endtime':belist[i]}})
for i in range(0,len(cjlist),1):
    result.update({cjlist[i]:{'vm':'c','pos':i,'starttime':cslist[i],'endtime':celist[i]}})
if len(djlist) != 0:
    for i in range(0,len(djlist),1):
        result.update({djlist[i]:{'vm':'d','pos':i,'starttime':dslist[i],'endtime':delist[i]}})
if len(ejlist) != 0:
    for i in range(0,len(ejlist),1):
        result.update({ejlist[i]:{'vm':'e','pos':i,'starttime':eslist[i],'endtime':eelist[i]}})
if len(fjlist) != 0:
    for i in range(0,len(fjlist),1):
        result.update({fjlist[i]:{'vm':'f','pos':i,'starttime':fslist[i],'endtime':felist[i]}})
if len(gjlist) != 0:
    for i in range(0,len(gjlist),1):
        result.update({gjlist[i]:{'vm':'g','pos':i,'starttime':gslist[i],'endtime':gelist[i]}})
print(ajlist, '\n', aslist, '\n', aelist)
print(bjlist, '\n', bslist, '\n', belist)
print(cjlist, '\n', cslist, '\n', celist)
print(djlist, '\n', dslist, '\n', delist)
print(ejlist, '\n', eslist, '\n', eelist)
print(fjlist, '\n', fslist, '\n', felist)
print(gjlist, '\n', gslist, '\n', gelist)
# print(result)


"""Add communication cost to the schedule"""
dag = getdict()
reverse_dag = reverse_dict(dag)


for i in range(0, len(ajlist)-1, 1):
    if ajlist[i] in reverse_dag:
        temp = 0
        for j in range(0, len(reverse_dag[ajlist[i]]), 1):
            if temp > commcost(ajlist[i], reverse_dag[ajlist[i]][j]
                                        , result[ajlist[i]]['vm'], result[reverse_dag[ajlist[i]][j]]['vm']):
                temp = commcost(ajlist[i], reverse_dag[ajlist[i]][j]
                                        , result[ajlist[i]]['vm'], result[reverse_dag[ajlist[i]][j]]['vm'])
        aelist[i] += temp
        if temp > aslist[i+1]:
            aelist[i] = aslist[i+1]
for i in range(0, len(bjlist)-1, 1):
    if bjlist[i] in reverse_dag:
        temp = 0
        for j in range(0, len(reverse_dag[bjlist[i]]), 1):
            if temp > commcost(bjlist[i], reverse_dag[bjlist[i]][j]
                                        , result[bjlist[i]]['vm'], result[reverse_dag[bjlist[i]][j]]['vm']):
                temp = commcost(bjlist[i], reverse_dag[bjlist[i]][j]
                                        , result[bjlist[i]]['vm'], result[reverse_dag[bjlist[i]][j]]['vm'])
        belist[i] += temp
        if temp > bslist[i+1]:
            belist[i] = bslist[i+1]
for i in range(0, len(cjlist)-1, 1):
    if cjlist[i] in reverse_dag:
        temp = 0
        for j in range(0, len(reverse_dag[cjlist[i]]), 1):
            if temp > commcost(cjlist[i], reverse_dag[cjlist[i]][j]
                                        , result[cjlist[i]]['vm'], result[reverse_dag[cjlist[i]][j]]['vm']):
                temp = commcost(cjlist[i], reverse_dag[cjlist[i]][j]
                                        , result[cjlist[i]]['vm'], result[reverse_dag[cjlist[i]][j]]['vm'])
        celist[i] += temp
        if temp > cslist[i+1]:
            celist[i] = cslist[i+1]
for i in range(0, len(djlist)-1, 1):
    if djlist[i] in reverse_dag:
        temp = 0
        for j in range(0, len(reverse_dag[djlist[i]]), 1):
            if temp > commcost(djlist[i], reverse_dag[djlist[i]][j]
                                        , result[djlist[i]]['vm'], result[reverse_dag[djlist[i]][j]]['vm']):
                temp = commcost(djlist[i], reverse_dag[djlist[i]][j]
                                        , result[djlist[i]]['vm'], result[reverse_dag[djlist[i]][j]]['vm'])
        delist[i] += temp
        if temp > dslist[i+1]:
            delist[i] = dslist[i+1]
for i in range(0, len(ejlist)-1, 1):
    if ejlist[i] in reverse_dag:
        temp = 0
        for j in range(0, len(reverse_dag[ejlist[i]]), 1):
            if temp > commcost(ejlist[i], reverse_dag[ejlist[i]][j]
                                        , result[ejlist[i]]['vm'], result[reverse_dag[ejlist[i]][j]]['vm']):
                temp = commcost(ejlist[i], reverse_dag[ejlist[i]][j]
                                        , result[ejlist[i]]['vm'], result[reverse_dag[ejlist[i]][j]]['vm'])
        eelist[i] += temp
        if temp > eslist[i+1]:
            eelist[i] = eslist[i+1]
for i in range(0, len(fjlist)-1, 1):
    if fjlist[i] in reverse_dag:
        temp = 0
        for j in range(0, len(reverse_dag[fjlist[i]]), 1):
            if temp > commcost(fjlist[i], reverse_dag[fjlist[i]][j]
                                        , result[fjlist[i]]['vm'], result[reverse_dag[fjlist[i]][j]]['vm']):
                temp = commcost(fjlist[i], reverse_dag[fjlist[i]][j]
                                        , result[fjlist[i]]['vm'], result[reverse_dag[fjlist[i]][j]]['vm'])
        felist[i] += temp
        if temp > fslist[i+1]:
            felist[i] = fslist[i+1]
for i in range(0, len(gjlist)-1, 1):
    if gjlist[i] in reverse_dag:
        temp = 0
        for j in range(0, len(reverse_dag[gjlist[i]]), 1):
            if temp > commcost(gjlist[i], reverse_dag[gjlist[i]][j]
                                        , result[gjlist[i]]['vm'], result[reverse_dag[gjlist[i]][j]]['vm']):
                temp = commcost(gjlist[i], reverse_dag[gjlist[i]][j]
                                        , result[gjlist[i]]['vm'], result[reverse_dag[gjlist[i]][j]]['vm'])
        gelist[i] += temp
        if temp > gslist[i+1]:
            gelist[i] = gslist[i+1]

"""Add commcost(without waitcost) into the schedule result"""


for i in range(1, len(ajlist), 1):
    if ajlist[i] in dag:
        temp = 0
        for j in range(0, len(dag[ajlist[i]]), 1):
            if commcost(dag[ajlist[i]][j], ajlist[i], result[dag[ajlist[i]][j]]['vm']
                    , result[ajlist[i]]['vm']) > temp:
                temp = commcost(dag[ajlist[i]][j], ajlist[i],result[dag[ajlist[i]][j]]['vm'],result[ajlist[i]]['vm'])
        aslist[i] -= temp
        if aslist[i] < aelist[i-1]:
            aslist[i] = aelist[i-1]
for i in range(1, len(bjlist), 1):
    if bjlist[i] in dag:
        temp = 0
        for j in range(0, len(dag[bjlist[i]]), 1):
            if commcost(dag[bjlist[i]][j], bjlist[i], result[dag[bjlist[i]][j]]['vm']
                    , result[bjlist[i]]['vm']) > temp:
                temp = commcost(dag[bjlist[i]][j], bjlist[i], result[dag[bjlist[i]][j]]['vm']
                                , result[bjlist[i]]['vm'])
        bslist[i] -= temp
        if bslist[i] < belist[i - 1]:
            bslist[i] = belist[i - 1]
for i in range(1, len(cjlist), 1):
    if cjlist[i] in dag:
        temp = 0
        for j in range(0, len(dag[cjlist[i]]), 1):
            if commcost(dag[cjlist[i]][j], cjlist[i], result[dag[cjlist[i]][j]]['vm']
                    , result[cjlist[i]]['vm']) > temp:
                temp = commcost(dag[cjlist[i]][j], cjlist[i], result[dag[cjlist[i]][j]]['vm']
                                , result[cjlist[i]]['vm'])
        cslist[i] -= temp
        if cslist[i] < celist[i - 1]:
            cslist[i] = celist[i - 1]
for i in range(1, len(djlist), 1):
    if djlist[i] in dag:
        temp = 0
        for j in range(0, len(dag[djlist[i]]), 1):
            if commcost(dag[djlist[i]][j], djlist[i], result[dag[djlist[i]][j]]['vm']
                    , result[djlist[i]]['vm']) > temp:
                temp = commcost(dag[djlist[i]][j], djlist[i], result[dag[djlist[i]][j]]['vm']
                                , result[djlist[i]]['vm'])
        dslist[i] -= temp
        if dslist[i] < delist[i - 1]:
            dslist[i] = delist[i - 1]
for i in range(1, len(ejlist), 1):
    if ejlist[i] in dag:
        temp = 0
        for j in range(0, len(dag[ejlist[i]]), 1):
            if commcost(dag[ejlist[i]][j], ejlist[i], result[dag[ejlist[i]][j]]['vm']
                    , result[ejlist[i]]['vm']) > temp:
                temp = commcost(dag[ejlist[i]][j], ejlist[i], result[dag[ejlist[i]][j]]['vm']
                                , result[ejlist[i]]['vm'])
        eslist[i] -= temp
        if eslist[i] < eelist[i - 1]:
            eslist[i] = eelist[i - 1]
for i in range(1, len(fjlist), 1):
    if fjlist[i] in dag:
        temp = 0
        for j in range(0, len(dag[fjlist[i]]), 1):
            if commcost(dag[fjlist[i]][j], fjlist[i], result[dag[fjlist[i]][j]]['vm']
                    , result[fjlist[i]]['vm']) > temp:
                temp = commcost(dag[fjlist[i]][j], fjlist[i], result[dag[fjlist[i]][j]]['vm']
                                , result[fjlist[i]]['vm'])
        fslist[i] -= temp
        if fslist[i] < felist[i - 1]:
            fslist[i] = felist[i - 1]
for i in range(1, len(gjlist), 1):
    if gjlist[i] in dag:
        temp = 0
        for j in range(0, len(dag[gjlist[i]]), 1):
            if commcost(dag[gjlist[i]][j], gjlist[i], result[dag[gjlist[i]][j]]['vm']
                    , result[gjlist[i]]['vm']) > temp:
                temp = commcost(dag[gjlist[i]][j], gjlist[i], result[dag[gjlist[i]][j]]['vm']
                                , result[gjlist[i]]['vm'])
        gslist[i] -= temp
        if gslist[i] < gelist[i - 1]:
            gslist[i] = gelist[i - 1]


print(ajlist, '\n', aslist, '\n', aelist)
print(bjlist, '\n', bslist, '\n', belist)
print(cjlist, '\n', cslist, '\n', celist)
print(djlist, '\n', dslist, '\n', delist)
print(ejlist, '\n', eslist, '\n', eelist)
print(fjlist, '\n', fslist, '\n', felist)
print(gjlist, '\n', gslist, '\n', gelist)
"""Build a new DAG for computing InstanceHour"""
"""Set nodes aG"""
# //0-45  75-115  123-188  250-285  290-330  335-370
# ajlist=[0,1,2,3,4,5]
# aslist=[0,75,123,250,290,335]
# aelist=[45,115,188,285,330,370]
for i in range(0,len(ajlist)+1,1):
    if i == 0:
        aG.add_node(i, starttime=aslist[0], endtime=aslist[0])
        print(aG.node[i]["starttime"], aG.node[i]["endtime"])
        continue
    if i == len(ajlist):
        aG.add_node(i, starttime=aelist[i-1], endtime=aelist[i-1])
        print(aG.node[i]["starttime"], aG.node[i]["endtime"])
        continue
    aG.add_node(i, starttime=aelist[i-1], endtime=aslist[i])
    print(aG.node[i]["starttime"],aG.node[i]["endtime"])
# print(G.get_node_data)
"""Set edges aG"""
for i in range(len(ajlist), 0, -1):
    # print('i=:',i)
    for j in range(0, i, 1):
        # print('j=:',j)
        # weight = round((G.node[ajlist[i]]["endtime"] - G.node[ajlist[j]]["starttime"]) / 6)
        # print(weight)
        aG.add_edge(j, i, weight=math.ceil((aG.node[i]["starttime"]-aG.node[j]["endtime"])/60))
        # print(j,i,':',G.get_edge_data(j,i))
# print(G.edges)


"""Set nodes bG"""
for i in range(0, len(bjlist)+1,1):
    if i == 0:
        bG.add_node(i, starttime=bslist[0], endtime=bslist[0])
        print(bG.node[i]["starttime"], bG.node[i]["endtime"])
        continue
    if i == len(bjlist):
        bG.add_node(i, starttime=belist[i-1], endtime=belist[i-1])
        print(bG.node[i]["starttime"], bG.node[i]["endtime"])
        continue
    bG.add_node(i, starttime=belist[i-1], endtime=bslist[i])
    print(bG.node[i]["starttime"],bG.node[i]["endtime"])
"""Set edges bG"""
for i in range(len(bjlist), 0, -1):
    for j in range(0, i, 1):
        bG.add_edge(j, i, weight=math.ceil((bG.node[i]["starttime"]-bG.node[j]["endtime"])/60))


"""Set nodes cG"""
for i in range(0, len(cjlist)+1,1):
    if i == 0:
        cG.add_node(i, starttime=cslist[0], endtime=cslist[0])
        print(cG.node[i]["starttime"], cG.node[i]["endtime"])
        continue
    if i == len(cjlist):
        cG.add_node(i, starttime=celist[i-1], endtime=celist[i-1])
        print(cG.node[i]["starttime"], cG.node[i]["endtime"])
        continue
    cG.add_node(i, starttime=celist[i-1], endtime=cslist[i])
    print(cG.node[i]["starttime"],cG.node[i]["endtime"])
"""Set edges cG"""
for i in range(len(cjlist), 0, -1):
    for j in range(0, i, 1):
        cG.add_edge(j, i, weight=math.ceil((cG.node[i]["starttime"]-cG.node[j]["endtime"])/60))


if len(djlist) != 0:
    """Set nodes dG"""
    for i in range(0, len(djlist) + 1, 1):
        if i == 0:
            dG.add_node(i, starttime=dslist[0], endtime=dslist[0])
            print(dG.node[i]["starttime"], dG.node[i]["endtime"])
            continue
        if i == len(djlist):
            dG.add_node(i, starttime=delist[i - 1], endtime=delist[i - 1])
            print(dG.node[i]["starttime"], dG.node[i]["endtime"])
            continue
        dG.add_node(i, starttime=delist[i - 1], endtime=dslist[i])
        print(dG.node[i]["starttime"], dG.node[i]["endtime"])
    """Set edges dG"""
    for i in range(len(djlist), 0, -1):
        for j in range(0, i, 1):
            dG.add_edge(j, i, weight=math.ceil((dG.node[i]["starttime"] - dG.node[j]["endtime"]) / 60))


if len(ejlist) != 0:
    """Set nodes eG"""
    for i in range(0, len(ejlist) + 1, 1):
        if i == 0:
            eG.add_node(i, starttime=eslist[0], endtime=eslist[0])
            print(eG.node[i]["starttime"], eG.node[i]["endtime"])
            continue
        if i == len(ejlist):
            eG.add_node(i, starttime=eelist[i - 1], endtime=eelist[i - 1])
            print(eG.node[i]["starttime"], eG.node[i]["endtime"])
            continue
        eG.add_node(i, starttime=eelist[i - 1], endtime=eslist[i])
        print(eG.node[i]["starttime"], eG.node[i]["endtime"])
    """Set edges eG"""
    for i in range(len(ejlist), 0, -1):
        for j in range(0, i, 1):
            eG.add_edge(j, i, weight=math.ceil((eG.node[i]["starttime"] - eG.node[j]["endtime"]) / 60))


if len(fjlist) != 0:
    """Set nodes fG"""
    for i in range(0, len(fjlist) + 1, 1):
        if i == 0:
            fG.add_node(i, starttime=fslist[0], endtime=fslist[0])
            print(fG.node[i]["starttime"], fG.node[i]["endtime"])
            continue
        if i == len(fjlist):
            fG.add_node(i, starttime=felist[i - 1], endtime=felist[i - 1])
            print(fG.node[i]["starttime"], fG.node[i]["endtime"])
            continue
        fG.add_node(i, starttime=felist[i - 1], endtime=fslist[i])
        print(fG.node[i]["starttime"], fG.node[i]["endtime"])
    """Set edges fG"""
    for i in range(len(fjlist), 0, -1):
        for j in range(0, i, 1):
            fG.add_edge(j, i, weight=math.ceil((fG.node[i]["starttime"] - fG.node[j]["endtime"]) / 60))


if len(gjlist) != 0:
    """Set nodes gG"""
    for i in range(0, len(gjlist) + 1, 1):
        if i == 0:
            gG.add_node(i, starttime=gslist[0], endtime=gslist[0])
            print(gG.node[i]["starttime"], gG.node[i]["endtime"])
            continue
        if i == len(gjlist):
            gG.add_node(i, starttime=gelist[i - 1], endtime=gelist[i - 1])
            print(gG.node[i]["starttime"], gG.node[i]["endtime"])
            continue
        gG.add_node(i, starttime=gelist[i - 1], endtime=gslist[i])
        print(gG.node[i]["starttime"], gG.node[i]["endtime"])
    """Set edges dG"""
    for i in range(len(gjlist), 0, -1):
        for j in range(0, i, 1):
            gG.add_edge(j, i, weight=math.ceil((gG.node[i]["starttime"] - gG.node[j]["endtime"]) / 60))

"""Find the minimum path"""
apath = nx.dijkstra_path(aG, 0, len(ajlist), weight='weight')
bpath = nx.dijkstra_path(bG, 0, len(bjlist), weight='weight')
cpath = nx.dijkstra_path(cG, 0, len(cjlist), weight='weight')
dpath = nx.dijkstra_path(dG, 0, len(djlist), weight='weight')
epath = nx.dijkstra_path(eG, 0, len(ejlist), weight='weight')
fpath = nx.dijkstra_path(fG, 0, len(fjlist), weight='weight')
gpath = nx.dijkstra_path(gG, 0, len(gjlist), weight='weight')
print(apath, '\n', bpath, '\n', cpath, '\n', dpath, '\n', epath, '\n', fpath, '\n', gpath)
# weight=nx.get_edge_attributes(G,'weight')
atemp = 0
btemp = 0
ctemp = 0
dtemp = 0
etemp = 0
ftemp = 0
gtemp = 0
# for i in range(0, len(path)-1, 1):
#     print(G.get_edge_data(path[i], path[i+1]))
    # temp += G.get_edge_data(path[i], path[i+1])['weight']
    # print (G[path[i]][path[i+1]]['weight'])
    # print(weight[(path[i],path[i+1])])
# print(temp)
# for i in range(len(ajlist), -1, -1):
#     for j in range(0, i, 1):
#         print((j, i), ':', G.get_edge_data(j, i))

"""print vm start time and end time"""
for i in range(0, len(apath)-1, 1):
    print('vm[a] start time:', aG.node[apath[i]]['endtime'], 'end time:', aG.node[apath[i+1]]['starttime']
          , aG.get_edge_data(apath[i], apath[i+1]))
    atemp += aG.get_edge_data(apath[i], apath[i + 1])['weight']
for i in range(0, len(bpath)-1, 1):
    print('vm[b] start time:', bG.node[bpath[i]]['endtime'], 'end time:', bG.node[bpath[i+1]]['starttime']
          , bG.get_edge_data(bpath[i], bpath[i+1]))
    btemp += bG.get_edge_data(bpath[i], bpath[i + 1])['weight']
for i in range(0, len(cpath)-1, 1):
    print('vm[c] start time:', cG.node[cpath[i]]['endtime'], 'end time:', cG.node[cpath[i+1]]['starttime']
          , cG.get_edge_data(cpath[i], cpath[i+1]))
    ctemp += cG.get_edge_data(cpath[i], cpath[i + 1])['weight']
for i in range(0, len(dpath)-1, 1):
    print('vm[d] start time:', dG.node[dpath[i]]['endtime'], 'end time:', dG.node[dpath[i+1]]['starttime']
          , dG.get_edge_data(dpath[i], dpath[i+1]))
    dtemp += dG.get_edge_data(dpath[i], dpath[i + 1])['weight']
for i in range(0, len(epath)-1, 1):
    print('vm[e] start time:', eG.node[epath[i]]['endtime'], 'end time:', eG.node[epath[i+1]]['starttime']
          , eG.get_edge_data(epath[i], epath[i+1]))
    etemp += eG.get_edge_data(epath[i], epath[i + 1])['weight']
for i in range(0, len(fpath)-1, 1):
    print('vm[f] start time:', fG.node[fpath[i]]['endtime'], 'end time:', fG.node[fpath[i+1]]['starttime']
          , fG.get_edge_data(fpath[i], fpath[i+1]))
    ftemp += fG.get_edge_data(fpath[i], fpath[i + 1])['weight']
for i in range(0, len(gpath)-1, 1):
    print('vm[g] start time:', gG.node[gpath[i]]['endtime'], 'end time:', gG.node[gpath[i+1]]['starttime']
          , gG.get_edge_data(gpath[i], gpath[i+1]))
    gtemp += gG.get_edge_data(gpath[i], gpath[i + 1])['weight']
print('total instance hour:', atemp, btemp, ctemp, dtemp, etemp, ftemp, gtemp)
"""Draw the DAG"""
# nx.draw(G,pos = nx.random_layout(G),node_color = 'b',edge_color = 'r',with_labels = True,font_size =12,node_size =40)
# plt.show()
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