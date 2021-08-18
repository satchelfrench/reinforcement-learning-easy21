import os
import sys
import pickle

root_dir = os.path.dirname(__file__ )
src_dir = os.path.join(root_dir, '..')
sys.path.append(src_dir)

from src.environment import Easy21
from src.agents.MonteCarlo import MonteCarloAgent
from src.utils.visualize import visualize

from collections import OrderedDict

class Easy21MonteCarlo(MonteCarloAgent):
    def _init_q(self):
        q = OrderedDict()
        for d in range(1,11):
            for p in range(1,22):
                q[(d,p)] = {
                    0: 0,
                    1: 0
                }
        return q


if __name__ == "__main__":
    e = Easy21()
    mc = Easy21MonteCarlo()
    cum_reward = [0]

    ''' 
    TRAINING LOOOP
    '''
    N = 70000 # num of episodes
    for i in range(1,N):
        e.reset()
        state = e.get_state()
        print("Evaluating episode {}...".format(i))
        while not e.is_terminated():
            prev_state = state
            action = mc.policy(state)
            state, reward = e.step(state, action)
            mc.log_return(prev_state, action, reward)
            mc.update_value()
            mc.reset_returns()
            print("Prev_State: {}\nAction: {}\nNew_State: {}\nReward: {}".format(prev_state, action, state, reward))
        print("Dealer Score: {}\nPlayer Score: {}".format(e.get_dealer_score(), e.get_player1_score()))
        cum_reward.append(cum_reward[i-1] + reward)

    with open('MC_Q.pkl', 'wb') as out_file:
        pickle.dump(mc.q, out_file)

    '''
    Visualize Agent Performance
    '''
    visualize(mc, cum_reward, N)