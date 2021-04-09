# funkcja sprawdzająca, czy x jest liczbą pierwszą
def pierwsza(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


# użytkownik podaje liczbę tak długo dopóki nie poda dwóch liczb naturalnych
m, n = -1, -1
while m < 0 or n < 0:
    m = int(input("Podaj początek przedziału: "))
    n = int(input("Podaj koniec przedziału: "))
    if m < 0 or n < 0:
        print("Obie liczby muszą być liczbami naturalnymi!")
# zmienna przechowująca wszystkie liczby pierwsze z przedziału - początkowo pusta
pierwsze = ""
# początek jest mniejszy od końca (normala sytuacja)
if m <= n:
    for j in range(m, n+1):
        # jeśli j i j+2 są liczbami pierwszymi, wypisuje je jako parę liczb bliźniaczych
        if pierwsza(j) == True and pierwsza(j+2) == True:
            pierwsze += str(j)+", "+str(j+2)+" | "
        else:
            continue
# początek jest większy od końca -> sprawdzanie przedziału od drugiej strony
if m > n:
    for j in range(m, n-1, -1):
        # jeśli j i j-2 są liczbami pierwszymi, wypisuje je jako parę liczb bliźniaczych
        if pierwsza(j) == True and pierwsza(j-2) == True:
            pierwsze += str(j)+", "+str(j-2)+" | "
        else:
            continue
# jeśli nie znaleziono żadnej liczby pierwszej zwraca komunikat: brak
if pierwsze == "":
    pierwsze = "brak"
print(f"Bliźniacze pary z przedziału <{m},{n}>: {pierwsze}")
