# Gra matematyczna gdzie 2 graczy podaje liczbę
liczba1 = int(input("Gracz 1 podaje liczbę -->"))
liczba2 = int(input("Gracz 2 podaje liczbę -->"))
print("___________________")
print("Gracz 1 podał %d "     ' |' % liczba1)
print("Gracz 2 podał %d "     ' |' % liczba2)
if (liczba1 >= 1000 or liczba2 >= 1000):
    print("Ktoś z graczy podał złą liczbę!")
else:
    suma1 = 0
    suma2 = 0
    for i in range(1, liczba1):
        if liczba1 % i == 0:
            suma1 += i
           # print(i)
    for i in range(1, liczba2):
        if liczba2 % i == 0:
            suma2 += i
            # print(i)
    print(suma1)
    print(suma2)
    if (suma1 > suma2):
        print("Wygrał gracz nr. 1")
    else:
        print("Wygrał gracz nr. 2")
