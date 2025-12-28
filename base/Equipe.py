class Equipe:

    def __init__ (self, json = None):
        if json is not None:
            self.personnages = json["personnages"] # TODO: charger les personnages selon le json