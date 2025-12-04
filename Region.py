from lib.graph import Graph
from Jeu import Jeu

class Region:
    
    def __init__(self, jeu: Jeu, nom, action_entree = None, action_sortie = None):
        self.jeu = jeu
        self.nom = nom
        self.carte = Graph()
        self.lieux = {}
        self.action_entree = action_entree
        self.action_sortie = action_sortie
        
    def entrer (self):
        if self.nom not in self.jeu.lieux_visite:
            if self.action_entree:
                self.jeu.executer_sequence(self.action_entree)

    def sortir (self):
        if self.nom in self.jeu.lieux_visite:
            self.jeu.lieux_visite.add(self.nom)
            if self.action_sortie:
                self.jeu.executer_sequence(self.action_sortie)
