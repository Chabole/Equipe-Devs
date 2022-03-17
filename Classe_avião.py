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

        print('arthur')
        self.__calc_L(); bbb=0
        print ('erro')
    def __calc_L(self, xlim=2.5, ylim=0.3):
        self.y_pos = np.linspace(0.3*ylim, ylim)
        self.x_pos = self.y_pos/np.tan(np.radians(self.teta))
        self.L = np.sqrt((self.x_pos*2)+(self.y_pos*2))

    def __filtragem(self, m, lim_min, lim_max):
        Vx = np.ravel(m)
        V = list()
        indice = list()
        p = len(m[0])
        for n in range(len(Vx)):
            if lim_min <= Vx[n] <= lim_max:
                V.append(Vx[n])
                indice.append(n)
        valor = np.array((indice)) / p
        v_pos_x = valor.astype(int)
        c = (valor - v_pos_x) * p
        v_pos_y = (np.around(c)).astype(int)
        return V, v_pos_x, v_pos_y