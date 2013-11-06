from numpy import ones, savetxt
from pylab import imshow, show, colorbar, gray, xlabel, ylabel, autumn, bone, cool, copper, flag, hsv, jet, pink, prism, spring, summer, winter

N = 10000 # lato della matrice di punti
ITER = 200 # iterazioni della mappa, dovrebbe essere \infty
xmin = -5#-1.6  # -1.5
xmax = 5 #-1.36 # 0.55
ymin = -5 #-0.10 #-1.0
ymax = 5 #0.10 # 1.0

M = ones([N, N], float) # parte con colore uniforme

for k in xrange(N):
    print "Running map on column", k, "of", N, "Re(x)=", xmin+(xmax-xmin)*k/N
    for l in xrange(N):
        z = 0
        for i in xrange(ITER):
            z = z*z + complex(xmin+(xmax-xmin)*k/N, ymin+(ymax-ymin)*l/N)
            if abs(z) > 2:
                M[k, l] = float(i)/ITER # quanto sto in mandel?
                #M[k, l] = 0 # Modo Manicheo
                break

#savetxt("Man_mat.dat", M, delimiter = ' ', newline = "\n")
imshow(zip(*M), extent=[xmin, xmax, ymin, ymax]) # density map di M
xlabel("Re(c)")
ylabel("Im(c)")
pink()
colorbar()
show()
