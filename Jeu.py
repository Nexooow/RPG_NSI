import pygame

from lib.graph import Graph
from Action import Action
from JSONLoader import JSONLoader
from lib.file import File
from lib.render import draw_rectangle, text_render_centered, text_render, screen

sommets = ["Auberge", "Mountain", "Ceilidh", "Dawn of the world", "Elder Tree"]
aretes = [
    ("Auberge", "Mountain", 0),
    ("Mountain", "Ceilidh", 0),
    ("Mountain", "Auberge", 0),
    ("Ceilidh", "Mountain", 0),
    ("Ceilidh", "Auberge", 0),
    ("Auberge", "Elder Tree", 0),
    ("Auberge", "Ceilidh", 0),
    ("Auberge", "Dawn of the world", 0)
]
positions_sommets = {
    "Auberge": (200, 400),
    "Mountain": (600, 120),
    "Ceilidh": (660, 480),
    "Dawn of the world": (450, 500),
    "Elder Tree": (500, 230),
}

class Jeu:

    def __init__ (self, id: str, json: dict | None = None):
        
        self.identifiant = id
        
        self.loader = JSONLoader(self)
        self.action_actuelle: Action | None = None
        self.actions = File()
        
        self.carte = Graph(
            sommets,
            aretes,
            positions_sommets,
            True,
            "background.webp"
        )
        
        self.regions = {}
        self.region = json["emplacement"]["region"] if json else "Auberge"
        # self.lieu = json["emplacement"]["lieu"] if json else self.regions[self.region].lieu_depart
        self.jour = 1
        self.heure = 12
        self.minute = 0

    def gerer_evenement (self, evenement):
        if self.action_actuelle is not None:
            self.action_actuelle.update(evenement)
            
    def executer_sequence (self, id):
        sequence = self.loader.actions_sequences[id]
        for action in sequence:
            self.actions.enfiler(action)
            
    def executer (self):
        action = self.action_actuelle
        if action is None:
            if not self.actions.est_vide():
                self.action_actuelle = self.actions.defiler()
                assert self.action_actuelle is not None
                self.action_actuelle.executer(self)
        else:
            if action.est_complete():
                if not self.actions.est_vide():
                    self.action_actuelle = self.actions.defiler()
                    assert self.action_actuelle is not None
                    self.action_actuelle.executer(self)
                else:
                    self.action_actuelle = None
                    
    def scene (self):
        if self.action_actuelle is not None:
            self.action_actuelle.draw()
        self.ui()
        
    def ui (self):
        pass
        
    def deplacement (self, lieu_region, est_region = False):
        pass
        
    def save (self):
        pass