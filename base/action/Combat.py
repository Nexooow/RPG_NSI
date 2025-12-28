import pygame
import random
from lib.render import text_render_centered, text_render_centered_left
from .Action import Action

parrysound = pygame.mixer.Sound("assets/sounds/parry.mp3")
parrysound.set_volume(0.05)

class Combat(Action):
    """
    Combat au tour par tour.
    """

    def __init__(self, jeu, data):
        super().__init__(jeu, data)
        self.desactive_ui = True
        self.windows = []
        self.frame = 0
        self.turn = "player"  # player/enemy
        self.statut = "selection"  # selection/attack/victory/game_over
        self.option_choisie = 0
        self.ap = 3

        ennemi_data = data["enemy"]
        self.ennemi = {
            "vie_max": ennemi_data["vie"],
            "vie": ennemi_data["vie"],
            "nom": ennemi_data["nom"],
            "actions": ennemi_data.get("actions", [])
        }

    def executer(self):
        super().executer()
        vie_max = self.jeu.joueur.vie_max
        self.player = {
            "vie": self.jeu.joueur.vie,
            "vie_max": vie_max
        }
        self.jeu.fade = 300
        if "music" in self.data:
            pygame.mixer.music.load(self.data["music"])
            pygame.mixer.music.play(-1)

    def charger_attaque_ennemi(self):
        if not self.ennemi["actions"]:
            self.turn = "player"
            self.statut = "selection"
            return

        action = random.choice(self.ennemi["actions"])
        self.windows = []
        start_frame = self.frame + 60  # Délai avant le début de l'attaque

        if action["type"] == "attaque":
            for window in action.get("windows", []):
                # w: {dmg: int, delay: int, duration: int}
                window_start = start_frame + window.get("delay", 0)
                window_end = window_start + window.get("duration", 30)
                self.windows.append({
                    "dmg": window.get("dmg", 10),
                    "start": window_start,
                    "end": window_end,
                })

        self.turn = "enemy"
        self.statut = "attack"

    def update(self, events):
        self.frame += 1

        if self.statut == "selection" and self.turn == "player":

            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.option_choisie = (self.option_choisie - 1) % 3
                    elif event.key == pygame.K_DOWN:
                        self.option_choisie = (self.option_choisie + 1) % 3
                    elif event.key == pygame.K_SPACE:
                        self.executer_choix_joueur()

        elif self.statut == "attack" and self.turn == "enemy":

            for window in self.windows:
                if self.frame >= window["end"]:
                    self.player["vie"] -= window["dmg"]
                    self.windows.remove(window)

            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    for window in self.windows:
                        if window["start"] <= self.frame < window["end"]:
                            parrysound.play()
                            self.windows.remove(window)

            if self.windows == []:
                self.turn = "player"
                self.statut = "selection"

        if self.ennemi["vie"] <= 0:
            self.statut = "victory"
        elif self.player["vie"] <= 0:
            self.statut = "game_over"

        if self.statut in ["victory", "game_over"]:
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.complete = True

    def executer_choix_joueur(self):
        if self.option_choisie == 0:  # Attaque de base
            degats = self.jeu.joueur.force
            self.ennemi["vie"] -= degats
            self.ap += 1
        elif self.option_choisie == 1:  # Capacités
            pass
        elif self.option_choisie == 2:  # Objets
            pass
        self.charger_attaque_ennemi()

    def draw_qte(self):
        # dessiner qte
        pass

    def draw_ui(self):

        # fond temp pour tests
        pygame.draw.rect(self.jeu.fond, (0, 0, 255), (0, 0, self.jeu.WIDTH, self.jeu.HEIGHT))

        # ennemi
        ennemi_health_ratio = max(0, self.ennemi["vie"] / self.ennemi["vie_max"])
        text_render_centered(self.jeu.ui_surface, self.ennemi["nom"], "regular", (255, 255, 255), (self.jeu.WIDTH / 2, 16), False, 16)
        pygame.draw.rect(self.jeu.ui_surface, (255, 255, 255), (9, 6 + 20, self.jeu.WIDTH - 18, 8))
        pygame.draw.rect(self.jeu.ui_surface, (0, 0, 0), (12, 7 + 20, self.jeu.WIDTH - 24, 6))
        pygame.draw.rect(self.jeu.ui_surface, (179, 32, 21), (12, 7 + 20, (self.jeu.WIDTH - 24) * ennemi_health_ratio, 6))

        # barre de vie
        player_health_ratio = max(0, self.player["vie"] / self.player["vie_max"])
        pygame.draw.rect(self.jeu.ui_surface, (0, 0, 0, 150), (9, 525, self.jeu.WIDTH - 9 * 2, 175 - 9))

        text_render_centered_left(self.jeu.ui_surface, f"HP: {self.player['vie']}/{self.player['vie_max']}", "regular", (255, 255, 255), (20, 540), False, 20)
        pygame.draw.rect(self.jeu.ui_surface, (255, 255, 255), (20, 560, 200, 10))
        pygame.draw.rect(self.jeu.ui_surface, (0, 0, 0), (22, 562, 196, 6))
        pygame.draw.rect(self.jeu.ui_surface, (46, 204, 113), (22, 562, 196 * player_health_ratio, 6))

        # AP
        text_render_centered_left(self.jeu.ui_surface, f"AP: {self.ap}/8", "regular", (255, 255, 0), (20, 590), False, 20)

        # Menu de sélection
        if self.statut == "selection" and self.turn == "player":

            options = ["Attaque de base", "Capacités", "Objets"]
            for i, opt in enumerate(options):
                color = (255, 255, 255) if i == self.option_choisie else (150, 150, 150)
                text_render_centered_left(self.jeu.ui_surface, opt, "regular", color, (300, 540 + i * 30), i == self.option_choisie, 24)

        elif self.statut == "attack" and self.turn == "enemy":

            self.draw_qte()

        if self.statut == "victory":

            text_render_centered(self.jeu.ui_surface, "VICTOIRE !", "bold", (255, 255, 0), (self.jeu.WIDTH / 2, self.jeu.HEIGHT / 2), False, 64)

        elif self.statut == "game_over":

            text_render_centered(self.jeu.ui_surface, "DEFAITE...", "bold", (255, 0, 0), (self.jeu.WIDTH / 2, self.jeu.HEIGHT / 2), False, 64)

    def draw(self):
        self.draw_ui()
