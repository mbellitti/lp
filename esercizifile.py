def sed(pattern, replacement, source, dest):
    try:
        fin = open(source, "r")
        fout = open(dest, "w")

        for line in fin:
            line = line.replace(pattern, replacement)
            fout.write(line)

        fin.close()
        fout.close()

    except:
        print("There was some kind of error")


# corsi a scelta, apre il file e lo trasforma in array
from numpy import *

s = open("scelta.dat")

isto = []

# trasforma il file in una lista di liste, con le parole separate
for line in s:
    print(line)
    isto.append(line.strip().split(" "))


def list_to_num(t):
    res = []
    for elem in t:
        if type(elem) == list:
            res.append(list_to_num(elem))
        else:
            if elem.isdigit():
                res.append(int(elem))
    return res

# trasformo la cosa di prima in una matrice
# la prima colonna sono sicuri, la seconda in forse
scelta = array(list_to_num(isto[1:]))
