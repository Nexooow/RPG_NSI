from .Action import Action

class AjoutTemps(Action):
    """
    Ajoute du temps au chrono de la région.
    """

    def __init__(self, jeu, data):
        super().__init__(jeu, data)

    def executer(self):
        super().executer()
        self.jeu.region.temps_restant += self.data.get("temps", 0)
        self.complete = True
