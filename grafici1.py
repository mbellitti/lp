from pylab import plot, show, xlim, ylim, xlabel, ylabel
from math import sin, cos
from numpy import linspace

#y = loadtxt("G1.dat", float)
#plot(y[:,0], y[:,1])

xp = []
yp = []

for x in linspace(0, 10, 100):
    xp.append(x)
    yp.append(sin(x))

xlim(-1, 11)
xlabel("x axis")

ylim(-1.2, 1.2)
ylabel("y axis")

plot(xp, yp, "b+")
plot(xp, map(cos, xp))
show()
