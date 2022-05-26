# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 14:26:17 2022

@author: falco
"""

import numpy as np

corda_raiz = 0.5
corda_ponta = np.linspace(0.2,0.5)
afil = corda_ponta / corda_raiz

corda_media = (2 / 3) * corda_raiz * ((1 + afil + afil**2) / (1 + afil))

corda_media2 = (corda_raiz + corda_ponta) / 2

erro = (corda_media - corda_media2) * 100 / corda_media

print(f'Erro máximo = {erro.max()} %')
print(f'Erro medio = {erro.mean()} %')