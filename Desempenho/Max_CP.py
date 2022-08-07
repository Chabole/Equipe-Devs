from scipy.integrate import odeint
from scipy.integrate import quad, solve_ivp
from scipy import integrate
import numpy as np
import ZebraLib as zb
import pandas as pd
import matplotlib.pyplot as plt
import random
from tqdm import tqdm

Zb = zb.Airplane()

'''def resid(x):
    Zb.Load = x
    #Zb.params_Calc
    return Zb.takeOff_Distance_EDO() + Zb.hdist_Obstacle() - 56.5

#Wmax = zb.robustNewton(resid, 8, xtol=1e-1, nitermax=1e3)

fig, ax = plt.subplots()

x = np.arange(1, 9, 0.1)

for i in range(len(x)):
    ax.scatter(x[i], resid(x[i]))

plt.show()
#print(Wmax)'''
A = Zb.info()
print(A)
