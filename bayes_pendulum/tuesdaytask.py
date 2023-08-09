#!/usr/bin/python3


import numpy as np
from scipy.optimize import curve_fit, minimize, dual_annealing
from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt

# The ODE systems


def pendulum(t, x, g, length):
    """x is the state consisting of [postion, x1]"""
    return [x[1], (-g/length)*np.sin(x[0])]


def pendulum_simplified(t, x, g, length):
    """x is the state consisting of [postion, x1]"""
    return [x[1], (-g/length)*x[0]]


def locate_root(index, sol_time, sol, indexes):
    return (((sol_time[indexes[index]]+0.05)*sol[indexes[index]])-(sol_time[indexes[index]]*sol[indexes[index]+1]))/(sol[indexes[index]]-sol[indexes[index]+1])


def period_time(sol, sol_time):
    indexes = []
    for i in range(len(sol)):
        if i+2 > len(sol):
            break
        if sol[i] < 0 and sol[i+1] >= 0 or sol[i] <= 0 and sol[i+1] > 0:
            # if (sol_time[i+1]*sol[i]-sol_time[i]*sol[i+1])/(sol[i]-sol[i+1]) == 0:
            indexes.append(i)
    start_time = locate_root(0, sol_time, sol,  indexes)
    end_time = locate_root(1, sol_time, sol, indexes)
    total_time = end_time - start_time
    return total_time


def main():
    full_periods = []
    simpl_periods = []
    angle = []

    t_vec = np.linspace(0, 5, 0.05)

    for i in range(1, 90):
        # If the starting angle is small, we don't care about the difference in the models, not significant
        starting_angle = i/57.2958
        length = 1  # pendulum length

        def solver(ode_sys, g):
            """Solve the ODE system for different g and length values"""
            return solve_ivp(ode_sys, [0, 5], [starting_angle, 0], args=(g, length), t_eval=t_vec)

        # Get the different solutions for the full and simplified version
        sol_simpl = solver(pendulum_simplified, 9.81)
        sol_full = solver(pendulum, 9.81)

        full_periods.append(period_time(sol_full.y[0, :], sol_full.t))
        simpl_periods.append(period_time(sol_simpl.y[0, :], sol_simpl.t))
        angle.append(starting_angle)

    fig, ax = plt.subplots()
    ax.plot(angle, simpl_periods, label="Simplified")
    ax.plot(angle, full_periods, label="Full")
    ax.set_xlabel("Angle")
    ax.set_ylabel("Period")
    ax.legend()
    plt.show()

    # Plotting, create a 'figure' and an 'axes' within it
    #fig, ax = plt.subplots()
    # Add two lines to the axes
    #ax.plot(t_vec, sol_simpl.y[0,:], label='Simplified')
    #ax.plot(t_vec, sol_full.y[0,:], label='Full')
    #ax.set_xlabel('Time [s]')
    #ax.set_ylabel('Swing angle $\Theta$')
    # ax.legend()
    # plt.show()

# If you run the file from the command line then call the main function.
# If the module is imported for testing, then it means the main function
# won't be executed.


if __name__ == "__main__":
    main()
