from .Action import Action

class Damage(Action):
    """
    Inflige des dégâts au joueur.
    """

    def __init__(self, jeu, data):
        super().__init__(jeu, data)

    def executer(self):
        super().executer()
        self.jeu.joueur.infliger(self.data.get("degats", 0))
        self.complete = True
