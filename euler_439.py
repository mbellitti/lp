def d(k):
    x = 0
    for i in range(1, k + 1):
        if k % i == 0:
            x = x + i
    return x


def S(N):
    x = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            x = x + d(i * j)
    return x
