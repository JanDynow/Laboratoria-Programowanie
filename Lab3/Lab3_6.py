n = int(input("Podaj liczbę studentów: "))
i = 1
y = 0
while i <= n:
    x = int(input(f"Podaj liczbę punktów studenta {i} (0-100): "))
    if x < 0 or x > 100:
        continue
    y += x
    i += 1
z = y/n
print("Średnia wszystkich studentów wynosi: ", round(z, 2))