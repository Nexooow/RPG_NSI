import pygame
from menu.Menu import Menu

class Carte (Menu):
    
    def __init__ (self, jeu):
        self.jeu = jeu
        self.region = None
        
    def update (self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                print("fermer")
                self.fermer()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = event.pos
                if self.region is None: # graphe global
                    for region_name, region in self.jeu.regions.items():
                        region_position = region.position
                        if pygame.Rect(region_position[0]-50, region_position[1]-50, 150, 150).collidepoint(position):
                            self.region = region_name
                else:
                    region = self.jeu.regions[self.region]
                    for lieu_nom, lieu in region.lieux.items():
                        lieu_position = lieu["position"]
                        if pygame.Rect(region_position[0]-50, region_position[1]-50, 150, 150).collidepoint(position):
                            print(lieu_nom)
                        
                
                
    def fermer (self):
        self.jeu.fermer_menu()
        
    def draw (self):
        if self.region is None:
            self.jeu.carte.affichage(self.jeu.ui_surface)
        else:
            self.jeu.regions[self.region].carte.affichage(self.jeu.ui_surface)