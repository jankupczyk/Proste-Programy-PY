# Pesel
pesel=int(input("Podaj swój Pesel: "))
c10=int(pesel[9])
if c10%2== 0:
print("Kobieta")
else:
    print("Mężczyzna")
