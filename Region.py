class Region:
    def __init__ (self, nom, description):
        self.nom = nom
        self.description = description
        
    def __str__(self):
        return f"Region {self.nom} : {self.description}"
    