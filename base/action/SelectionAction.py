import pygame
from .Action import Action

class SelectionAction(Action):
    """
    Action éxécutée lorsqu'il n'y a plus d'actions dans la file, et lorsque le joueur doit choisir
    ce qu'il veut faire.
    Exemple: ouvrir la carte, ouvrir l'inventaire...
    """

    def __init__(self, jeu):
        super().__init__(jeu, {"type": "selection-action"})
        self.option_choisie = 0

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.complete = True

    def draw(self):
        pass

    def executer(self):
        super().executer()
