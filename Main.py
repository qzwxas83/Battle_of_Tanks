import pygame
import os
import random
from Modules.Classes import *
from Modules.mapsetting import map


pygame.init()

x = 0
y = 0
blocks_list = []

wall_image1 = os.path.join(PATH, 'images/wall.png')
wall_image2 = os.path.join(PATH, 'images/wall1.png')

for row in map:
    for i in row:
        if i == 1:
            blocks_list.append(Block(x, y, 1, wall_image1))
        elif i == 2:
            blocks_list.append(Block(x, y, 2, wall_image2))
        x += STEP
    y += STEP
    x = 0


is_game_running = True
while is_game_running:
    for block in blocks_list:
        block.blit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False

    pygame.display.flip()