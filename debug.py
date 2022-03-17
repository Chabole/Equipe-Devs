
import numpy as np
import pandas as pd

def volumes(L, S, k='b ou c', Sw='área da asa'):
    v = []
    for i in range(len(L)):
        v.append(L[i]*S/(k*Sw))
    return filtragem(v)

def filtragem(m, lim_min=0.35, lim_max=0.5):
    Vx = np.ravel(m)
    V = list()
    indice = list()
    p = len(m[0])
    for n in range(len(Vx)):
        if lim_min <= Vx[n] <= lim_max:
            V.append(Vx[n])
            indice.append(n)
    valor = np.array((indice)) / p
    v_pos_x = valor.astype(int)
    c = (valor - v_pos_x) * p
    v_pos_y = (np.around(c)).astype(int)
    return V, v_pos_x, v_pos_y

#Inputs
S = np.linspace(0.1,0.5) #m^2
xlim = 2.5; ylim = 0.3   #m
teta = 10                #graus
deg2rad = np.pi/180
AR = 2

#Processamento
c = (S / AR) **(1 / 2)
b = (S / c)
y_pos = np.linspace(0.3*ylim, ylim)
x_pos = y_pos/np.tan(teta * deg2rad)
l  =  np.sqrt((x_pos*2)+(y_pos*2))

values = np.array((S, l))

valor, indice_l, indice_S = volumes(values[1], values[0], k=0.4, Sw=1)

print(valor[0], l[indice_l[0]], S[indice_S[0]])

print(x_pos[indice_l[0]], y_pos[indice_l[0]])
print(c[indice_S[0]], b[indice_S[0]])


