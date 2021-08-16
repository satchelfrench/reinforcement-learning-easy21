import random
import numpy as np
from collections import OrderedDict

'''
This is a generic montecarlo agent, it makes no assumptions about state or action space _init_q() must be implemented for the application for the agent to work

This will intialize the q-values for all possible states that may be encountered before learning, it must be implemented prior to running. 
The function must return an OrderedDict witht the following structure: 
* After Python 3.7 a regular dict() may be used as well *

def _init_q(self):
    q = OrderedDict({
        state: {
            some_action: some_initial_value,
            some_other_action: some_initial_value
        }
        another_state: {...}
    })

    return q

'''
class MonteCarloAgent:
    def __init__(self):
        self.q = self._init_q()
        self._state_count = self._init_state_count()
        self._returns = {}

    def _init_q(self) -> OrderedDict:
        raise NotImplementedError

    
    def _init_state_count(self):
        '''Creates a counting dictionary for all state, action pairs in Q'''
        state_count = {}
        for state in self.q:
            state_count[state] = {}
            for action in self.q[state]:
                state_count[state][action] = 0
        
        return state_count

    
    def log_return(self, state, action, reward):
        '''Stores returns from episodes, along with the corresponding actions and states, increment counters for states and state-action pairs'''
        if state not in self._returns:
            self._returns[state] = (action, reward)
        self._state_count[state][action] += 1 # Come up with default
   

    
    def get_state_count(self, state):
        '''Returns the total count for a state across all actions. '''
        count = 0
        for action in self._state_count[state]:
            count += self._state_count[state][action]
        return count

    
    def update_value(self):
        '''Updates value function in the direction of the obtianed reward '''
        for state in self._returns:
            action = self._returns[state][0]
            alpha = 1 / self._state_count[state][action]
            self.q[state][action] += alpha*(self._returns[state][1] - self.q[state][action]) # do this for both actions?


    def policy(self, state, greedy=False) -> int:
        '''Returns the action with the largest Q value with 1-e probability, otherwise act randomly with probability e.'''

        max_value = float('-inf')
        for a in self.q[state]:
            if self.q[state][a] >= max_value:
                action = a
                max_value = self.q[state][a]

        if not greedy:
            e = 100 / (100 + self.get_state_count(state))
            if e >= random.random():
                actions = [0, 1]
                action = random.choice(actions)
        
        return action

    def reset_returns(self):
        self._returns = {}

    
    def get_optimal_value(self):
        '''Returns the optimal value function as a 1-D numpy array, typically for graphing.'''
        value = np.array([])
        for state in self.q.keys():
            value = np.append(value, max(list(self.q[state].values())))
        
        return value

    def get_action_value(self, action):
        '''
        Input: An Action number
        Returns: The corresponding value function of that action in each state, as a 1-D numpy array, typically for graphing.
        '''
        value = np.array([])
        for state in self.q.keys():
            value = np.append(value, self.q[state][action])
        
        return value

    def get_policy_map(self):
        '''Returns the policy (all actions) for all states in Q as a 1-D Numpy array, typically for graphing.'''
        policy = np.array([])
        for state in self.q.keys():
            policy = np.append(policy, self.policy(state, greedy=True)) 
        
        return policy


