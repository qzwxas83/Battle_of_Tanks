import pygame
import os
import random
from Modules.Classes import *


pygame.init()

x = 0
y = 0
blocks_list = []

for row in map:
    for i in row:
        if i == 1:


is_game_running = True
while is_game_running:
    window.fill((255, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False

    pygame.display.flip()