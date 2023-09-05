import pygame
import os
import random
from Modules.Classes import *
from Modules.mapsetting import map


pygame.init()

background = pygame.image.load(os.path.join(PATH, 'images/background.png'))
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

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

    player1 = Player(1,1)

    clock = pygame.time.Clock()

is_game_running = True
while is_game_running:
    window.blit(background, (0, 0))
    for block in blocks_list:
        block.blit()
    player1.blit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False
    clock.tick(120)
    pygame.display.flip()