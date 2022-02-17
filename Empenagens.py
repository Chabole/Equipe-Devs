# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 14:45:21 2021

@author: Renan
"""

import numpy as np
import matplotlib.pyplot as plt
import time

start = time.time()
 
# x = (Limite regulamento - envergadura) - dist_motor até c.a.
x = 889.43 / 1000 
S = 0.843         # Área da asa  
b = 1.86          # Envergadura 
c_medium = 0.463  # Corda média da asa
AR = 3            # Alongamento

# Inclinação entre centro aerodiâmico da asa e do profundor
teta = np.linspace(np.pi/36, np.pi/18, 20) # 5 até 10 #np.degrees()

# Intervalos de cordas possíveis - profundor
cht = np.linspace(.150, .400, 20)

# Area da asa pela relação (S = c**2)*AR
s_it = (cht ** 2) * AR

#São lmitações
V_ht = [0.35, 0.5]

#LISTAS CRIADAS
Vht = list()       #Volume de cauda
Sht_old = list()   #Área de cauda inicial
lht_save = list()  #Distância entre c.a. da asa e do profundor inicial
lht_f = list()     #Distância entre c.a. da asa e do profundor final
Sht_f = list()     #Área de cauda final
teta_save = list() #Inclinação entre c.a. da asa e do profundo 

#Variando pra cada ângulo
for k in teta:
    l_ht = (x - cht * (3 / 4)) / np.cos(k) 

    for S_ht in (s_it):
        Vht_test = ((l_ht) * S_ht) / (c_medium * S)

        for j in range(len(Vht_test)):
            x_test = l_ht[j] * np.cos(k) + (3 / 4) * (S_ht / AR) ** (1 / 2)
            
            #Condição filtragem
            if (Vht_test[j] >= V_ht[0] and Vht_test[j] <= V_ht[1] and x_test <= x and x_test >= x*0.99):
                Vht.append(Vht_test[j])
                Sht_old.append(S_ht)
                lht_save.append(l_ht[j]) 
                teta_save.append(k)
        
Sht_n = np.array(Sht_old)
lht_n = np.array(lht_save)

# for indx, i in enumerate(lht_save):
#     if i >= (max(lht_save) * 0.99):
#         lht_f.append(i)
#         Sht_f.append(Sht_old[indx])

# Sht_n = np.array(Sht_f)
# lht_n = np.array(lht_f)

c_ht = (Sht_n / AR) ** (1 / 2)
b_ht = (Sht_n / c_ht)

data = np.array((Vht, lht_n, c_ht, b_ht, teta_save))

cont = 0
for i in range(0, len(data[1])):
    it = i - cont
    if (data[1][it] < (0.999 * max(data[1]))):
        data = np.delete(data, it, 1)
        cont += 1

cont = 0
for i in range(0, len(data[0])):
    it = i - cont
    if (data[0][it] < (0.999 * max(data[0]))):
        data = np.delete(data, it, 1)
        cont += 1

x_cord = np.empty((len(data[4])))
y_cord = np.empty((len(data[4])))


for i in range(0, len(data[4])):
    y_cord[i] = data[1][i] * np.sin(data[4][i])
    x_cord[i] = data[1][i] * np.cos(data[4][i])


fig, (ax1, ax2) = plt.subplots(2,1)
for i in range(0,len(data[0])):
    
    ax1.plot([0, data[3][i]], [0, 0]) 
    ax1.plot([data[3][i], data[3][i]], [0, data[2][i]])
    ax1.plot([0, data[3][i]], [data[2][i], data[2][i]]) 
    ax1.plot([0, 0], [0, data[2][i]])
    ax2.plot([(x_cord[i] - (data[2][i] / 4)), x_cord[i] + ((3/4) * data[2][i])], [y_cord[i], y_cord[i]])

ax2.plot([-(1/4)*0.526,(3/4)*0.526],[0,0])
ax2.plot([0,0], [0,-0.16])
ax2.set_xlim(0, 1)
plt.axis('equal')

print(f'termino em {time.time()-start}')

plt.show()

# Vvt = (l_vt * S_vt) / (b * S) 

