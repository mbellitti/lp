from math import sqrt
from numpy import linspace


def integral(r, N):
    I = 0
    for x in linspace(-r, r, N):
        I += sqrt(1-x**2)*2*r/N
    return I
