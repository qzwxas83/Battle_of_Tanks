import pygame
import os
from Modules.mapsetting import map

PATH = os.path.abspath(__file__ + '/../..')
SCREEN_WIDTH = 1540
SCREEN_HEIGHT = 790
STEP = 39.5
STEP_TANK = 1

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Batle of Tanks')


class Block(pygame.Rect):
    def __init__(self, x, y, type_block, image):
        super().__init__(x, y, STEP, STEP)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (STEP, STEP))
        self.type_block = type_block
    def blit(self):
        window.blit(self.image, (self.x, self.y))
class Bullet(pygame.Rect):
    pass

class Panzar(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x * STEP, y * STEP, STEP, STEP)
        self.image = None
        self.pos = [x, y]

        self.angle = 0
    def move(self):
        pass
    def blit(self):
        self.move()
        window.blit(self.image, (self.x, self.y))
    def rotate_to(self, angle):
        rotate = (360 - self.angle + angle)
        self.angle = angle
        self.image = pygame.transform.rotate(self.image, rotate)

class Player(Panzar):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load(os.path.join(PATH, 'images/panzer.png'))
        self.image = pygame.transform.scale(self.image, (STEP - 6, STEP - 6))
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if map[self.pos[1] - 1][self.pos[0]] == 0:
                self.y -= STEP_TANK
                self.pos[1] -= 1
            self.rotate_to(0)

        elif keys[pygame.K_s]:
            if map[self.pos[1] + 1][self.pos[0]] == 0:
                self.y += STEP_TANK
                self.pos[1] += 1
            self.rotate_to(180)

        elif keys[pygame.K_a]:
            if map[self.pos[1]][self.pos[0] - 1] == 0:
                self.x -= STEP_TANK
                self.pos[0] -= 1
            self.rotate_to(90)

        elif keys[pygame.K_d]:
            if map[self.pos[1]][self.pos[0] + 1] == 0:
                self.x += STEP_TANK
                self.pos[0] += 1
            self.rotate_to(270)

class Player2(Panzar):
    pass