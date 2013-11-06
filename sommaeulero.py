from numpy import pi

s = 0

for n in range(1, 100000001):
    s += 1 / n ** 2

res = pi ** 2 / 6 - s

print(res)
