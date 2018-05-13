from examples.XMLParser import getjobs_tup, getdag, commcost, compcost
from heft.util import reverse_dict
from examples.InsHour import getvm, geteL, getG
# import re
class Pro:
    def __init__(self, pro_id, compcost, previous, commcost, pro_list):
        if pro_id == 0:
            self.commcost = 0
            self.compcost = 0
        else:
            self.commcost = commcost
            self.compcost = compcost(pro_id, 'agent')
        self.pro_id = pro_id
        # self.require_time = require_time
        self.previous = previous
        # self.commcost=commcost
        # self.status = False
        pro_list.append(self)

        # def Test(self):

    #   for item in self.previous:
    #       if pro_list[item].status == False:
    #           return False
    #   return True
    def ShowSelf(self):
        print(self.pro_id, self.compcost, self.previous,)
        # self.status,

    # def Pro_Finish(self):
    #   self.status = True
    def run(self):
        total = 0
        tmp = []
        if self.pro_id == 0:
            return 0
        a = len(self.previous)
        for x in range(a):
            # if x == 0:
            #     return total
            #     # tmp.append(pro_list[x].run() + float(self.require_time)
            #     #            + self.commcost(self.pro_id, self.previous[x], 'A', 'B'))
            # else:
            for i in pro_list:
                if i.pro_id == self.previous[x]:
                    n = i
                    m = pro_list.index(n)
                    tmp.append(pro_list[m].run() + self.compcost
                               + self.commcost(self.previous[x], self.pro_id, 'A', 'B'))
        # print(tmp)
        total = max(tmp)
        # print(total)
        return total


dag = reverse_dict(getdag())
jobs_tup = getjobs_tup()
pro_list = []
pro_0 = Pro(0, compcost, [0], commcost, pro_list)

# pro_0.status = True
list1 = [pro_0]

for index in range(len(jobs_tup)):
    a = jobs_tup[index]['id']
    if a not in dag:
        # pro_1 = Pro(jobs_tup[index]['id'], jobs_tup[index]['runtime'], [0], commcost, pro_list)
        list1.append(Pro(jobs_tup[index]['id'], compcost, [0], commcost, pro_list))
    else:
        # pro_1 = Pro(jobs_tup[index]['id'], jobs_tup[index]['runtime'], list(dag[a]), commcost, pro_list)
        list1.append(Pro(jobs_tup[index]['id'], compcost, list(dag[a]), commcost, pro_list))
        # list[index] = Pro(jobs_tup[index]['id'], jobs_tup[index]['runtime'], dag['jobs_tup[index]['id']'], commcost, pro_list)
    # print(jobs_tup[index]['id'], jobs_tup[index]['runtime'],list(dag[a]))


total_time = list1[len(jobs_tup)].run()
print("Total_time:", total_time)
max = 0
vm = getvm()
eL = geteL()
G = getG()
for i in range(0, len(G), 1):
    if eL[vm[i]][len(eL[vm[i]]) - 1] > max:
        max = eL[vm[i]][len(eL[vm[i]]) - 1]
print(max/total_time)
