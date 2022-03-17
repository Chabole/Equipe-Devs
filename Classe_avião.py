import numpy as np
import ZebraLib as Lzb

class plane:
    def _init_(self, Sw=1, AR=2, teta=10, cw=0.5, bw=2):

        #Asa
        self.Sw = Sw
        self.teta = teta
        self.cw = cw
        self.bw = bw