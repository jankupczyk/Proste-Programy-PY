# Silnia iteracyjna
def silnia_i(n):
    s = 1
    for i in range(2, n+1):
        s *= i
    return s