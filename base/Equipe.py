from base.Personnage import Personnage


class Equipe:

    def __init__ (self, jeu):
        self.jeu = jeu
        self.argent = 100
        self.chance = 10
        self.personnages: list[Personnage] = [] # liste des personnages dans l'équipe (c.-à-d. débloqués)
        self.inventaire = {}

    def get_personnage (self, nom) -> Personnage | None:
        for personnage in self.personnages:
            if personnage.nom == nom:
                return personnage
        return None

    def personnage_debloque (self, nom) -> bool:
        personnage = self.get_personnage(nom)
        return personnage is not None

    def ajouter_personnage (self, personnage):
        self.personnages.append(personnage)

    def equiper_personnage (self, nom, item_id):
        if item_id in self.inventaire:
            personnage = self.get_personnage(nom)
            if personnage:
                personnage.equiper(item_id)

    def restaurer (self, json):
        self.argent = json["argent"]
        self.chance = json["chance"]
        self.inventaire = json["inventaire"]
        for personnage in json["personnages"]:
            # TODO: charger les personnages selon le json indiqué
            pass

    def sauvegarder (self):
        return {
            "argent": self.argent,
            "chance": self.chance,
            "inventaire": self.inventaire,
            "personnages": [] # TODO: sauvegarder les personnages
        }

    def infliger (self, degats):
        for personnage in self.personnages:
            personnage.infliger(degats)

    def soigner (self, points):
        for personnage in self.personnages:
            personnage.soigner(points)
