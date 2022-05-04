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
        self.opposite_storage = 0
        self.trading_result = False
        self.trading = False
        self.original_storage = self.storage_type

        #generate type 1 agents' Q(precieved value for holding good 1 , 2 , 3)
        if self.consume_type == 1:
            self.Q_2 = 65 + random.randint(1, 50)
        if self.consume_type == 1:
            self.Q_3 = 103 + random.randint(1, 50)
        if self.consume_type == 1:
            self.Q_1 = 9999
            
        #generate type 2 agents' Q(precieved value for holding good 1 , 2 , 3)
        if self.consume_type == 2:
            self.Q_1 = 256 + random.randint(1, 50)
        if self.consume_type == 2:
            self.Q_3 = 244 + random.randint(1, 50)
        if self.consume_type == 2:
            self.Q_2 = 9999
            
        #generate type 3 agents' Q(precieved value for holding good 1 , 2 , 3)
        if self.consume_type == 3:
            self.Q_1 = 290 + random.randint(1, 50)
        if self.consume_type == 3:
            self.Q_2 = 230 + random.randint(1, 50)
        if self.consume_type == 3:
            self.Q_3 = 9999

        # other characteristics wait to be added
        Agent.agentCount += 1

    def displayAgent(self):
        print("Agent id:", self.id, "consume:", self.consume_type, ",produce:", self.product_type, ",storage:",
              self.storage_type, "Q_1:", self.Q_1, "Q_2:", self.Q_2, "Q_3:", self.Q_3,"opposite:",self.opposite_storage,"trading:",self.trading,"trading_reuslt:",self.trading_result)

        
# matching process
# update agent's information of what situation he is facing
def match(mylist):
    random.shuffle(mylist)
    matchlist = dict()
    index = list(range(0, len(mylist), 2))
    for i in index:
        matchlist[mylist[i]] = mylist[i + 1]
    for key in matchlist:
        update_opposite_storage(key,matchlist[key])
        key.original_storage = key.storage_type #easy to update Q at the end of the round
        matchlist[key].original_storage = matchlist[key].storage_type
    return matchlist

# update what good the other agent is holding
def update_opposite_storage(agent1, agent2):
    storage_1 = agent1.storage_type
    storage_2 = agent2.storage_type
    agent1.opposite_storage = storage_2
    agent2.opposite_storage = storage_1

    

#get the parameters for decision making and updating Q
def get_Q_hold(agent):
    if agent.storage_type == 1:
        return agent.Q_1
    elif agent.storage_type == 2:
        return agent.Q_2
    elif agent.storage_type == 3:
        return agent.Q_3

def get_original_Q_hold(agent):
    if agent.original_storage == 1:
        return agent.Q_1
    elif agent.original_storage == 2:
        return agent.Q_2
    elif agent.original_storage == 3:
        return agent.Q_3

def set_Q_hold(agent,update_value):
    if agent.storage_type == 1:
        agent.Q_1 = update_value
    elif agent.storage_type == 2:
        agent.Q_2 = update_value
    elif agent.storage_type == 3:
        agent.Q_3 = update_value

        
def set_original_Q_hold(agent,update_value):
    if agent.original_storage == 1:
        agent.Q_1 = update_value
    elif agent.original_storage == 2:
        agent.Q_2 = update_value
    elif agent.original_storage == 3:
        agent.Q_3 = update_value

def get_Q_trade(agent):
    if agent.opposite_storage == 1:
        return agent.Q_1
    elif agent.opposite_storage == 2:
        return agent.Q_2
    elif agent.opposite_storage == 3:
        return agent.Q_3

def get_C_hold(agent):
    if agent.storage_type == 1:
        return c_1
    elif agent.storage_type == 2:
        return c_2
    elif agent.storage_type == 3:
        return c_3

def get_C_trade(agent):
    if agent.opposite_storage == 1:
        return c_1
    elif agent.opposite_storage == 2:
        return c_2
    elif agent.opposite_storage == 3:
        return c_3

# trading decision by each agent
def transaction_decision(agent):
    Q_hold = get_Q_hold(agent)
    Q_trade = get_Q_trade(agent)
    C_hold = get_C_hold(agent)
    C_trade = get_C_trade(agent)

    if β * Q_hold - C_hold < β * Q_trade - C_trade:
        agent.trading = True
    else:
        agent.trading = False

# trading result
def produce_outcome(matched_list):
    trade_outcome = list()
    for key in matched_list.keys():
        if key.trading == True and matched_list[key].trading == True:
            trade_outcome.append(True)
            key.trading_result = True
            matched_list[key].trading_result = True
        else:
            trade_outcome.append(False)
            key.trading_result = False
            matched_list[key].trading_result = False
    return trade_outcome

# based on trading result, updates Q and storage

def update_trading(agent):
    if(agent.trading_result == False): #if there is trade
        v_prime = get_C_hold(agent)*(-1) + β * get_Q_hold(agent)
        updated_value = get_Q_hold(agent) + γ * (v_prime - get_Q_hold(agent))
        set_Q_hold(agent,updated_value)
    else: #if trade happened 
        if agent.consume_type == agent.opposite_storage: #agent gets his own consumption good
            agent.storage_type = agent.product_type #agent eats the consumption good and produces another production good 
            v_prime = get_C_hold(agent) * (-1) + β * get_Q_hold(agent) + u
            updated_value = get_original_Q_hold(agent) + γ * (v_prime - get_original_Q_hold(agent))
            set_original_Q_hold(agent,updated_value)
        else: #agent does not get his cons good
            agent.storage_type = agent.opposite_storage 
            v_prime = get_C_hold(agent) *(-1) + β * get_Q_hold(agent)
            updated_value = get_original_Q_hold(agent) + γ * (v_prime - get_original_Q_hold(agent))
            set_original_Q_hold(agent, updated_value)

            
# Global behavior recorder

def global_a1_s2_f3(mylist,count_down,count_up): #agent 1 holding 2 facing opportunity for 3
    result = list()
    for ele in mylist:
        if (ele.consume_type == 1 and ele.storage_type == 2 and ele.opposite_storage == 3):
            count_down += 1
            if (ele.trading == True):
                count_up += 1

    result.append(count_up)
    result.append(count_down)
    return result

def global_a2_s3_f1(mylist,count_down,count_up): #agent 2 holding 3 facing opportunity for 1
    result = list()
    for ele in mylist:
        if (ele.consume_type == 2 and ele.storage_type == 3 and ele.opposite_storage == 1):
            count_down += 1
            if (ele.trading == True):
                count_up += 1

    result.append(count_up)
    result.append(count_down)
    return result

def global_a3_s1_f2(mylist,count_down,count_up): #agent 3 holding 1 facing opportunity for 2
    result = list()
    for ele in mylist:
        if (ele.consume_type == 3 and ele.storage_type == 1 and ele.opposite_storage == 2):
            count_down += 1
            if (ele.trading == True):
                count_up += 1

    result.append(count_up)
    result.append(count_down)
    return result


# main code

if __name__ == '__main__':
    u = 100
    β = 0.9
    c_1 = 1
    c_2 = 4
    c_3 = 9
    t = 1
    γ = 1/t

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

    game_continue = True

    count_round = 0
    sum_up123 = 0
    sum_down123 = 0
    sum_up231 = 0
    sum_down231 = 0
    sum_up312 = 0
    sum_down312 = 0
    
    while(count_round < 140 ):
        count_round += 1
        t = t+1
        matched_list = match(mylist)

        for key in matched_list.keys():
            transaction_decision(key)
            transaction_decision(matched_list[key])

        global_r1_2_3 = global_a1_s2_f3(mylist,0,0)
        sum_up123 = sum_up123 + global_r1_2_3[0]
        sum_down123 = sum_down123 + global_r1_2_3[1]
        
        global_r2_3_1 = global_a2_s3_f1(mylist,0,0)
        sum_up231 = sum_up231 + global_r2_3_1[0]
        sum_down231 = sum_down231 + global_r2_3_1[1]
        
        global_r3_1_2 = global_a3_s1_f2(mylist,0,0)
        sum_up312 = sum_up312 + global_r3_1_2[0]
        sum_down312 = sum_down312 + global_r3_1_2[1]

        for ele in mylist:
            ele.displayAgent()

        produce_outcome(matched_list)

        for key in matched_list.keys():
            update_trading(key)
            update_trading(matched_list[key])

        print(count_round)

        stopping_draw = random.uniform(0, 1)
        if stopping_draw > 0.01:
            game_continue = True
        else:
            game_continue = False

    print("Agent 1 with good 2 facing good 3:", sum_up123/sum_down123)
    print("Agent 2 with good 3 facing good 1:", sum_up231/sum_down231)
    print("Agent 3 with good 1 facing good 2:", sum_up312/sum_down312)
    
#hx wo ai ni
# i love zw
# See PyCharm help at https://www.jetbrains.com/help/pycharm/