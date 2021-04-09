# NWD dla dowolnej liczby
n = int(input("Podaj liczbe:"))
print("Dzielniki liczby %d:" % n)
for i in range(1, n+1):
    if(n % i == 0):
        print(i)
