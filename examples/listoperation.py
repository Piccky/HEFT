list1 = [0, 75, 123, 250, 290, 335]
list2 = [45, 115, 188, 285, 330, 370]
list3 = [0, 1, 2, 3, 4, 5]
print('The original job scheduling result：', '\n', 'Start time list', list1, '\n', 'End time list', list2)
list1 = [0, 70, 120, 230, 280, 330]
list2 = [50, 125, 190, 290, 335, 370]
print('Example result for adding commcost:', '\n', 'Start time list', list1,'\n', 'End time list', list2)


def getVmList(list1, list2, list3):
    i = 0
    j = len(list1)
    """j=3"""
    """i=0,1 """
    while i < j - 1:
        k = 1
        while k < j - i:
        # for k in range(0, j-i, 1):
        #     if k == 0 or i+k > j-1:
        #         continue
            # if list2[i] == list1[i + k]:
            #     list2[i] = list2[i + k]
            #     del list1[i + k]
            #     del list2[i + k]
            #     del list3[i + k]
            #     j -= 1
            #     i -= 1
            #     if i < 0:
            #         i = 0
            if list2[i] >= list1[i + k]:
                if list1[i] >= list1[i + k]:
                    list1[i] = list1[i + k]
                if list2[i] <= list2[i + k]:
                    list2[i] = list2[i + k]
                del list1[i + k]
                del list2[i + k]
                del list3[i + k]
                j -= 1
                continue
            #     i -= 1
            #     if i < 0:
            #         i = 0
            else:
                k += 1
        i += 1


    return list1, list2

# def getVmList(list1, list2, list3):
#     slist = []
#     elist = []
#     slist[0] = list1[0]
#     elist[0] = list2[0]
#     for i in range(0, len(list1), 1):
#         if i == 0:
#             continue
#         for j in range(0, len(slist), 1):
#             if list1[i] > elist[j]:
#                 slist[len(slist)] = list1[i]
#                 elist[len(elist)] = list2[i]
#             if list1[i] <=
#
#


def recruise(getVmlist,list1,list2,list3):
    slist, elist = getVmList(list1, list2, list3)
    temp1, temp2 = getVmList(slist, elist, list3)
    while slist != temp1 and elist!= temp2:
        temp1, temp2 = getVmList(temp1, temp2, list3)
    return temp1, temp2


list1, list2 = recruise(getVmList, list1, list2, list3)
print('VM busy:', '\n','Start time list', list1, '\n','End time list', list2)

