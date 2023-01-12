# Napisz funkcję potęga(), która podniesie wartości z pierwszej listy do potęg z drugiej listy. Sprawdź,
# czy listy są tej samej długości. Parametrami funkcji są dwie listy. Funkcja ma zwracać listę z wynikami.


licz = [1,2,3,4,5]
pot = [2,2,2,2,2]

def potega(a,b):
    p = 0
    lista = []
    for x in range(len(a)) and range(len(b)):
            p = a[x]**b[x]
            lista.append(p)
    return lista

print(potega(licz,pot))
