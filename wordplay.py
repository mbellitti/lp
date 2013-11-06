fin = open('/home/ksarnek/codice/python/wordsEn.dat')


def has_no_e(str):
    for letter in str:
        if letter == "e":
            return False
    return True


def avoids(str, forbidden):
    for letter in str:
        if letter in forbidden:
            return False
    return True


def uses_only(word, allowed):
    for letter in word:
        if letter not in allowed:
            return False
    return True


def triple_double(word):
    if len(word) < 6:
        print("Word too short")
    else:
        for i in range(len(word)-5):
            if word[i] == word[i+1] and word[i+2] == word[i+3] and word[i+4] == word[i+5]:
                return True
    return False


def in_fin(of, word):
    for line in of:
        par = line.strip()
        if par == word:
            return True
    return False

#we = 0
#woe = 0
#for line in fin:
#    word = line.strip()
#    we += 1
#    if has_no_e(word):
#        woe += 1
#        #print(word)


