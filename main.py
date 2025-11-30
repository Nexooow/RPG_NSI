import pygame

from menu.accueil import Accueil
from lib.render import screen, transparent_surface
from lib.game import clock, jeu_en_cours, quitter, recuperer_partie

pygame.init()
pygame.display.set_caption("Game Name")

if __name__ == "__main__":
    
    accueil = Accueil()
    accueil.ouvrir()
    
    while jeu_en_cours():
        
        jeu = recuperer_partie()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quitter()
            if jeu is None:
                accueil.update(event)
            else:
                jeu.gerer_evenement(event)
        
        screen.fill((0, 0, 0))
        transparent_surface.fill((0, 0, 0, 0))
        
        center = screen.get_rect(center = (screen.get_width()/2, screen.get_height()/2))
        
        if jeu is None:
            accueil.draw()
        else:
            jeu.scene()
            
        screen.blit(transparent_surface, center)
    
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()