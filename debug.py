
import numpy as np
import pandas as pd

def volumes(L, S, k='b ou c', Sw='área da asa'):
    v = []
    for i in range(len(L)):
        v.append(L[i]*S/(k*Sw))
    return filtragem(v)

def filtragem(m, lim_min=0.35, lim_max=0.5):
    k = np.ravel(np.array((m)))
    z = list();b = list()

    for n in range(len(k)):
        if lim_min <= k[n] <=lim_max:
            z.append(k[n])
            b.append(n)
    return z, b

L = np.linspace(0.5, 1.5, 10) #0.5 - 1.5
S = np.linspace(0.1, 0.4, 10) #0.1 - 0.4

valor, pos = volumes(L, S, k=0.4, Sw=1)

