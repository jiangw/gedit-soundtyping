# play sound
import pygame

import time

#pygame.init()

#pygame.mixer.music.load("/home/jiang/Share/gedit/plugins/SoundTyping/123.wav")

#pygame.mixer.music.play()

#time.sleep(0.2)

pygame.mixer.init()
s1 = pygame.mixer.Sound("/home/jiang/Share/gedit/plugins/SoundTyping/ABC.wav")
s2 = pygame.mixer.Sound("/home/jiang/Share/gedit/plugins/SoundTyping/abc.wav")

s1.play()
s2.play()

time.sleep(0.2)
