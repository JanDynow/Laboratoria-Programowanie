
#instalujemy i importujemy biblioteke matplotlib

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-(np.pi), np.pi, 100)
y = np.sin(x)
plt.plot(x,y)
# plt.plot(x, np.sin(x)*2) pierwszy wykres
# plt.plot(x, np.sin(x)+2) drógi wykres
plt.plot(x, np.sin(x*2))
plt.show()








