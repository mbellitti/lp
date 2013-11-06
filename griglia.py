def volte(funzione, num):
    """does funzione num times"""
    for x in range(num):
        funzione()


def orizz():
    """draws horizontal line"""
    print(("+ "+"- "*4)*2+"+")

def verticale():
    """draws vertical separators"""
    print(("| "+"  "*4)*2+"|")

orizz()
volte(verticale, 4)
orizz()
volte(verticale, 4)
orizz()
