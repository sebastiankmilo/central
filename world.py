from datetime import datetime

import os
import sys
nb_dir = os.path.split(os.getcwd())[0]
print(nb_dir)
print sys.path
if nb_dir not in sys.path:
    sys.path.append(nb_dir)
class Abonado (object) :


    def __init__ (self, nombre, telefono, estado):
        self.Nombre = nombre
        self.Telefono = telefono
        self.Tiempo = 0
        pass

    def SaveTime(self, accion):
        to = datetime.now()
        accion()
        tf = datetime.now()
        time = tf-to
        time = time.seconds
        return time

pass
