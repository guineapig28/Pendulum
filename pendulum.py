#!/usr/bin/python3
import pdb
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

def exponential_decay(t, y):
    return -0.5 * y


#Histogram

np.random.seed(42)
x = np.random.normal(size=1000)

plt.hist(x, density=True, bins=30)
plt.ylabel("Probablity")
plt.xlabel("Data"); 

plt.show()

#SciPy
t_evek = np.arange(0,10,0.1)
sol = solve_ivp(exponential_decay, [0, 10], [2], t_eval = t_evek)

plt.plot(t_evek, sol.y[0,:] )
print(sol.t)
print(sol.y)

plt.show()
