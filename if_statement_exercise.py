# -*- coding: utf-8 -*-
"""
Complete this script so that it prints the numbers 1-100, except if a number is
divisible by 9 it instead prints "lucky 9's", and if a number divisible by 3
but not 9 it prints 'triples'.

In Python you can find the remainder of a division with the % operator. For
example, 4 % 2 equals 0 and 5 % 2 equals 1.
"""

for i in range(1, 101):
    if i % 9 == 0:
        print("lucky 9's")
    elif i % 3 == 0:
        print("triples")
    else:
        print(i)
