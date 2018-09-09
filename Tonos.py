import pygame.mixer
import os
from time import sleep


class Tonos(object):

    def __init__(self):
        dir = os.path.split(os.getcwd())[0]
        self.tonos = {10: dir+"\sonidos\T0.wav",
                      1: dir+"\sonidos\T1.wav",
                      2: dir+"\sonidos\T2.wav",
                      3: dir+"\sonidos\T3.wav",
                      4: dir+"\sonidos\T4.wav",
                      5: dir+"\sonidos\T5.wav",
                      6: dir+"\sonidos\T6.wav",
                      7: dir+"\sonidos\T7.wav",
                      8: dir+"\sonidos\T8.wav",
                      9: dir+"\sonidos\T9.wav",
                      'disponible': dir+"\sonidos\disponible.wav",
                      'ocupado': dir+"\sonidos\Ocupado.wav",
                      'fuera de servicio': dir+"\sonidos\FueraS.wav",
                      'timbrar':dir+"\sonidos\Timbrar.wav"
                      }
    pass

    def load(self, tono):
        pygame.mixer.init()
        pygame.mixer.music.load(open(self.tonos[tono], "rb"))
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            sleep(1)
        pass
    pass
pass