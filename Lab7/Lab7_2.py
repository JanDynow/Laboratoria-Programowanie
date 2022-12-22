import numpy as np

macierz = np.random.randint(low=1, high=50, size=(5,5))
print(macierz)

print("Wartość maksymalna: ", macierz.max())
print("Wartość minimalna: ", macierz.min())


print("Wartość maksymalna po wierszach: ", macierz.max(axis=1))
print("Wartość maksymalna po kolumnach: ", macierz.max(axis=0))

print("Suma w poszczególnych wierszach", macierz.sum(axis=1))



