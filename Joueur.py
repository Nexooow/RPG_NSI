class Joueur:

    def __init__ (self, jeu, json):
        if json is not None:
            self.vie_max = json["vie_max"]
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
        self.vie -= degats
        
    def soigner (self, points):
        self.vie += points
        if self.vie > self.vie_max:
            self.vie = self.vie_max
            
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
        