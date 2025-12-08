class Joueur:

    def __init__ (self, jeu, json):
        self.json = json
        self.inventaire = json["inventaire"] or {}
        # TODO: mettre les attributs json dans la classe
        # 
    
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
        