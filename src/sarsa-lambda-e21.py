import os
import sys
import pickle
import numpy as np

root_dir = os.path.dirname(__file__ )
src_dir = os.path.join(root_dir, '..')
sys.path.append(src_dir)

from src.environment import Easy21
from src.agents.TDSarsa import TDSarsaAgent
from src.utils.visualize import visualize
import matplotlib.pyplot as plt

from collections import OrderedDict

class Easy21TDSarsa(TDSarsaAgent):
    def _init_q(self):
        q = OrderedDict()
        for d in range(1,11):
            for p in range(1,22):
                q[(d,p)] = {
                    0: 0,
                    1: 0
                }
        return q


# Return the MSE for each state, action pair
def mse(Q1, Q2):
    e = 0
    c = 0
    for s in Q1:
        for a in Q1[s]:
            e += (Q1[s][a] - Q2[s][a])**2
            c +=1

    return e/c

if __name__ == "__main__":

    with open('MC_Q.pkl', 'rb') as in_file:
        Q = pickle.load(in_file) # load in Q function from monte carlo

    mse_errors = []

    # for lmbda in np.arange(0,1.1,0.1):
    lmbda = 1
        
    errors = []

    print("Running with Lambda = {}".format(lmbda))

    e = Easy21()
    agent = Easy21TDSarsa(gamma=1,lambda_=lmbda)
    cum_reward = [0]

    ''' 
    TRAINING LOOOP
    '''

    N = 70000 # num of episodes
    for i in range(1,N):
        e.reset()
        agent.reset_e()
        state = e.get_state()
        action = agent.policy(state)
        r = 0
        # print("Evaluating episode {}...".format(i))
        while not e.is_terminated():
            prev_state = state
            state, reward = e.step(state, action)
            prev_action = action
            action = agent.policy(state) if not e.is_terminated() else 2 # If S' is a terminal state
            r += reward
            agent.log_return(prev_state, prev_action, reward, state, action)
            agent.update_value()
            agent.reset_returns()
            # print("Prev_State: {}\nAction: {}\nNew_State: {}\nReward: {}".format(prev_state, action, state, reward))
        # print("Dealer Score: {}\nPlayer Score: {}".format(e.get_dealer_score(), e.get_player1_score()))
        cum_reward.append(cum_reward[i-1] + r)
        errors.append(mse(Q, agent.q))

    mse_errors.append(errors)

    # print(len(mse_errors))
    '''
    Visualize Agent Performance
    '''
    
    X = range(1,N)
    l = np.arange(0, 1.1, 0.1)
    for idx, curve in enumerate(mse_errors):
        label = "λ=" + str(l[idx])
        plt.plot(X, curve, label=label)
    
    plt.legend(loc="upper right")
    plt.xlabel("# of episodes")
    plt.ylabel("MSE")
    plt.title("Mean Squared Error for Sarsa(λ)")
    plt.show()    

    visualize(agent, cum_reward, N)