from numpy import loadtxt
from pylab import imshow, show, colorbar

data = loadtxt("stm.txt")

imshow(data)
colorbar()
show()
