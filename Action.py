import pygame

from lib.render import text_render_centered


class Action:
    def __init__(self, jeu, json={}):
        self.complete = False
        self.jeu = jeu
        self.json = json
        self.desactive_ui = False

    def draw(self):
        pass

    def update(self, events):
        pass

    def executer(self):
        pass

    def get_complete(self):
        return self.complete


class Dialogue(Action):
    def __init__(self, jeu, json):
        super().__init__(jeu, json)
        self.frame_relative = -100  # -100 = "l'action" est en train d'être démarrée, 0 = "l'action" est en cours d'exécution, 100 = "l'action" est terminée

    def draw(self):
        pygame.draw.rect(
            self.jeu.ui_surface,
            (0, 0, 0, 15),
            (0, 675 - (len(self.json["lines"]) * 26), 1000, 650),
        )
        pygame.draw.rect(
            self.jeu.ui_surface,
            (0, 0, 0, 110),
            (0, 675 - (len(self.json["lines"]) * 26), 1000, 1),
        )
        for index, line in enumerate(self.json["lines"]):
            text_render_centered(
                self.jeu.ui_surface,
                line,
                "imregular",
                (0, 0, 0, 255),
                (1000 / 2, 675 - index * 26),
                size=28,
            )

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.complete = True

    def executer(self):
        pass


class Selection(Action):
    def __init__(self, jeu, json):
        super().__init__(jeu, json)
        self.option_choisie = 0

    def draw(self):
        options = self.json["options"]
        for index, choix in enumerate(options):
            text_render_centered(
                self.jeu.ui_surface,
                choix["name"],
                "imregular",
                pos=(1000 / 2, 675 - (26 * index)),
                underline=index == self.option_choisie,
                size=28,
            )
        text_render_centered(
            self.jeu.ui_surface,
            self.json["question"],
            "imregular",
            pos=(1000 / 2, 675 - (26 * len(options) - 1)),
            size=28,
        )

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                if self.option_choisie != len(self.json["options"]) - 1:
                    self.option_choisie += 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                if self.option_choisie != 0:
                    self.option_choisie -= 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.complete = True
                valeur = self.json["options"][self.option_choisie]["valeur"]
                print(self.json["actions"][valeur])

    def executer(self):
        self.option_choisie = 0


class Damage (Action):
    
    def __init__ (self, jeu, json):
        super().__init__(jeu, json)
    
    def executer (self):
        self.jeu.joueur.infliger(self.json["degats"])
        self.complete = True