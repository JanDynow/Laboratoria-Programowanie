import numpy as np

tablica = np.zeros([3,3])
print(tablica)


#tablica[1:,:2] = 1     pierwszy wycinek
#tablica[:,2] = 1       drógi wycinek
#tablica[:2,:] = 1      trzeci wycinek
#tablica[:2,::2] = 1    piaty wycinek
#lub
tablica[:2, [0,2]] = 1
print(tablica)




