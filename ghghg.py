import pygame.mixer
import world
from time import sleep
pygame.mixer.init()
pygame.mixer.music.load(open("C:\Users\Usuario\Desktop\Universidad\9 semestre\Conmutacionpython\sonidos\pickupthephone.wav","rb"))
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
      sleep(1)
print "done"

ab= world.Abonado('l','l','l')
