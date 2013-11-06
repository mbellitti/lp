def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def print_hist(d):
    for c in sorted(d.keys()):
        print(c, d[c])


def inv_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def has_duplicates(l):
    h = histogram(l)
    for elem in h:
        if h[elem] > 1:
            return True
    return False


def has_duplicates2(t):
    return len(set(t)) < len(t)
