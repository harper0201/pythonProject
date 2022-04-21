# This is a sample Python script.

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


def transaction(agent1, agent2):
    pass


if __name__ == '__main__':
    agent1 = Agent(1,1,2)
    agent2 = Agent(2,1,2)
    agent3 = Agent(3,1,2)
    agent4 = Agent(4,1,2)
    agent5 = Agent(5,1,2)
    agent6 = Agent(6,1,2)
    agent7 = Agent(7,2,3)
    agent8 = Agent(8,2,3)
    agent9 = Agent(9,2,3)
    dic = {agent1: agent2,agent3:agent4};
    for key in dic:
            transaction(key,dic[key])
    agent1.displayAgent()

#hx wo ai ni
# i love whj
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
