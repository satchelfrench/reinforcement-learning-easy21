import random
import numpy as np
from collections import OrderedDict

'''SARSA Lambda Agent'''
''' Functional but requires refactor '''

class TDSarsaAgent:
    def __init__(self, gamma=1, lambda_=1):
        self.q = self._init_q()
        self._state_count = self._init_state_count()
        self._returns = {}
        self.e = self._init_state_count() # should be corrected so there are separated initalizations for q and e, only works for uniform 0 initializations
        self.GAMMA = gamma
        self.LAMBDA = lambda_

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

    
    def log_return(self, state, action, reward, state2, action2):
        '''Stores returns from episodes, along with the corresponding actions and states, increment counters for states and state-action pairs'''
        if state not in self._returns:
            self._returns[state] = (action, reward, state2, action2)
        self._state_count[state][action] += 1 # Count state occurence
        self.e[state][action] += 1 # Increment eligibility trace
   

    def get_state_count(self, state):
        '''Returns the total count for a state across all actions. '''
        count = 0
        for action in self._state_count[state]:
            count += self._state_count[state][action]
        return count

    
    def update_value(self):
        '''Updates value function in the direction of the obtianed reward '''
        for state, episode in self._returns.items():
            action, r, state2, action2 = episode
            alpha = 1 / self._state_count[state][action]

            # Deal with terminal state S' / Needs refactor
            try:
                delta = r + self.GAMMA*self.q[state2][action2] - self.q[state][action]
            except KeyError:
                delta = r - self.q[state][action]
            
            self.q[state][action] = self.q[state][action] + alpha*delta*self.e[state][action]

        for state in self.e:
            for action in self.e[state]:
                self.e[state][action] *= self.GAMMA*self.LAMBDA


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

    def reset_e(self):
        self.e = self._init_state_count()
    
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


