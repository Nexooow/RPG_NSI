from .Dialogue import Dialogue

class Deplacement(Dialogue):
    """
    Change le lieu et la région du joueur.
    """

    def __init__(self, jeu, data):
        data["lines"] = [f"Vous arrivez à {data['lieu']} dans la région {data['region']}."]
        super().__init__(jeu, data)

    def executer(self):
        super().executer()
        self.jeu.region = self.data["region"]
        self.jeu.lieu = self.data["lieu"]
