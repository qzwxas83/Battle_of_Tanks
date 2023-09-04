import pygame
import os

PATH = os.path.abspath(__file__ + '/../..')
SCREEN_WIDTH = 1520
SCREEN_HEIGHT = 880
STEP = 40

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
    pass
class Player(Panzar):
    pass
class Player2(Panzar):
    pass