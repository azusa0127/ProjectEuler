import sympy.ntheory

patterns = []
patterns[0] = [1, 0, 0, 0, 2]
patterns[1] = [0, 1, 0, 0, 2]
patterns[2] = [0, 0, 1, 0, 2]
patterns[3] = [0, 0, 0, 1, 2]


def getNumber(pt, i, j, k):
    n = ""
    for p in pt:
        if p == 1:
            n += str(i)
        elif p == 0:
            n += str(k)
        elif p == 2:
            n += str(j)
    return int(n)


def main():
    for i in range(10):
        for j in [1, 3, 7, 9]:
            if (i + j) % 3:
                for pt in patterns:
                    c = 0
                    cd = 3
                    for k in range(10):
                        if sympy.ntheory.isprime(getNumber(pt, i, j, k)):
                            c += 1
                            if c >= 8:
                                print(getNumber(pt, i, j, k))
                        else:
                            cd -= 1
                            if cd == 0:
                                break

main()