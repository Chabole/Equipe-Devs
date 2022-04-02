import numpy as np
import ZebraLib as zb
import time 
import pandas as pd

class Aviao():

    def init(self, b=1.86, S=0.843, Af=0.601, CLn=1.080, CLmax=1.5193, c=0.463):
        self.b = b
        self.S = S
        self.Af = Af
        self.CLn = CLn
        self.CLmax = CLmax
        self.c = c

    def dados(self):
        self.S = np.linspace(0.5, 1.5, 10000)
        self.b = np.linspace(1.5, 2.5, 10000)
        self.Af = np.linspace(0.2, 1, 10000)
        self.CLn = np.linspace(1.3, 1.87, 10000)
        self.c = np.linspace(0.2, 0.8, 10000)

        z = list()
        for x in range(5):
            p = zb.Airplane(S=self.S[x], b=self.b[x], Af=self.Af[x], CLn=self.CLn[x], c=self.c[x])
            z.append(p)
        return z
    
df = pd.DataFrame()

start = time.time()
teste = Aviao()
a = teste.dados()

print(time.time() - start)