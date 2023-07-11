import random
from tqdm import tqdm
import numpy as np
import pandas as pd
# Random distribution generator function
def gerador(x=1, min=1, max=5): #The numbers "min" and "max" just are used to generate, you can use what you want  

    #1D array
    if x==1: 
        return float(random.uniform(min, max))  
    
    #2D array or plus
    else:
        lista = np.empty((x)) #np.empty is faster then np.zeros or some known solution
        for i in (range(x)): 
            lista[i]=(float(random.uniform(min, max)))
        return lista

"---------------------------------------------------------------------------------------------------------------------"

class loteria:
    def __init__(self, x=100):
        self.x = int(x) #turning any number into a integer

    #Create a DataFrame with the parameters of the SAE Aero 

    def gen_dados(self, loading=True): 
        df = pd.DataFrame()

        df['PV_prev'] = self.PV_prev()
        df['PV_real'] = self.PV_real()
        df['CP_prev'] = self.CP_prev()
        df['CP_real'] = self.CP_real()
        df['NR'] = self.NR()
        df['NR_max'] = self.NR_max()
        df['tempo'] = self.tempo()

        results = np.empty((len(df['PV_prev'])))

        if loading:
            for i in tqdm(range(len(df['PV_prev']))):

                pt = pontuação( df['PV_prev'].iloc[i], df['PV_real'].iloc[i],
                                df['CP_prev'].iloc[i], df['CP_real'].iloc[i], 
                                df['NR'].iloc[i], df['NR_max'].iloc[i], 
                                df['tempo'].iloc[i])      

                results[i] = pt.calc()
        else:
            for i in (range(len(df['PV_prev']))):

                pt = pontuação( df['PV_prev'].iloc[i], df['PV_real'].iloc[i],
                                df['CP_prev'].iloc[i], df['CP_real'].iloc[i], 
                                df['NR'].iloc[i], df['NR_max'].iloc[i], 
                                df['tempo'].iloc[i])      

                results[i] = pt.calc()
        df['resultados'] = results
        return df
    
    def PV_prev(self):
        return gerador(self.x, 1, 3.5)
    
    def PV_real(self):
        return gerador(self.x, 1, 3.5)

    def CP_prev(self):
        #5 é minima carga pra competição eu acho (5 is the less load for the competition, I guess)
        return gerador(self.x, 5, 20) 

    def CP_real(self):
        #5 é minima carga pra competição eu acho (5 is the less load for the competition, I guess)
        return gerador(self.x, 5, 20)

    def NR(self):
        return gerador(self.x, 10, 185)
    
    def NR_max(self):
        return float(185)
    
    def tempo(self):
        return gerador(self.x, 0, 120)

class pontuação:

    def __init__(self, PV_previsto, PV_real, CP_previsto, CP_real, NR, NR_max, tempo):
        self.PV_previsto = PV_previsto #Peso vazio previsto #Empty predicted load 
        self.PV_real = PV_real         #Peso vazio real     #Empty real load
        self.CP_previsto = CP_previsto #Carga paga previsto #Predicted Payload 
        self.CP_real = CP_real         #Carga paga real     #Real Payload
        self.NR = NR                   #Nota de relatório   #Report grade
        self.NR_max = NR_max           #Nota de relatório máxima #Max report grade
        self.tempo = tempo             #Tempo de descarga    #Download time

    def calc(self):
        return self.PCP() + self.FPV() + self.FPR() + self.P_voo() + self.P_AC() + self.B_PO() + self.B_RC() #ainda não coloqueui B_CF 

    #7.8.1
    def PCP(self):
        return 12.5*self.CP_real

    #7.8.2
    def FPV(self):
        pontuação_min = 0.8
        A =  1.1 - 15*(((self.PV_previsto-self.PV_real)/self.PV_previsto)**2)
        if A >= pontuação_min:
            return A
        else:
            return pontuação_min

    #7.8.3
    def FPR(self):
        pontuação_min = 1
        A = 0.5 + (0.9*(self.NR/self.NR_max))
        if A >= pontuação_min:
            return A
        else:
            return pontuação_min
    #7.8.4
    def P_voo(self):
        return self.FPR()*self.FPV()*self.PCP()

    #7.8.5
    def P_AC(self):
        #O segundo abs eu inventar -- testar mais tarde
        pontuação_min = 0
        A = 30 - (830*abs((abs(self.CP_previsto - self.CP_real)/self.CP_previsto)**1.75))
        if A >= 0:
            return A
        else:
            return pontuação_min

    #7.8.6
    def B_PO(self):
        return 1*self.CP_real

    #7.8.7
    def B_RC(self):
        pontuação_min = 20
        A = 40 - (self.tempo/3)
        if A >= pontuação_min:
            return A
        else:
            return pontuação_min

    #7.8.8
    def B_CF(self, PB1, PB2):
        pontuação_min = 0
        A = 20*(1-(5*((PB1-PB2)/PB1))**2)
        if A >= pontuação_min:
            return A
        else:
            return pontuação_min