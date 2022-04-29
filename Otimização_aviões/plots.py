#%% Recebe dados
import numpy as np
import ZebraLib as zb
import pandas as pd
import matplotlib.pyplot as plt
import random
from tqdm import tqdm
import itertools


df = pd.read_excel('D:/resultados_aviões_BRABO.xlsx', index_col=0)

filtro_2 = df[(df['Slo'] > 3) & (df['Slo'] <= 50)]
filtro_2.plot(kind='scatter', x='AR', y='S', alpha=1, 
            s=filtro_2['Af'], label='Af', figsize=(10,7), 
            c='Slo', cmap=plt.get_cmap('jet'), colorbar=True)
            
print('fg')