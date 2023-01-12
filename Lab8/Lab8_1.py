# Napisz funkcję find(), która w liście sprawdza czy występuje podana wartość. Lista i wartość są
# parametrami funkcji. Funkcja ma zwracać listę indeksów, pod którymi wystąpiła wartość. Nie wolno korzystać z
# operatora in w celu sprawdzenia czy wartość występuje w liście.



def find(a,b):
    list = []
    for i in range(len(a)):
        if a[i] == b:
            list.append(i)
    return list
print(find([1,2,3,4,5,6,4,6,7,],4))

L = [6,12,89,100,578,5,12,5321,12]
wynik = find(L,12)
print(wynik)









