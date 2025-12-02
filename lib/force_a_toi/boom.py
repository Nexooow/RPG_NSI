import pygame
from pygame.locals import *
import base64
from io import BytesIO

class Explosion(pygame.sprite.Sprite):
    def __init__(self,x,y,size):
        super().__init__()
        self.images=[]
        with open("sprite.txt", "r") as f:
            lines = f.read().splitlines()
        for i in range(5):
            img_data = base64.b64decode(lines[i])
            img = pygame.image.load(BytesIO(img_data))
            img = pygame.transform.scale(img,(400*size,400*size))
            self.images.append(img)
        self.explosion_speed=4
        self.index=0
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
        self.counter=0
    def update(self):
        self.counter+=1
        if self.counter>=self.explosion_speed:
            self.counter=0
            self.index+=1

            if self.index>=len(self.images) :
                self.kill()
                return
            self.image=self.images[self.index]
