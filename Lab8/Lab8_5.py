# Napisz program działający jak prosty kalkulator. W tym celu utwórz funkcje dodawanie(),
# odejmowanie(), mnożenie() oraz dzielenie(). Następnie utwórz słownik, którego kluczem jest działanie, a
# wartością – nazwa odpowiedniej funkcji.

def dodawanie(a,b):
    c = a + b
    return c
def odejmowanie(a,b):
    c = a - b
    return c
def mnozenie(a,b):
    c = a * b
    return c
def dzielenie(a,b):
    if b == 0:
        print("prosze tak nie robic")
    else:
        c = a / b
    return c
dict = {'+':dodawanie,'-':odejmowanie,'*':mnozenie,'/':dzielenie}
x = input("Podaj działanie [+,-,*,/]: ")
y = int(input("Liczba pierwsza: "))
z = int(input("kolejna liczba: "))
print(dict[x](y,z))


