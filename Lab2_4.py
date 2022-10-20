#Napisz skrypt, która zamienia wprowadzoną literę na przeciwną (co do wielkości) i wypisuje ją na ekranie.
#Zadanie 4
print("Zadanie 4")
a = input("Podaj teks: ")

roznica = ord('a') - ord('A')
dodawanie = ord(a) + roznica
znak = chr(dodawanie)

if 'a' <= a <= 'z':
    print(chr(ord(a) - roznica))
elif 'A' <= a <= 'Z':
    print(znak)
else:
    print("To nie jest litera")

