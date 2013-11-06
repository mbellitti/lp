from cmath import sqrt
from scipy.constants import hbar

m = 9.11e-31

E = float(input("Initial energy in eV:"))

V = float(input("Barrier height in eV:"))

k1 = sqrt(2*m*E)/hbar
k2 = sqrt(2*m*(E-V))/hbar

T = (4*k1*k2)/(k1+k2)**2
R = ((k1-k2)/(k1+k2))**2

print("Reflection coefficient is: ", R)
print("Transmission coefficient is:", T)
