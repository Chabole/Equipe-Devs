import numpy as np
#import ZebraLib as Lzb
import matplotlib.pyplot as plt

class plane:

    def __init__(self, Sw=1, AR=2, teta=10, cw=0.5, bw=2):
        #Asa
        self.Sw = Sw
        self.teta = teta
        self.cw = cw
        self.bw = bw 
                #Profundor e leme
        self.AR = AR
        self.S = np.linspace(0.05, 0.6)
        self.c = (self.S / self.AR) **(1 / 2)
        self.b = self.S/self.c

        #Calculos
        self.__calc_L()
        
    def __calc_L(self, xlim=2, ylim=0.3):
        
        if self.teta != 0:
            self.y_pos = np.linspace(0.3*ylim, ylim)
            self.x_pos = self.y_pos/np.tan(np.radians(self.teta))
            self.L = np.sqrt((self.x_pos*2)+(self.y_pos*2))
        else:
            self.L = np.linspace(0.1*xlim, xlim)

    def __filtragem(self, mh, mv):
        Vxh = np.ravel(mh)
        Vxv = np.ravel(mv)
        Vh = list()
        Vv = list()
        indiceh = list()
        indicev = list()
        p = len(mh[0])
        for n in range(len(Vxh)):
            if 0.35 <= Vxh[n] <= 0.5:
                Vh.append(Vxh[n])
                indiceh.append(n)
            if 0.04 <= Vxv[n] <= 0.06:
                Vv.append(Vxv[n])
                indicev.append(n)
        #Horizontal
        valor = np.array((indiceh)) / p
        v_posh_x = valor.astype(int)
        c = (valor - v_posh_x) * p
        v_posh_y = (np.around(c)).astype(int)
        #Vertical
        valor = np.array((indicev)) / p
        v_posv_x = valor.astype(int)
        c = (valor - v_posv_x) * p
        v_posv_y = (np.around(c)).astype(int)
        
        return Vh, Vv, v_posh_x, v_posh_y, v_posv_x, v_posv_y
    
    def volumes(self):
        vh = []; vv = []
        for i in range(len(self.L)):
            vh.append(self.L[i]*self.S/(self.cw*self.Sw))
            vv.append(self.L[i]*self.S/(self.bw*self.Sw))
        return self.__filtragem(vh, vv)
    
    def optmize(self, l, Sv, Sh, D=0.025, plot=False): 
        Sfus = 2 * np.pi * D * l
        Swet = Sfus + Sh * Sv 
        idx = np.where(Swet.min() == Swet)
        if plot:
            plt.plot(l, Swet, label = 'Swet')
            plt.plot(l, Sv, label = 'Sv')
            plt.plot(l, Sh, label = 'Sh')
            plt.plot(l, Sfus, label = 'Sfus')
            plt.ylabel('Área molhada (m^2)')
            plt.xlabel('Tamanho de cauda (m)')
            plt.legend()
        return l[idx]