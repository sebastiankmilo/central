from datetime import datetime


class Abonado(object):

    def __init__(self, nombre, telefono, estado):
        self.nombre = nombre
        self.telefono = telefono
        self.tiempo = 0
        self.lastcalltime = 0
        self.estado = estado
        pass

    def SaveTime(self, accion, mensaje):
        to = datetime.now()
        accion(mensaje)
        tf = datetime.now()
        time = tf - to
        time = time.seconds
        self.lastcalltime = time
        return time

    def AddTime(self, tiempo):
        self.tiempo = self.tiempo + tiempo
        pass

    def __str__(self):
        return self.nombre + ' : ' + str(self.telefono)

    pass

pass
