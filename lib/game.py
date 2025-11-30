import pygame

clock = pygame.time.Clock()
jeu_instance = None
running = True

def jeu_en_cours():
    return running

def quitter():
    global running
    running = False

def recuperer_partie():
    return jeu_instance

def demarrer_jeu(value):
    global jeu_instance
    jeu_instance = value
    