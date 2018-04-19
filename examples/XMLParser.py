"""
遗留问题
    dict 没有根据 keys 排序，sorted函数有问题

"""

try:
    import xml.etree.cElementTree as ET
    from heft.util import reverse_dict
    from heft.core import (wbar, cbar, ranku, schedule, Event, start_time,
                           makespan, endtime, insert_recvs, insert_sends, insert_sendrecvs, recvs,
                           sends)
    #import itertools as it
except ImportError:
    import xml.etree.ElementTree as ET

# def reverse_dict(d):
#     """ Reverses direction of dependence dict
#
#     >>> d = {'a': (1, 2), 'b': (2, 3), 'c':()}
#     >>> reverse_dict(d)
#     {1: ('a',), 2: ('a', 'b'), 3: ('b',)}
#     """
#     result = {}
#     for key in d:
#         for val in d[key]:
#             result[val] = result.get(val, tuple()) + (key, )
#     sorted(result.keys())
#     return result

tree = ET.parse("Montage_1000.xml")  # <class 'xml.etree.ElementTree.ElementTree'>
root = tree.getroot()           # 获取根节点 <Element 'data' at 0x02BF6A80>
# print(root.tag, ":", root.attrib)  # 打印根元素的tag和属性
# 遍历xml文档的第二层
dict = {}
jobs_tup = ()
# job_dict = {}
# users_tup = ()
# user_dict = {}
for child in root:
    if (child.get('ref') == None):
        # print(child.attrib)
        job_dict = {}
        job_dict.update({'name': child.get('name'), })
        job_dict.update({'version': child.get('version'), })
        job_dict.update({'runtime': child.get('runtime'), })
        job_dict.update({'namespace': child.get('namespace'), })
        job_dict.update({'id': child.get('id'), })
        users_tup = ()
        for children in child:
            # print(children.attrib)
            user_dict = {}
            user_dict.update({'size': children.get('size')})
            user_dict.update({'type': children.get('type')})
            user_dict.update({'optional': children.get('optional')})
            user_dict.update({'transfer': children.get('transfer')})
            user_dict.update({'register': children.get('register')})
            user_dict.update({'link': children.get('link')})
            user_dict.update({'file': children.get('file')})
            temp = (user_dict, )
            users_tup = users_tup + temp
            # print(users_tup)
        # print(users_tup)
        job_dict.update({'uses':  users_tup})
        # print(job_dict)
        temp_tup = (job_dict,)
        jobs_tup += temp_tup
    else:
        # 第二层节点的标签名称和属性
        # print("\t",child.tag,":", child.attrib)
        # print('\t'+child.get('ref'))
        tup = ()
        # 遍历xml文档的第三层
        for children in child:
            # 第三层节点的标签名称和属性
            # print('\t\t'+children.get('ref'));
            temp = (children.get('ref'), )
            tup = tup + temp
        # print(tup)
        dict.update({child.get('ref'): tup, })
# print(dict)
dag = reverse_dict(dict)
# print(jobs)
# print(jobs_tup)
# print(dict.keys()[0])

def getdag():
    return dag


def getjobs_tup():
    return jobs_tup


def getdict():
    return dict
def compcost(job, agent):
    if agent != None:
        for i in jobs_tup:
            # job={}
            #    job=eval('jobs_tup[i]')
            if(i['id'] == job):
                time = round(float(i['runtime']), 2)
                return time
# print (compcost('ID00000'))
# print(jobs_tup[0])
# job=eval('jobs_tup[0]')
# print(job)

#     if(job_dict['id']==job):
#     return
# print(job_dict)


def commcost(ni, nj, A, B):
    if A == B:
        return 0
    else:
        size = 0
        for i in jobs_tup:
            if i['id'] != ni:
                continue
            else:
                idict = {}
                for m in i['uses']:
                    if m['link'] == 'output':
                        idict.update({m['file']: m['size']})
                jdict = {}
                for j in jobs_tup:
                    if j['id'] != nj:
                        continue
                    else:
                        for n in j['uses']:
                            if n['link'] == 'input':
                                jdict.update({n['file']: n['size']})
                for k in idict:
                    for p in jdict:
                        if k == p:
                            size += int(jdict[p])
        time = float(size/1024000)
        return time
# print(commcost('ID00000','ID00005','A','B'))
        # link = "output" size="4167312" file="region.hdr


orders, jobson = schedule(dag, 'abcdef', compcost, commcost)
"""print orders"""
for eachP in sorted(orders):
    print(eachP, orders[eachP])
# print(orders['a'][0][0],orders['a'][0][1],orders['a'][0][2])
# print(jobson)
def getorders():
    return orders
