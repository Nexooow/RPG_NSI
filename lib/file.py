class File:

    def __init__ (self, content = []):
        self.contenu = content

    def defiler (self):
        return self.contenu.pop(0)
    
    def enfiler (self, valeur):
        self.contenu.append(valeur)

    def sommet (self):
        return self.contenu[0]
    
    def est_vide (self):
        return len(self.contenu) == 0