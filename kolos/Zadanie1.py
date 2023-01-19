# Napisz program, który wygeneruje 100 liczb losowych z przedziału [1, 100] i sprawdzi, ile z tych liczb jest
# podzielnych przez x (x podaje użytkownik). (liczby nie zapisuj do listy)
import random
n = 0
i = 0
while n<= 100:
    for i in random(1,100):
        x = int(input("Podaj x: "))
        y = i % x
        if y == 0:
            i += 1
        else:
            i += 0
    print(i)
    n +=1












