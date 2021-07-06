# Monte-Carlo Control in Easy21

Apply Monte-Carlo control to Easy21. Initialise the value function to zero. Use a time-varying scalar step-size of _α<sub>t</sub> = 1/N(s<sub>t</sub>_, a<sub>t</sub>) and an 𝜖-greedy exploration strategy with _𝜖<sub>t</sub> = N<sub>0</sub>/(N<sub>0</sub> + N(s<sub>t</sub>))_, where N<sub>0</sub> = 100 is a constant, _N(s)_ is the number of times that state s has been visited, and _N(s, a)_ is the number of times that action _a_ has been selected from state _s_. Feel free to choose an alternative value for _N<sub>0</sub>_, if it helps producing better results. Plot the optimal value function _V<sub>*</sub>(s) = max<sub>a</sub> Q<sub>*</sub>(s, a)_ using similar axes to the following figure taken from Sutton and Barto’s Blackjack example.

<img src="./images/axis.png" alt="axis for optimal value funciton" width="200"/>
