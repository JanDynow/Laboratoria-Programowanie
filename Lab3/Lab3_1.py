#Zadanie 1
'''
("Podaj dwie liczby jdedną większą druga mniejszą")
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
print("wejście: ", a, b)
if a > b:
    max = a
    min = b
else:
    max = b
    min = a
while min != max:
    print(min, end=" ")
    min += 1
'''
print("Podaj dwie liczby jdedną większą druga mniejszą")
x = int(input("Podaj x: "))
y = int(input("Podaj y: "))
if y < x:
    x,y = y,x
while x <= y:
    print(x, end=" ")
    x += 1
