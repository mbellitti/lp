from visual import sphere, color
L = 1
RNa = 0.3
RCl = 0.2

for i in range(-L, L + 1):
    for j in range(-L, L + 1):
        for k in range(-L, L + 1):
            if (i + j + k) % 2 == 0:
                sphere(pos=[i, j, k], radius=RCl, color=color.magenta)
            else:
                sphere(pos=[i, j, k], radius=RNa, color=color.green)
