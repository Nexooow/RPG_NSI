import base64
from io import BytesIO

import pygame
from pygame.locals import *


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.images = []
        for i in range(5):
            img = pygame.image.load("./assets/sprites/explosion_" + str(i+1) + ".png")
            img = pygame.transform.scale(img, (400 * size, 400 * size))
            self.images.append(img)
        self.explosion_speed = 4
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0

    def update(self):
        self.counter += 1
        if self.counter >= self.explosion_speed:
            self.counter = 0
            self.index += 1

            if self.index >= len(self.images):
                self.kill()
                return
            self.image = self.images[self.index]
