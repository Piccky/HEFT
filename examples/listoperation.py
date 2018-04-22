# list1 = [0, 25, 35, 55, 88]
# list2 = [22, 45, 65, 85, 105]

def getVmList(list1, list2, list3):
    i = 0
    j = len(list1)
    while i < j - 1:
        if list2[i] > list1[i + 1]:
            if list1[i] > list1[i + 1]:
                list1[i] = list1[i + 1]
            if list2[i] < list2[i + 1]:
                list2[i] = list2[i + 1]
            del list1[i + 1]
            del list2[i + 1]
            del list3[i + 1]
            j -= 1
            i -= 1
        i += 1
    return list1, list2
# print(list1, list2)
