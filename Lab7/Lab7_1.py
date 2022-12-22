import numpy as np
potegi=[]
for i in range(7,-1,-1):
    potegi.append(2**i)
print(potegi)

wagi = np.array(potegi)
print(wagi)

liczba_bin = np.random.randint(low=0,high=2,size=8)
print(liczba_bin)

iloczyn = liczba_bin * wagi
print(iloczyn)

suma = 0
for i in range(8):
    suma = suma + iloczyn[i]
print(suma)
#lub
print(iloczyn.sum())

