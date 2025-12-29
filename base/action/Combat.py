import pygame
import random
from lib.render import text_render_centered, text_render_centered_left
from .Action import Action

parrysound = pygame.mixer.Sound("assets/sounds/parry.mp3")
parrysound.set_volume(0.05)

class Combat(Action):
    """
    Combat au tour par tour.
    """

    def __init__(self, jeu, data):
        super().__init__(jeu, data)
        self.desactive_ui = True

    def update (self, events):
        pass

    def draw (self):
        pass
