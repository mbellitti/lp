

def palindromo(s):
    for i in range(0, len(str(s))//2):
        if str(s)[i] != str(s)[-i-1]:
            pal = 0
            break
        else:
            pal = 1
    return pal

x = 0

for m in range(999, 99, -1):
    print("m is: ", m)
    for n in range(m, 99, -1):
        print("n is: ", n)
        if palindromo(str(m*n)) and x < m*n:
            x = m*n
    print("x is: ", x)

print("Biggest palindrome is: ", x)
