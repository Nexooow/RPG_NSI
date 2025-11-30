import json
import os
from random import random, randint
import glob

from Action import Dialogue

class JSONLoader:
    
    def __init__ (self, parent):
        self.parent = parent
        
        self.actions_sequences = {}
        
        self.charger_actions()
        # self.charger_npcs()
                
    def charger_actions (self):
        files = glob.glob("./data/actions/*.json")
        for file in files:
            try:
                with open(file, 'r') as f:
                    content = json.load(f)
                    id = content["id"]
                    self.actions_sequences[id] = []
                    for action in content['run']:
                        self.actions_sequences[id].append(
                            self.creer_action(action)
                        )
            except Exception:
                continue
                
    def creer_action (self, data: dict):
        if data["type"] == "dialogue":
            return Dialogue(data)

    def tirer_action (self, chance, chance_negative):
        evenement = random()*100 <= chance
        if evenement:
            positive_part = ((chance-chance_negative)/0.75)+chance_negative
            rand = random()*100
            if rand <= chance_negative:
                pass
                #index = randint(0, len(self.evenements_negatifs))
                #key = self.evenements_negatifs[index]
                #return self.actions[key]
            if rand >= positive_part:
                pass
                #index = randint(0, len(self.evenements_positifs))
                #key = self.evenements_positifs[index]
                #return self.actions[key]
            else:
                pass
                #index = randint(0, len(self.evenements_positifs))
                #key = self.evenements_positifs[index]
                #return self.actions[key]
        else:
            return None