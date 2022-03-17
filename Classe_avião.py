import numpy as np
import ZebraLib as Lzb

class plane:
    def _init_(self, Sw=1, AR=2, teta=10, cw=0.5, bw=2):

        #Asa
        self.Sw = Sw
        self.teta = teta
        self.cw = cw
        self.bw = bw 
                #Profundor e leme
        self.AR = AR
        self.S = np.linspace(0.05, 0.5)
        self.c = (self.S / self.AR) **(1 / 2)
        self.b = self.S/self.c

        #Calculos

        self.__calc_L()