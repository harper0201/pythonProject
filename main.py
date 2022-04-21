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
    agent2 = Agent(2,2,3)
    agent3 = Agent(3,3,1)
    agent4 = Agent(4,3,1)
    dic = {agent1: agent2,agent3:agent4};
    for key in dic:
            transaction(key,dic[key])
    agent1.displayAgent()

#hx wo ai ni
# i love whj
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
