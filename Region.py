from lib.graph import Graph
from Jeu import Jeu

class Region:
    
    def __init__(self, jeu: Jeu, nom):
        self.jeu = jeu
        self.nom = nom
        self.carte = Graph()
        self.lieux = []
        
    