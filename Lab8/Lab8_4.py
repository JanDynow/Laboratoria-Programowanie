# Napisz funkcję znaki(), która zlicza znaki w string’u za pomocą słownika: znaki stanowią klucze, liczba
# znaków – wartości. Parametrem funkcji jest string. Funkcja ma zwracać słownik z wynikami. Wypisz słownik
# uporządkowany według kluczy.

a ="kalka"

def znaki(a):
    s = {}
    for x in a:
        if x in s:
            s[x] +=1
        else:
            s[x] = 1
    return s
print(znaki(a))





