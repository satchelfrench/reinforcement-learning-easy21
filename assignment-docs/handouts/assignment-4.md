# Linear Function Approximation

**Due Date**: August 4th <br />
**Weight**: 15 Marks

**This assignment may be considered a bonus or replaceable**

We now consider a simple value function approximator using coarse coding. Use a binary feature vector _φ(s, a) with 3 ∗ 6 ∗ 2 = 36_ features. Each binary feature
has a value of 1 iff _(s, a)_ lies within the cuboid of state-space corresponding to that feature, and the action corresponding to that feature. The cuboids have the following overlapping intervals:

- _dealer(s) = {[1, 4], [4, 7], [7, 10]}_
- _player(s) = {[1, 6], [4, 9], [7, 12], [10, 15], [13, 18], [16, 21]}_
- _a = {hit, stick}_

where
- dealer(s) is the value of the dealer’s first card (1–10)
- sum(s) is the sum of the player’s cards (1–21)

Repeat the _Sarsa(λ)_ experiment from the previous section, but using linear value function approximation _Q(s, a) = φ(s, a)<sup>T</sup>θ_. Use a constant exploration of _ε = 0.05_ and a constant step-size of 0.01. Plot the mean-squared error against _λ_. For _λ = 0_ and _λ = 1_ only, plot the learning curve of mean-squared error against episode number.
