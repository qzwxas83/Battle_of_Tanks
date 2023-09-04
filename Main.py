import pygame
import os
import random
from Modules.Classes import *


pygame.init()


is_game_running = True
while is_game_running:
    window.fill((255, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False

    pygame.display.flip()