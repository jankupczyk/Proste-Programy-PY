# Program liczby z tablicy PALINDROMICZNE
n = int(input("Podaj liczbę liczb do sprawdzenia: "))
suma = []
for x in range (n):
    x = str(x + 1)
    next_numb = int(input("Podaj " + x + " liczbę: "))
    while next_numb < 10:
        print("Podaj liczbę dwucyfrową!!!")
        next_numb = int(input("Podaj " + x + " liczbę: "))
        if str(next_numb)==str(next_numb)[::-1]:
            suma.append(next_numb)
            print(*suma, sep='/n')