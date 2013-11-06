from visual import sphere, rate
from math import cos, sin, pi
from numpy import linspace

s = sphere(pos=[1, 0, 0], radius=0.1)

for t in linspace(0, 10 * pi, 1000):
    rate(100)
    x = 2*cos(t)
    y = sin(t)
    s.pos = [x, y, 0]
