from numpy import loadtxt, shape
a = loadtxt("G1.dat")
mean = sum(a[0:, 0]**2)/shape(a)[0]
print("average in G1 is: ", mean)
