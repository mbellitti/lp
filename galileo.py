from numpy import linspace, pi
from pylab import plot, show
from math import sin, cos

x = []
y = []

for t in linspace(0, 2*pi, 100):
    r = t**2
    x.append(r*cos(t))
    y.append(r*sin(t))

plot(x, y, "r-")
show()
