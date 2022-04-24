# This is a sample Python script.
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Agent:
    agentCount = 0
    def __init__(self,id,consume_type,product_type):
        self.id = id
        self.consume_type = consume_type
        self.product_type = product_type
        self.storage_type = product_type
        Agent.agentCount += 1

    def displayAgent(self):
        print("consume:", self.consume_type, ",produce:", self.product_type, ",storage:",
              self.storage_type)


def match(mylist):
    random.shuffle(mylist)
    matchlist = dict()
    index = list(range(0, len(mylist), 2))
    for i in index:
        matchlist[mylist[i]] = mylist[i+1]
    return matchlist


if __name__ == '__main__':
    mylist = list()
    agent1 = Agent(1,1,2)
    mylist.append(agent1)
    agent2 = Agent(2,1,2)
    mylist.append(agent2)
    agent3 = Agent(3,1,2)
    mylist.append(agent3)
    agent4 = Agent(4,1,2)
    mylist.append(agent4)
    agent5 = Agent(5,1,2)
    mylist.append(agent5)
    agent6 = Agent(6,1,2)
    mylist.append(agent6)
    agent7 = Agent(7,1,2)
    mylist.append(agent7)
    agent8 = Agent(8,1,2)
    mylist.append(agent8)
    agent9 = Agent(9,2,3)
    mylist.append(agent9)
    agent10 = Agent(10,2,3)
    mylist.append(agent10)
    agent11 = Agent(11,2,3)
    mylist.append(agent11)
    agent12 = Agent(12,2,3)
    mylist.append(agent12)
    agent13 = Agent(13,2,3)
    mylist.append(agent13)
    agent14 = Agent(14,2,3)
    mylist.append(agent14)
    agent15 = Agent(15,2,3)
    mylist.append(agent15)
    agent16 = Agent(16,2,3)
    mylist.append(agent16)
    agent17 = Agent(17,3,1)
    mylist.append(agent17)
    agent18 = Agent(18,3,1)
    mylist.append(agent18)
    agent19 = Agent(19,3,1)
    mylist.append(agent19)
    agent20 = Agent(20,3,1)
    mylist.append(agent20)
    agent21 = Agent(21,3,1)
    mylist.append(agent21)
    agent22 = Agent(22,3,1)
    mylist.append(agent22)
    agent23 = Agent(23,3,1)
    mylist.append(agent23)
    agent24 = Agent(24,3,1)
    mylist.append(agent24)

    matched_list = match(mylist)
    for key in matched_list.keys():
            print(key.id,matched_list[key].id)
#hx wo ai ni
# i love zw
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
