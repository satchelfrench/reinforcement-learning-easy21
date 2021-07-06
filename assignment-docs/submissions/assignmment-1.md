# Assignment 1

## Objective
For this first assignment the core objective was to create the game environment for which we will be running our agents in for the remainder of the course.
The game Easy21 is similar but not identical to the popular card game "Black Jack", and the exact rules for it may be found [here](https://www.davidsilver.uk/wp-content/uploads/2020/03/Easy21-Johannes.pdf).

For this assignment there are two key files:
- environment.py
- test_env.py

Environment.py implements the game easy21 as a stateful object which tracks the ```Player``` objects, current state, and termination check of the game. The function ```draw_new_card()``` selects a card from 1-10 with uniform distrubution, and makes it a red card with 1/3 probability, and black otherwise. As red cards subtract from the score, they are denoted with a negative.

The ```step()``` function is the most important, it implements most of the game logic and determines if the dealer, or player has won. It accepts three arguments, the first two represent the state as the dealer's first card and the players current score, the third is the action to *"hit"* or *"stick"* (partially observable process). The step function returns the new updated state based on the action, and a reward calculated according to the environment rules.

## How to Use
The game is really only designed for computers to play, and offers no user interface. For an agent to play the game, it is expected that the initial state is grabbed by calling ```get_state()``` after initialization. This value should be stored and then only the step function should be called. Any further use of this function in the game will give the real state, which is not desired.

Action is described as a boolean of **True** or **False** for whether the agent wishes to hit or not. If True, the environment will simulate a hit, if False it will simulate a stick.

**Example usage**
```python

e = Easy21() # create game object
init_state = e.get_state() # grab initial state

#######################################################
# Implement RL techniques for action prediction here. #
#######################################################

N = 1000 # number of training iterations
for i in range(N):
    while not e.terminated:
        state, reward = e.step(init_state, action) 

    ## RECORD DATA IF NEEDED
    e.reset() # Reset Environment


```

## Testing

As there is non human interface, this game must be tested to ensure functionality. See the ```/tests/test_env.py``` folder for specific environment testing.!

To verify everything is running as expected:

```sh
git clone https://github.com/satchelfrench/reinforcement-learning-easy21
cd reiforcement-learning-easy21
python test/test_env.py
```