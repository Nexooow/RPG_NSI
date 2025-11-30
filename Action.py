import pygame

class Action:
    
    def __init__ (self, json):
        self.complete = False
        self.json = json
        
    def draw (self):
        pass
        
    def update (self, event):
        pass
        
    def executer (self, jeu):
        pass
        
    def est_complete (self):
        return self.complete

class Dialogue (Action):
    
    def __init__ (self, json):
        super().__init__(json)
        
    def draw (self):
        pass
        
    def update (self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.complete = True
        
    def executer (self, jeu):
        pass
