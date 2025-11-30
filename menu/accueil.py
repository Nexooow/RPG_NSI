import pygame
import uuid
import random
import os
import json

from lib.render import text_render_centered, screen, transparent_surface
from lib.game import quitter, demarrer_jeu

from Jeu import Jeu
from menu.Menu import Menu

class Accueil (Menu):
    
    def __init__ (self):
        try:
            savesNames = os.listdir("./saves")
            self.saves = [
                json.load(open(f"./saves/{name}", "r")) for name in savesNames
            ]
        except FileNotFoundError:
            self.saves = []
        self.menu_selected_option = 0
        self.particules = []
        
    def ouvrir (self):
        pygame.mixer.music.load('./assets/music/intro.mp3')
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play(1, 0, 1000)
        
    def fermer (self):
        pygame.mixer.music.stop()
        
    def update (self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if self.menu_selected_option != 0:
                self.menu_selected_option -= 1
            if self.menu_selected_option == 1 and len(self.saves) == 0:
                self.menu_selected_option = 0
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if self.menu_selected_option != 3:
                self.menu_selected_option += 1
            if self.menu_selected_option == 1 and len(self.saves) == 0:
                self.menu_selected_option = 2
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE):
            self.fermer()
            pygame.mixer.Sound("./assets/sounds/accueil_clique.mp3").play()
            if self.menu_selected_option == 0:
                demarrer_jeu(Jeu(str(uuid.uuid4())))
            elif self.menu_selected_option == 1 and len(self.saves) > 0:
                pass 
            elif self.menu_selected_option == 2:
                pass
            elif self.menu_selected_option == 3:
                quitter()
        
        
    def draw (self):
        doit_generer = True if random.randint(1, 100) == 1 else False
        if doit_generer:
            particle_position = random.randint(0, 1280)
            alpha = random.randint(80, 225)
            self.particules.append(([particle_position, 720], alpha))
        
        for particle in self.particules:
            pygame.draw.circle(transparent_surface, (245, 205, 0, particle[1]), particle[0], 1)
            particle[0][1] -= 0.25
            if particle[0][1] < 0:
                self.particules.remove(particle)
                    
        text_render_centered(screen, "Game Name", "extrabold", color=(255, 255, 255), pos=(1280/2, 175), size=128)
            
        text_render_centered(transparent_surface, "Créer une partie", "regular",
            color = (245, 205, 0, 185),
            pos=(1280/2, 350),
            underline=self.menu_selected_option == 0
        )
        text_render_centered(transparent_surface, "Charger une partie", "regular",
            color = (245, 205, 0, 185) if len(self.saves) > 0 else (255-100, 215-100, 0, 140),
            pos=(1280/2, 400),
            underline=self.menu_selected_option == 1
        )
        text_render_centered(transparent_surface, "Paramètres", "regular",
            color = (245, 205, 0, 185),
            pos=(1280/2, 450),
            underline=self.menu_selected_option == 2
        )
        text_render_centered(transparent_surface, "Quitter", "regular",
            color = (245, 205, 0, 185),
            pos=(1280/2, 500),
            underline=self.menu_selected_option == 3
        )
