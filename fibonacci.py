def fibl(n):
    """fornisce i numeri di Fibonacci minori di n in una lista"""
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result
