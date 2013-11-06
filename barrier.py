# This script calculates reflection and trasmission coefficient for a
# particle hitting a step potential barrier in x=0

from cmath import sqrt
from scipy.constants import hbar

# la particella ha la massa di un elettrone
m = 0.511e6

E = float(input("Initial energy in eV: "))

V = float(input("Barrier height in eV: "))

# sqrt is the cmat version, so under-barrier passage case is included
k1 = sqrt(2 * m * E) / hbar
k2 = sqrt(2 * m * (E - V)) / hbar

T = ((abs(2 * k1 / (k1 + k2))) ** 2) * (k2.real / k1.real)
R = ((abs((k1 - k2) / (k1 + k2))) ** 2)

print("R = ", R)
print("T = ", T)
