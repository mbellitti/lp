def freq(R1, R2, R, C):
    """calcola la frequenza di un oscillatore a rilassamento"""
    from math import log
    T = 2.0 * R * C * log(1 + 2*R1/R2)
    f = 1/T
    return f

def erfreq(R1, R2, R, C, dR1, dR2, dR, dC):
    """ Calcola frequenza ed errore di un oscillatore a rilassamento,
    usando lo schema nelle slide di Hueller
    """
    from math import log
    A = 4.0*R*C/(1 + 2*R1/R2)
    B = 2.0 * log(1 + 2*R1/R2)
    T = 2.0 * R * C * log(1 + 2*R1/R2)
    dT = A*dR1 + A*R1*dR2/R2**2 + C*B*dR + R*B*dC
    f = 1/T
    df = dT/T**2
    return f, df
