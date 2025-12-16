import pygame
from Action import Action

from demiurge import Fighter
pygame.init()
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
warrior_size = 162
warrior_scale = 4
warrior_offset = [72, 56]
warrior_data = [warrior_size, warrior_scale, warrior_offset]
demiurge_size = 250
demiurge_scale = 3
demiurge_offset = [112, 107]
demiurge_data = [demiurge_size, demiurge_scale, demiurge_offset]
bg = pygame.image.load("images.jpg").convert_alpha()
bg = pygame.transform.scale(bg, (screen_width, screen_height))
warrior_sheet = pygame.image.load(
    "./brawler_images/images/warrior/Sprites/warrior.png").convert_alpha()
demiurge_sheet = pygame.image.load(
    "./brawler_images/images/wizard/Sprites/wizard.png").convert_alpha()
warrior_animation_steps = [10, 8, 1, 7, 7, 3, 7]
demiurge_animation_steps = [8, 8, 1, 8, 8, 3, 7]


class StreetFighter (Action):

    def __init__(self, jeu):
        self.jeu = jeu
        self.desactive_ui = True
        self.demiurge = Fighter(200, 310, demiurge_data, demiurge_sheet,
                                demiurge_animation_steps)
        self.player = Fighter(700, 310, warrior_data, warrior_sheet,
                              warrior_animation_steps)
        pass

    def draw_bg(self):
        background = pygame.image.load("images.jpg").convert_alpha()
        background = pygame.transform.scale(background, 100)
        self.jeu.fond.blit(background, (0, 0))

    def draw_health(self, health, x, y):
        ratio = health/100
        pygame.draw.rect(self.jeu.ui_surface, WHITE, (x-2, y-2, 404, 34))
        pygame.draw.rect(self.jeu.ui_surface, RED, (x, y, 400, 30))
        pygame.draw.rect(self.jeu.ui_surface, YELLOW, (x, y, 400*ratio, 30))

    def draw(self):
        self.draw_bg()
        self.draw_health(screen, self.player.health, 20, 20)
        self.draw_health(screen, self.demiurge.health, 500, 20)
        self.demiurge.draw(screen)

    def update(self):
        self.player.move(screen_width, screen_height, screen, self.demiurge)
        self.demiurge.move(screen_width, screen_height, screen, self.player, False)
        self.demiurge.ai_behavior(screen, self.player)
        

running = True
while running:
    clock.tick(60)
    draw_bg()
    draw_health(screen, player.health, 20, 20)
    draw_health(screen, demiurge.health, 500, 20)
    demiurge.draw(screen)
    player.update()
    demiurge.update()
    player.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()
