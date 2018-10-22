# -*- coding: utf-8 -*-
"""
Make a function that creates a list of the first n fibonacci numbers for n >=2.
Then print the first 10 fibonacci numbers.

The fibonacci numbers are defined by the equation f_n = f_(n-1) + f_(n-2).
"""


def fibonacci_list(n):
    fib_list = [0, 1]
    for i in range(n-2):
        fib_list.append(fib_list[-1]+fib_list[-2])
    return fib_list

print(fibonacci_list(10))
