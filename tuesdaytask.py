#!/usr/bin/python3


import numpy as np
from scipy.optimize import curve_fit, minimize, dual_annealing
from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt

# The ODE systems
def pendulum(t,x,g,length):
    """x is the state consisting of [postion, x1]"""
    return [x[1] ,(-g/length)*np.sin(x[0])]

def pendulum_simplified(t,x,g,length):
    """x is the state consisting of [postion, x1]"""
    return [x[1] ,(-g/length)*x[0]]



def period_time_full(sol_full, sol_full_time):
    points= [] 
    indexes = []
    for i in range(len(sol_full)):
        if i+2 > len(sol_full):
            break
        if sol_full[i] < 0 and sol_full[i+1] >= 0 or sol_full[i] <= 0 and sol_full[i+1] > 0:
            points.append(sol_full[i])
            indexes.append(i)
            
        if len(points) >= 2:
            break
    start_time = sol_full_time[indexes[0]]
    end_time = sol_full_time[indexes[1]]
    total_time = end_time - start_time
    return total_time

def period_time_simpl(sol_simpl, sol_simpl_time):
    points= []
    indexes = []
    for i in range(len(sol_simpl)):
        if i+2 > len(sol_simpl):
            break
        if sol_simpl[i] < 0 and sol_simpl[i+1] >= 0 or sol_simpl[i] <= 0 and sol_simpl[i+1] > 0:
            points.append(sol_simpl[i])
            indexes.append(i)

        if len(points) >= 2:
            break
    start_time = sol_simpl_time[indexes[0]]
    end_time = sol_simpl_time[indexes[1]]
    total_time = end_time - start_time
    return total_time


t_vec =np.linspace(0,5,100)

# If the starting angle is small, we don't care about the difference in the models, not significant
starting_angle = 0.75
length = 1 # pendulum length

def solver(ode_sys, g):
    """Solve the ODE system for different g and length values"""
    return solve_ivp(ode_sys, [0,5], [starting_angle,0], args=(g,length), t_eval=t_vec)

# Get the different solutions for the full and simplified version
sol_simpl = solver(pendulum_simplified, 9.81)
sol_full = solver(pendulum, 9.81)

print("The period of the oscillation from the full equation is: ", period_time_full(sol_full.y[0,:], sol_full.t), "seconds.")

print("The period of the oscillation from the simple equation is: ", period_time_simpl(sol_simpl.y[0,:], sol_simpl.t), "seconds.")


#Plotting, create a 'figure' and an 'axes' within it
fig, ax = plt.subplots()
# Add two lines to the axes
ax.plot(t_vec, sol_simpl.y[0,:], label='Simplified')
ax.plot(t_vec, sol_full.y[0,:], label='Full')
ax.set_xlabel('Time [s]')
ax.set_ylabel('Swing angle $\Theta$')
ax.legend()
plt.show()
