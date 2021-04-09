# Funkcja sprawdzająca czy x jest liczbą pierwszą
def pierwsza(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


m, n = -1, -1
while m < 0 or n < 0:
    m = int(input("Podaj początek przedziału: "))
    n = int(input("Podaj koniec przedziału: "))
    if m < 0 or n < 0:
        print("Obie liczby muszą być liczbami naturalnymi!")
pierwsze = ""
if m <= n:
    for j in range(m, n+1):
        if pierwsza(j) == True:
            pierwsze += str(j)+", "
        else:
            continue
if m > n:
    for j in range(m, n-1, -1):
        if pierwsza(j) == True:
            pierwsze += str(j)+", "
        else:
            continue
if pierwsze == "":
    pierwsze = "brak"
print(f"Liczby pierwsze z przedziału <{m},{n}>: {pierwsze}")
