# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 09:19:20 2022

@author: falco
"""

import numpy as np
import matplotlib.pyplot as plt

#Inputs
AR = 4
afil = 0.9
a_perfil = 5.781

# alfa_0 = -14
# alfa = 10

#Função fator de arrasto induzido
def fat_di(AR, afil):
    #Data AR
    delt_x = np.array([0.2,0.4,0.6,0.8,1])
    delt_AR4  = np.array([0.004,0.002,0.008,0.02,0.04])
    delt_AR6  = np.array([0.008,0.004,0.02,0.04,0.06])
    delt_AR8  = np.array([0.016,0.008,0.027,0.053,0.08])
    delt_AR10 = np.array([0.02,0.016,0.035,0.072,0.12])
    
    delt_AR = np.array(([delt_AR4,
                        np.mean((delt_AR4, delt_AR6), axis=0),
                        delt_AR6,
                        np.mean((delt_AR6, delt_AR8), axis=0),
                        delt_AR8,
                        np.mean((delt_AR8, delt_AR10), axis=0),
                        delt_AR10]))
    #Seleção
    AR_test = np.array([4,5,6,7,8,9,10])
    idx = np.argmin(abs(AR - AR_test))
    
    #Calculo
    x = delt_x
    y = delt_AR[idx]
    z = np.polyfit(x, y, 4)
    func = np.poly1d(z)
    
    x_ = np.linspace(x.min(), x.max(),100)
    #plt.plot(x,y,'o')
    #plt.plot(x_, func(x_))
    return func(afil)

#calc
def red_cl(AR, afil, a_perfil=0.1009):
    if AR < 4:
        a_asa = a_perfil / (np.sqrt(1 + (((180/np.pi) * a_perfil / (np.pi * AR)) ** 2 )+ ((180/np.pi) * a_perfil / (np.pi * AR))))
    if AR >= 4:
        delt = fat_di(AR, afil)
        e = 1 / (1 + delt)
        a_asa = a_perfil / (1 + ((180/np.pi) * a_perfil/(np.pi * e * AR)))
    perc_red = a_asa/a_perfil
    return perc_red

teste = red_cl(AR, afil)
print(f'Clmax={teste*2.025}') #2.025
print(f'Clmax={teste*2.025}') #2.025
