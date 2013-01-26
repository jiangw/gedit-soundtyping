# play sound
import pygame

import time

pygame.init()

pygame.mixer.music.load("typewriter-key-1.wav")

pygame.mixer.music.play()

time.sleep(0.2)
