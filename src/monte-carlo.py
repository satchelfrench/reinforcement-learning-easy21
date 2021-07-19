import random
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import os
import sys
import numpy as np

root_dir = os.path.dirname( __file__ )
src_dir = os.path.join(root_dir, '..')
sys.path.append(src_dir)

from src.environment import Easy21

'''
An agent learning to play Easy21 via monte-carlo learning

Initialize the policy
Initialize the value function

Loop:
- Take actions according to policy (e-greedy on action-value function) until episode is complete
    - Record the reward for state, action pairs
- Evaluate action-value function with monte carlo learning
    - Average
'''

'''
Action-value function
Q(s,a) -> predicts the total discounted return of being in state s and taking some action a
State -> (PLAYER_SUM, DEALER_SHOWING, ACE)
Action Space -> (0, 1) 0 = stick, 1 = hit

Appent the state cases as they come (to zero)
if the key doesn't exist, create it -> initialize to zero

q = {
    (player_sum, dealer_showing, ace): {0: value, 1: value}
    (17, 10, False): {0: 0.8, 0.6}
}

returns = {
    (player_sum, dealer_showing): (action, reward)
}


Improvements:
- Need to change the data structure for counting, its a poor system – not scalable
- Add discounting
- Refactor
'''

class MonteCarloAgent:
    def __init__(self):
        self.q = {}
        self._returns = {}
        self._initialize_q()

    '''
    Initialize the value function Q(S,A) to zero everywhere, and create a counting variable for each state to update the learning rate.
    '''
    def _initialize_q(self):
        for d in range(1,11):
            for p in range(-10,32):
                self.q[(d,p)] = {
                    "count": 0,
                    "value": {0: [0.0, 0], 1: [0.0, 0]}
                }
    
    '''
    Store returns from episodes, along with the corresponding actions and states, increment counters for states and state-action pairs
    '''
    def log_return(self, state, action, reward):
        if not self._returns.get(state):
            self._returns[state] = (action, reward)
            self.q[state]["count"] += 1
            self.q[state]["value"][action][1] += 1

    '''
    Update value function in the direction of the obtianed reward
    '''
    def update_value(self):
        for state in self._returns.keys():
            action = self._returns[state][0]
            alpha = 1 / self.q[state]["value"][action][1]
            self.q[state]["value"][action][0] += alpha*(self._returns[state][1] - self.q[state]["value"][action][0]) # do this for both actions?

    '''
    Select the action with the largest Q value with 1-e probability, otherwise act randomly with probability e.
    '''
    def policy(self, state) -> int:
        max_value = -999999999
        for a in self.q[state]["value"]:
            if self.q[state]["value"][a][0] >= max_value:
                action = a
                max_value = self.q[state]["value"][a][0]

        e = 100 / (100 + self.q[state]["count"])
        if e >= random.random():
            actions = [0, 1]
            action = random.choice(actions)
        
        return action

    def reset_returns(self):
        self._returns = {}




e = Easy21()
mc = MonteCarloAgent()
total_reward = [0]
reward_log = [0]

'''
Run for 50000 iterations
'''
N = 2000000 # num of episodes
for i in range(1,N):
    e.reset()
    state = e.get_state()
    print("Evaluating episode {}...".format(i))
    while not e.is_terminated():
        prev_state = state
        print(mc.q[state])
        action = mc.policy(state)
        state, reward = e.step(state, action)
        mc.log_return(prev_state, action, reward)
        print("Prev_State: {}\nAction: {}\nNew_State: {}\nReward: {}".format(prev_state, action, state, reward))
    print("Dealer Score: {}\nPlayer Score: {}".format(e.get_dealer_score(), e.get_player1_score()))
    total_reward.append(total_reward[i-1] + reward)
    reward_log.append(reward)
    mc.update_value()
    mc.reset_returns()



'''
Graphing
'''

for d in range(1, 11):
    row = []
    row1 = []
    row2 = []
    for p in range(1, 22):
        state = (d,p)
        if mc.q[state]["value"][0][0] > mc.q[state]["value"][1][0]:
            row.append(mc.q[state]["value"][0][0])
        else:
            row.append(mc.q[state]["value"][1][0])
        
        row1.append(mc.q[state]["value"][0][0])
        row2.append(mc.q[state]["value"][1][0])
    # row = np.array([row])

    if d == 1:
        value = row
        hit_value = row2
        stick_value = row1
    else:
        value = np.vstack((value,row))
        hit_value = np.vstack((hit_value, row2))
        stick_value = np.vstack((stick_value, row1))


# plt.plot(range(0,N), total_reward)
# plt.title("Total Cumulative Reward")
# plt.ylabel("Total Reward")
# plt.xlabel("Timestep")
# plt.show()

dealer_cards = np.arange(1,11)
player_total = np.arange(1,22)

X, Y = np.meshgrid(dealer_cards, player_total) # no idea why to do that

fig = plt.figure()
q = fig.add_subplot(1,3,1, projection ='3d')

# syntax for plotting
q.plot_surface(X, Y, np.transpose(value), cmap='viridis')
q.set_title('Optimal State-Action Value Function Q(s,a)')

h = fig.add_subplot(1,3,2,projection = '3d')
h.plot_surface(X, Y, np.transpose(hit_value), cmap='viridis')
h.set_title('State-Hit Value Function Q(s,a)')

s = fig.add_subplot(1,3,3,projection = '3d')
s.plot_surface(X, Y, np.transpose(stick_value), cmap='viridis', ccount=100, rcount=100)
s.set_title('State-Stick Value Function Q(s,a)')

plt.show()


