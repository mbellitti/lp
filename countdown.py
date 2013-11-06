

def countdown(sec):
    """counts down to 0, at which it blasts off"""
    if sec <= 0:
        print("Blastoff!")
    else:
        print(sec)
        countdown(sec - 1)


def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**2 == c**2:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("Nope, that doesn't work")
