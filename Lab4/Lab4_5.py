'''Wyświetl informację o największej i najmniejszej ilości zdobytych punktów
• Wyświetl indeks pierwszego wystąpienia punktów podanych przez użytkownika. Jeżeli taka liczba
punktów nie występuje na liście, wyświetl odpowiedni komunikat
• Oblicz średnią punktów liczbę punktów z egzaminu
• Oblicz, ile osób zdobyło punkty powyżej, a ile poniżej średniej
• Wyświetl punkty poniżej średniej
• Wyświetl punkty powyżej średniej'''
import random
punkty = []
for x in range(15):
    punkty.append(round(random.uniform(0,50), 2))
print(punkty)
print("wartość minimalna: ", min(punkty))
print("wartość maksymalna: ", max(punkty))
liczba = float(input("Podaj liczbę: "))
if liczba in punkty:
    print("Index liczby to: ", punkty.index(liczba))
else:
    print("taka liczba nie istnieje")
suma = sum(punkty)
srednia = round(suma/len(punkty), 2)
print("Średnia liczba punktów to: ", srednia)

ponizej = []
for y in punkty:
    if y < srednia:
        ponizej.append(y)
powyzej = [y for y in punkty if y > srednia]
print("Osoby poniżej średniej: ", ponizej)
print("Osoby powyżej średniej: ", powyzej)
print(len(ponizej), len(powyzej))



