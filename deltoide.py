from math import sin, cos, pi
from numpy import linspace
from pylab import plot, show

x = []
y = []

for i in linspace(0, 2*pi, 100):
    x.append(2*cos(i) + cos(2*i))
    y.append(2*sin(i) - sin(2*i))

plot(x,y)

show()
