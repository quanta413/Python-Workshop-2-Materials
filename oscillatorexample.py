# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 21:55:49 2018

@author: Nicholas Sherer
"""

def small_drag_force(x, v):
    return -.1*v

def small_spring_force(x, v):
    return -.1*x


def integrate_by_dt(x0, v0, acceleration, dt):
    x1 = x0 + v0*dt + 1/2*acceleration*dt**2
    v1 = v0 + acceleration*dt
    return x1, v1


def integrate_Newtons_equations(x0, v0, mass, force, t0, tf, N):
    x_list = [x0]
    v_list = [v0]
    t_list = [t0]
    x_current = x0
    v_current = v0
    t_current = t0
    dt = (tf-t0)/N
    for i in range(N):
        acceleration = force(x_current, v_current) / mass
        x_current, v_current = integrate_by_dt(x_current, v_current,
                                               acceleration, dt)
        t_current = t_current + dt
        x_list.append(x_current)
        v_list.append(v_current)
        t_list.append(t_current)
    return x_list, v_list, t_list
    