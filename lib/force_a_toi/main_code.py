import base64
from io import BytesIO
from random import choice, randint

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pygame
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from matplotlib.transforms import offset_copy

from boom import *
from classe_graphe import *
from meteor import *
from npc import *
from sound import *
from text_display import *

def display_frames(image, frame_width, frame_height):
    frames = []
    sheet_width = image.get_width()
    sheet_height = image.get_height()
    num_frames = sheet_width // frame_width
    for i in range(num_frames):
        frame = image.subsurface((i * frame_width, 0, frame_width, frame_height))
        frames.append(frame)
    return frames

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1000, 700))

caelid = None
mt = None
fight_zone = None
list_meteor = []
clock = pygame.time.Clock()

half_radahn = pygame.image.load(BytesIO(base64.b64decode(b64_radahn))).convert_alpha()
radahn_frames = display_frames(half_radahn, 1200, 1350)
radahn_frame_index = 0
explosion_group = pygame.sprite.Group()

while True:
    if main_img == fight_zone:
        if not music_playing:
            play_music(
                "/mnt/c/Users/peter/Downloads/Gloria_Gaynor_-_I_Will_Survive_Re-Recorded_Remastered_(SkySound.cc).mp3"
            )
            music_playing = True
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        counter = int(195 - seconds)
        text = str(counter).rjust(3) if counter > 0 else ""
        if counter > 0:
            stop_music()
        screen.blit(radahn_frames[radahn_frame_index], (0, -120))
        radahn_frame_index = (radahn_frame_index + 1) % len(radahn_frames)
        this = randint(1, 200)
        if len(list_meteor) < 10 and this <= 10:
            if this > 3:
                list_meteor.append(Meteor((randint(25, 910), -25)))
            else:
                border = choice([25, 910])
                list_meteor.append(Meteor((border, randint(-25, 150))))
        for meteor in list_meteor:
            meteor.deplace()
            meteor.frame_index = (meteor.frame_index + 1) % len(meteor.frames)
            if meteor.rect.bottom >= 480:
                list_meteor.remove(meteor)
                explosion = Explosion(
                    meteor.rect.center[0], meteor.rect.center[1], meteor.size
                )
                explosion_group.add(explosion)
            else:
                screen.blit(meteor.frame, meteor.rect)
        text_render_centered_up(
            screen, "Survive", "bold", color=(255, 0, 0), pos=(500, 100)
        )
        screen.blit(font.render(text, True, (255, 0, 0)), (500, 150))
    clock.tick(45)
    explosion_group.draw(screen)
    explosion_group.update()

    pygame.display.update()
pygame.quit()
print(graphe.paths("Ceilidh", "Elder Tree"))
