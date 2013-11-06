from math import pi,e,log,exp

G = 6.67e-11
M = 5.97e24
R = 6.371e6

T = float(input("Insert orbital period in sec:"))

h = (((G*M*(T**2))/(4*pi**2))**(1/3)) - R

print("The required altitude is:", h/1000, "km")
