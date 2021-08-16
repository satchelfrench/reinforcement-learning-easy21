'''
This is file is used to perform all graphing operations neccesarry to visualize the agents performance.
It is intended to be specific to this application of Easy21
TODO:
- [] Could become a class for visualization, pulling state directly from agent.
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from src.utils.graphing import create_line_plot, create_2d_heat_map


def visualize(agent, cum_reward, N):
    # ============================ GRAPHING ========================= #
    
    ''' Get Values '''

    value = agent.get_optimal_value()
    value = np.reshape(value, (10,21))

    hit_value = agent.get_action_value(1)
    hit_value = np.reshape(hit_value, (10,21))

    stick_value = agent.get_action_value(0)
    stick_value = np.reshape(stick_value, (10,21))

    e_actions = agent.get_policy_map()
    e_actions = np.reshape(e_actions, (10,21))
    

    '''
    Plot Cumulative Reward
    '''

    reward_fig, total_reward,  = create_line_plot(range(0,N), cum_reward,
                            "Timestep",
                            "Total Reward",
                            "Total Cumulative Reward")

    reward_fig.show()

    '''
    Plot Value functions:
    - Optimal Value Function: Q*(s,a)
    - Hit value function: H(s,a)
    - Stick value function: S(s,a)
    '''

    dealer_cards = np.arange(1,11)
    player_total = np.arange(1,22)

    X, Y = np.meshgrid(dealer_cards, player_total) # no idea why to do that

    value_fig, (q, h, s) = plt.subplots(1,3, subplot_kw=dict(projection ='3d'))
    value_fig.suptitle("Value Functions Q(s,a)")

    q.plot_surface(X, Y, np.transpose(value), cmap='viridis')
    q.set_title('Optimal State-Action Value Function Q(s,a)')
    q.set_xlabel('Dealer Card')
    q.set_ylabel('Player Total')
    q.set_zlabel('Value')
    

    h.plot_surface(X, Y, np.transpose(hit_value), cmap='viridis')
    h.set_title('State-Hit Value Function Q(s,a)')
    h.set_xlabel('Dealer Card')
    h.set_ylabel('Player Total')
    h.set_zlabel('Value')

    s.plot_surface(X, Y, np.transpose(stick_value), cmap='viridis', ccount=100, rcount=100)
    s.set_title('State-Stick Value Function Q(s,a)')
    s.set_xlabel('Dealer Card')
    s.set_ylabel('Player Total')
    s.set_zlabel('Value')

    value_fig.show()

    '''
    Plot Policy Map
    '''
    policy_fig, ax = create_2d_heat_map(np.transpose(e_actions), dealer_cards, player_total, {1: "H", 0: "S"}, "Policy Map", "Dealer Card Showing", "Player Total")
    policy_fig.show()

    plt.show()