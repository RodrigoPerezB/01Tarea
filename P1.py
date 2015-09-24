'''
Parte 1
'''

import matplotlib.pyplot as plt
import numpy as np

plt.figure(1)
plt.clf()

Radsol = np.loadtxt("./sun_AM0.dat")
# x es longitud de onda en micrón
x=Radsol[:,0]*0.001
# y debe ser flujo (en cgs)
y=Radsol[:,1]

plt.plot(x,y,color='r')
plt.yscale('log')
plt.xlabel('Longitud de onda $[\mu$$m]$')
plt.ylabel('Flujo $[\\frac{g}{s^3*\mu m}]$')
plt.title("Flujo vs longitud de onda",color='b')
plt.savefig('radiacion.png')
