import pygame
from random import randint
from io import BytesIO
import base64
import math
with open("meteor_sprite_sheet.txt","r") as f:
    b64=f.read()
class Meteor:
    def __init__(self,center,image=b64,frame_index=0):
        self.image=pygame.image.load(BytesIO(base64.b64decode(image))).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.center=center
        self.speed=randint(2,10)
        self.x_speed=randint(2,10) if center[0]==25 else randint(-10,-2) if center[0]==910 else randint(-10,10)
        self.size=randint(1,6)*0.1
        self.frames=self.load_frames()
        self.frame_index=frame_index
    def deplace(self):
        self.rect=self.rect.move(self.x_speed,self.speed)
    def collision(self):
        return self.rect.colliderect(targetRect)
    def load_frames(self,frame_width=448,frame_height=448):
        frames = []
        sheet_width = self.image.get_width()
        sheet_height =self.image.get_height()
        num_frames = sheet_width // frame_width
        for i in range(num_frames):
            frame = self.image.subsurface((i*frame_width,0,frame_width,frame_height))
            scale_w=int(frame_width*self.size)
            scale_h=int(frame_height*self.size)
            frame=pygame.transform.scale(frame,(scale_w,scale_h))
            frame=pygame.transform.rotate(frame,math.atan(self.x_speed/self.speed)*180/math.pi)
            frames.append(frame)
        self.rect=frames[0].get_rect(center=self.rect.center)
        return frames
