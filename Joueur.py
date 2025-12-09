class Joueur:

    def __init__ (self, jeu, json):
        if json is not None:
            self.vie_max = json["max_vie"]
            self.vie = json["vie"]
            self.inventaire = json["inventaire"]
            self.equipment = json["equipment"]
        else:
            self.vie_max = 100
            self.vie = 100
            self.inventaire = {}
            self.equipment = {
                "main": None,
                "main_secondaire": None,
                "tete": None,
                "torse": None,
                "jambes": None,
                "pieds": None
            }
        
    def save (self):
        return self.__dict__
    
    def infliger (self, degats):
        self.json["vie"] -= degats
        
    def soigner (self, points):
        self.json["vie"] += points
        if self.json["vie"] > self.json["max_vie"]:
            self.json["vie"] = self.json["max_vie"]
            
    def ajouter_objet (self, objet, quantite = 1):
        if objet in self.inventaire:
            self.inventaire[objet] += quantite
        else:
            self.inventaire[objet] = quantite
            
    def retirer_objet (self, objet, quantite = 1):
        if objet in self.inventaire:
            self.inventaire[objet] -= quantite
            if self.inventaire[objet] <= 0:
                del self.inventaire[objet]
        