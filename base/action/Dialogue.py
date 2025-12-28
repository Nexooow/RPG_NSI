import pygame
from lib.render import text_render_centered_left
from .Action import Action

class Dialogue(Action):
    """
    Dialogue.
    """

    def __init__(self, jeu, data):
        super().__init__(jeu, data)

    def draw(self):
        lines = self.data.get("lines", [])
        speaker = self.data.get("speaker", "")

        if not lines:
            self.complete = True

        # hauteur boite
        line_height = 30
        padding = 20
        speaker_height = 35 if speaker else 0
        total_height = len(lines) * line_height + padding * 2 + speaker_height

        # position boite
        box_y = 700 - total_height - 20
        box_width = 960
        box_x = 20

        pygame.draw.rect(
            self.jeu.ui_surface,
            (50, 50, 50),
            (box_x - 3, box_y - 3, box_width + 6, total_height + 6),
        )
        pygame.draw.rect(
            self.jeu.ui_surface, (20, 20, 30), (box_x, box_y, box_width, total_height)
        )

        current_y = box_y + padding
        if speaker:
            text_render_centered_left(
                self.jeu.ui_surface,
                speaker,
                "imitalic",
                color=(255, 200, 100),
                pos=(box_x + padding, current_y),
                size=26,
            )
            current_y += speaker_height

        for line in lines:
            text_render_centered_left(
                self.jeu.ui_surface,
                line,
                "imregular",
                color=(255, 255, 255),
                pos=(box_x + padding, current_y),
                size=24,
            )
            current_y += line_height

        # fleche
        indicator_x = box_x + box_width - 30
        indicator_y = box_y + total_height - 15
        triangle_points = [
            (indicator_x, indicator_y - 5),
            (indicator_x + 10, indicator_y),
            (indicator_x, indicator_y + 5),
        ]
        pygame.draw.polygon(self.jeu.ui_surface, (255, 255, 255), triangle_points)

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.complete = True

    def executer(self):
        super().executer()
