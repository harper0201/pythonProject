# Create agents
import random
# Agents have there type which same as there consumption type, they also have production type
class Agent:
    agentCount = 0

    def __init__(self, id, consume_type, product_type):
        self.id = id
        self.consume_type = consume_type
        self.product_type = product_type
        self.storage_type = product_type
        self.trading = False
        if self.consume_type == 1:
            self.Q_2 = 65 + random.randint(1, 10)
        if self.consume_type == 1:
            self.Q_3 = 103 + random.randint(1, 10)
        if self.consume_type == 1:
            self.Q_1 = 65 + u + random.randint(1, 10)

        if self.consume_type == 2:
            self.Q_1 = 256 + random.randint(1, 10)
        if self.consume_type == 2:
            self.Q_3 = 244 + random.randint(1, 10)
        if self.consume_type == 2:
            self.Q_2 = 244 + u + random.randint(1, 10)

        if self.consume_type == 3:
            self.Q_1 = 290 + random.randint(1, 10)
        if self.consume_type == 3:
            self.Q_2 = 230 + random.randint(1, 10)
        if self.consume_type == 3:
            self.Q_3 = 290 + u + random.randint(1, 10)

        # other characteristics wait to be added
        Agent.agentCount += 1

    def displayAgent(self):
        print("Agent id:", self.id, "consume:", self.consume_type, ",produce:", self.product_type, ",storage:",
              self.storage_type, "Q_1:", self.Q_1, "Q_2:", self.Q_2, "Q_3:", self.Q_3,"trading:",self.trading)

        # matching process

def match(mylist):
    random.shuffle(mylist)
    matchlist = dict()
    index = list(range(0, len(mylist), 2))
    for i in index:
        matchlist[mylist[i]] = mylist[i + 1]
    return matchlist

def get_Q_hold(agent):
    if agent.storage_type == 1:
        return agent.Q_1
    elif agent.storage_type == 2:
        return agent.Q_2
    elif agent.storage_type == 3:
        return agent.Q_3

def get_Q_trade(agent1,agent2):
    if agent2.storage_type == 1:
        return agent1.Q_1
    elif agent2.storage_type == 2:
        return agent1.Q_2
    elif agent2.storage_type == 3:
        return agent1.Q_3

def get_C_hold(agent):
    if agent.storage_type == 1:
        return c_1
    elif agent.storage_type == 2:
        return c_2
    elif agent.storage_type == 3:
        return c_3

def transaction(agent1, agent2):
    Q_hold = get_Q_hold(agent1)
    Q_trade = get_Q_trade(agent1,agent2)
    C_hold = get_C_hold(agent1)
    C_trade = get_C_hold(agent2)

    if β * Q_hold - C_hold < β * Q_trade - C_trade:
        agent1.trading = True
    else:
        agent1.trading = False

def produce_outcome(matched_list):
    trade_outcome = list()
    for key in matched_list.keys():
        if key.trading == True and matched_list[key].trading == True:
            trade_outcome.append(True)
        else:
            trade_outcome.append(False)
    return trade_outcome

if __name__ == '__main__':
    u = 100
    β = 0.9
    c_1 = 1
    c_2 = 4
    c_3 = 9
    t = 1
    mylist = list()
    agent1 = Agent(1, 1, 2)
    mylist.append(agent1)
    agent2 = Agent(2, 1, 2)
    mylist.append(agent2)
    agent3 = Agent(3, 1, 2)
    mylist.append(agent3)
    agent4 = Agent(4, 1, 2)
    mylist.append(agent4)
    agent5 = Agent(5, 1, 2)
    mylist.append(agent5)
    agent6 = Agent(6, 1, 2)
    mylist.append(agent6)
    agent7 = Agent(7, 1, 2)
    mylist.append(agent7)
    agent8 = Agent(8, 1, 2)
    mylist.append(agent8)
    agent9 = Agent(9, 2, 3)
    mylist.append(agent9)
    agent10 = Agent(10, 2, 3)
    mylist.append(agent10)
    agent11 = Agent(11, 2, 3)
    mylist.append(agent11)
    agent12 = Agent(12, 2, 3)
    mylist.append(agent12)
    agent13 = Agent(13, 2, 3)
    mylist.append(agent13)
    agent14 = Agent(14, 2, 3)
    mylist.append(agent14)
    agent15 = Agent(15, 2, 3)
    mylist.append(agent15)
    agent16 = Agent(16, 2, 3)
    mylist.append(agent16)
    agent17 = Agent(17, 3, 1)
    mylist.append(agent17)
    agent18 = Agent(18, 3, 1)
    mylist.append(agent18)
    agent19 = Agent(19, 3, 1)
    mylist.append(agent19)
    agent20 = Agent(20, 3, 1)
    mylist.append(agent20)
    agent21 = Agent(21, 3, 1)
    mylist.append(agent21)
    agent22 = Agent(22, 3, 1)
    mylist.append(agent22)
    agent23 = Agent(23, 3, 1)
    mylist.append(agent23)
    agent24 = Agent(24, 3, 1)
    mylist.append(agent24)
    matched_list = match(mylist)

    for key in matched_list.keys():
        print(key.id,matched_list[key].id)

    for key in matched_list.keys():
        transaction(key,matched_list[key])
        transaction(matched_list[key],key)

    for ele in mylist:
        ele.displayAgent()

    print(produce_outcome(matched_list))

#hx wo ai ni
# i love zw
# See PyCharm help at https://www.jetbrains.com/help/pycharm/