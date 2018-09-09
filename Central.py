import sys, os

nb_dir = os.path.split(os.getcwd())[0]
if nb_dir not in sys.path:
    sys.path.append(nb_dir)
import Abonado, Tonos
from datetime import datetime


class CentralTelefonica(object):
    global tonos
    tonos = Tonos.Tonos()

    def __init__(self, abonados, indicativo):
        self.abonados = abonados
        self.Indicativo = indicativo
        self.historial = []
        pass

    def llamar(self, usuario, destino):
        self.abonados[usuario].estado = 0
        n = self.abonados[destino].estado
        tonos.load('timbrar')
        if self.abonados[destino].estado == -1:
            tonos.load('fuera de servicio')
            self.abonados[destino].estado = n
            pass
        elif self.abonados[destino].estado == 0:
            tonos.load('ocupado')
            self.abonados[destino].estado = n
            pass
        elif self.abonados[destino].estado == 1:
            self.tiempo=self.abonados[usuario].SaveTime(tonos.load,'disponible')
            self.abonados[usuario].AddTime(self.tiempo)
            #tonos.load('disponible')
            self.abonados[destino].estado = n
            pass
        self.historial.append(datetime.now())
        pass

    def cobrar(self,usuario):
        tarifaPorSegundo = 1
        saldo = self.abonados[usuario].tiempo * tarifaPorSegundo
        return saldo

    pass
