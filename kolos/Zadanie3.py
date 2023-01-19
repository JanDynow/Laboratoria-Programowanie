# Napisz funkcję, która ma dwa parametry a, b. Funkcja ma utworzyć i zwrócić listę wypełnioną liczbami od
# mniejszej z przekazanych wartości do większej (bez wykorzystania range()). Sprawdź działanie funkcji.

def fun(a,b):
    l=[]
    if b < a:
        a,b = b,a
        l.append(a)
        l.append(b)
        print(l)
    else:
        l.append(a)
        l.append(b)
        print(l)

fun(20,7)












