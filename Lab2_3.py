import math
print("Operatory w kalkilatorze: Dodawanie:'1', Odejmowanie:'2', Mnożenie'3', Dzielenie'4', Potęgowanie'5'")
a = int(input("podaj pierwszą liczbę: "))
b = int(input("podaj kolejną liczbę: "))
c = input("podaj operator: ")
operacja  = {"1":a+b, "2":a-b, "3":a*b, "4":a/b, "5":a**b}
if c == "1":
    print(operacja["1"])
elif c == "2":
    print(operacja["2"])
elif c == "3":
    print(operacja["3"])
elif c == "4":
    print(operacja["4"])
elif c == "5":
    print(operacja["5"])
else:
    print("Podaj właściwy operator!")
