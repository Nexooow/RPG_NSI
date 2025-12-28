class Personnage:

    def __init__ (self, equipe, nom):
        self.equipe = equipe
        self.nom = nom

        self.vie_max = 100
        self.vie = 100
        self.force = 10
        self.vitesse = 10
        self.resistance = 0

        self.arme = None

        self.competences_debloques = []
        self.competences = {}

    def restaurer (self, json):
        self.vie = json["vie"]
        self.vie_max = json["vie_max"]
        self.arme = json["arme"]
        self.force = json["force"]
        self.resistance = json["resistance"]
        self.vitesse = json["vitesse"]
        self.competences_debloques = json["competences_debloques"]

    # TODO: système de compétences (avec arbre)
    # TODO: attributs du personnage (force, vitesse, chance, resistance ...)

    def attaquer (self, adversaire):
        pass

    def recevoir (self, degats):
        pass

    def equiper (self, item_id):
        if self.arme:
            ancienne_arme = self.equipe.jeu.loader.items[self.arme]
            # TODO: déséquiper et retirer les bonus de l'arme
            pass
        # TODO: équiper l'arme et ajouter les bonus


    def utiliser (self, item):
        pass

    def infliger (self, degats):
        pass

    def soigner (self, points):
        pass