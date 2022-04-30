import numpy as np
import ZebraLib as zb
import pandas as pd
import matplotlib.pyplot as plt
import random
from tqdm import tqdm
import itertools

it = int(50)

Cr = np.linspace(0.1, 0.8, it)
Af = np.linspace(0.1, 1, it)
b = np.linspace(1, 2.5, it)

A = (list(itertools.product(Cr, Af, b)))

Cr_list, Af_list, b_list, Cp_list, Cm_list = [], [], [], [], []
for elem in A:
    Cr_list.append(elem[0])
    Af_list.append(elem[1])
    b_list.append(elem[2])
    Cp_list.append(elem[0]*elem[1])
    Cm_list.append((2/3)*elem[0]*((1+elem[1]+elem[1]**2)/(1+elem[1])))

df = pd.DataFrame({'Cr':Cr_list, 'Cp':Cp_list, 'Cm':Cm_list, 'Af':Af_list, 'b':b_list})
df['S'] = (df['Cr']+df['Cp'])*df['b']*(0.5)
df['AR'] = df['b']/df['Cm']

filtro = df

N, Slo, Slo2, Slo3 = [], [], [], []
for x in tqdm(range(len(filtro.index))):
    Zb = zb.Airplane()
    Zb.b = filtro['b'].iloc[x]; Zb.AR = filtro['AR'].iloc[x] 
    Zb.c = filtro['Cm'].iloc[x]; Zb.Af = filtro['Af'].iloc[x]; Zb.S = filtro['S'].iloc[x]
    Zb.params_Calc

    N.append(Zb.save('D:/Aviões_gerados_x2.xlsx', False))
    #Slo.append(Zb.takeOff_Distance_AproxMiranda())
    Slo3.append(Zb.takeOff_Distance_EDO())


df2 = pd.DataFrame(N)
#df2['Slo_miran'] = Slo
df2['Slo_EDO'] = Slo3


try:
    df2.to_excel('D:/outputs_aviões.xlsx') #ESCOLHER UM LOCAL DO COMPUTADOR PRA SALVAR
except:
    df2.to_csv('D:/dados_TOP_02.csv')