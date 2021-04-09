# Silnia rekurencja
def silnia(x):
    if x < 0: return "liczba ujemna nie liczy się silni"
    if x ==0:return 1
    else: return silnia(x-1)*x
liczba = int(input("Podaj liczbę, dla jakiej chcesz obliczyć silnie: "))
print(f"{liczba}! = {silnia(liczba)}")