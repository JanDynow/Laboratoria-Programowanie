#Grupa 1. Użytkownik podaje 6 liczb. Zapisz do listy tylko liczby nieparzyste wieksze od 20.
i = 0
L = []
while i <= 5:
    x = int(input("Podaj dowolną liczbe: "))
    a = x % 2
    if a == 1 and x > 20:
        L.append(x)
    i += 1
print(L)
