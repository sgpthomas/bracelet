#!/usr/bin/env python3

# import itertools
# from collections import Counter
from math import floor
import numpy as np

def sym_mod(n, p):
    """Calculate a symmetric modulus of a number given an integer and a base."""
    L = floor(n / 2)
    p %= n
    if p <= L:
        return p
    else:
        return n - p

def distance(bracelet, a, b):
    """Calculate the distance between 'a' and 'b' in a bracelet.
    (a and b are not indices but values.)"""
    n = len(bracelet)
    ai = bracelet.index(a)
    bi = bracelet.index(b)

    if ai == bi:
        return 0
    else:
        return sym_mod(n, sym_mod(n, ai) + sym_mod(n, bi))

def distance_matrix(bracelet):
    """Calculate the distance matrix of a bracelet"""
    n = len(bracelet)

    matrix = np.zeros((n,n)) # initalize a matrix of size n x n
    for i in range(n):
        for j in range(n):
            matrix[i][j] = distance(bracelet, i, j)
    return matrix

try:
    while True:
        pre = input("Enter a bracelet: ")
        bracelet = [int(x) for x in pre.split()]

        M = distance_matrix(bracelet)
        print(M)

        det = round(np.linalg.det(M), 5)
        print("Det: {}".format(det))
except EOFError:
    print("Exiting")
except KeyboardInterrupt:
    print("Exiting")
