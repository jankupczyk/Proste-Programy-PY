# Prosta tabliczka mnożenia
import random
wynik = 0
for i in range(10):

    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print("a=", a, ", b=", b)
    print(f"Runda {i}")
    sprawdzenie = int(input("Podaj wynik: "))
    if (a*b == sprawdzenie):
        print("Brawo podałeś dobry wynik!")
        wynik += 1
    else:
        print("Poprawny wynik to: ", a*b)
        print("Musisz jeszcze poćwiczyć!")

if wynik < 4:
    ocena = "NDST"
elif wynik == 4:
    ocena = "DOP"
elif wynik <= 6:
    ocena = "DST"
elif wynik <= 8:
    ocena = "DB"
elif wynik == 9:
    ocena = "BDB"
else:
    ocena = "CEL"
print(f"Koniec, twój wynik to: {wynik} na 10 punktów. Twoja ocena to {ocena}")
