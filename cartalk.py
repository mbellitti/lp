def times(agemom):
    ageson = 0
    count = 0
    while agemom-1 < 200:
        ageson += 1
        agemom += 1
        if agemom > 99:
            am = str(agemom)
            ason = str(ageson).zfill(3)
        else:
            am = str(agemom)
            ason = str(ageson)
        if am == ason[::-1]:
            print(agemom, ageson)
            count += 1
    return count


def age_guy(num):
    for agemom in xrange(200):
        if times(agemom) == num and agemom > 12:
            return agemom

