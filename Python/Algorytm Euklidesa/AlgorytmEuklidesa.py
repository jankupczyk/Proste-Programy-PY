# Algorytm Euklidesa |Rekurencja|
def NWD(a, b):
    c = 0
    while b != 0:
        c = a % b
        print("a = {a}; b = {b}".format(a=a, b=b))
        a, b = b, c
    print("a = {a}; b = {b}".format(a=a, b=b))
    return a


def classicNWD(a, b):
    while a != b:
        a, b = max(a, b), min(a, b)
        print("a = {a}; b = {b}".format(a=a, b=b))
        a = a - b
    print("a = {a}; b = {b}".format(a=a, b=b))
    return a


def main(args):
    a = int(input("Podaj pierwszą liczbę całkowitą dodatnią: "))
    b = int(input("Podaj drugą liczbę całkowitą dodatnią: "))
    print("Metoda z wydajniejsza: n")
    print("nNajwiększy wspólny dzielnik liczb {a} i {b} jest równy: {NWD}".format(
        a=a, b=b, NWD=NWD(a, b)))
    print("nObliczanie NWD metodą klasyczną:n")
    print("nNajwiększy wspólny dzielnik liczb {a} i {b} jest równy: {NWD}".format(
        a=a, b=b, NWD=classicNWD(a, b)))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
