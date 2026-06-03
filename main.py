import pygame
import json
import os
import ctypes
from Core.Scene_Manager import SceneManager

try:
    # Memaksa Windows agar tidak melakukan auto-zoom pada jendela game
    ctypes.windll.user32.SetProcessDPIAware()
except AttributeError:
    pass # Abaikan jika pemain menggunakan Mac / Linux

pygame.init()

# Inisialisasi Window
Screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Visual Novel")

Clock = pygame.time.Clock()

Scene = SceneManager()

Running = True

while Running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            Running = False

        Scene.Eventhandler(event)

    Scene.Update()

    # Bersihkan layar
    Screen.fill((0, 0, 0))

    # Render scene aktif
    Scene.Render(Screen)

    pygame.display.flip()

    Clock.tick(60)

pygame.quit()
