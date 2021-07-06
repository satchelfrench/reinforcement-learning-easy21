# TD Learning in Easy 21

**Due Date:** July 21 <br />
**Weight:** 15 Marks

Implement _Sarsa(λ)_ in 21s. Initialise the value function to zero. Use the same step-size and exploration schedules as in the previous section. Run the algorithm with parameter values _λ ∈ {0, 0.1, 0.2, ..., 1}_. Stop each run after 1000 episodes and report the mean-squared error _Σ<sub>s,a</sub> (Q(s, a) − Q<sup>*</sup>(s, a))<sup>2</sup>_ over all states _s_ and actions _a_, comparing the true values _Q<sub>*</sub>(s, a)_ computed in the previous section with the estimated values _Q(s, a)_ computed by Sarsa. Plot the meansquared error against λ. For λ = 0 and λ = 1 only, plot the learning curve of mean-squared error against episode number.
