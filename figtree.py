from numpy import arange
from pylab import plot, show
from itertools import groupby

rp = []
xp = []

for r in arange(0, 4, 0.001):
    x = 0.5
    for i in range(1000):
        x = r * x * (1 - x)
    xp.append(x)
    rp.append(r)
    for i in range(100):
        t = r*xp[-1]*(1 - xp[-1])
        xp.append(t)
        rp.append(r)

plot(rp, xp, "k.")
show()
