# -*- coding: utf-8 -*-
"""
Write a function that solves a first order differential equation using Euler's
method.

Plot the solution to the linear ode dx_dt = -2x with x_0=10 for t=0 to t=4 with
100 steps .
"""

import matplotlib.pyplot as plt


def eulers_method(dx_dt, x0, t0, tf, n_steps):
    t = [t0]
    x = [x0]
    delta_t = (tf - t0)/n_steps
    for i in range(1, n_steps+1):
        t.append(t[-1]+delta_t)
        x.append(x[-1]+dx_dt(x[-1])*delta_t)
    return t, x


def f(x):
    return -2*x

plt.plot(*eulers_method(f, 10, 0, 4, 100))
