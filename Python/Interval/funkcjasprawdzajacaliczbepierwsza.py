# Funkcja sprawdzająca, czy x jest liczbą pierwszą
def pierwsza(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


for n in range(10, 100):
    liczba = str(n)
    suma = int(liczba[0])+int(liczba[-1])
    if pierwsza(suma) == True:
        print(f"{n} (suma={suma})")
    else:
        continue
