import pygame

screen = pygame.display.set_mode((1280, 720)) # fond avec tout ce qui est nécessaire pour le jeu
transparent_surface = pygame.Surface((1280, 720), pygame.SRCALPHA) # fond transparent pour les éléments qui doivent être affichés juste au dessus des éléments principaux
ui_layer = pygame.Surface((1280, 720), pygame.SRCALPHA) # layer pour les éléments de l'interface utilisateur
filter = pygame.Surface((1280, 720), pygame.SRCALPHA) # layer pour les éléments de filtre à l'écran (fade-in, fade-out, etc.)

def font_render (text, font, color=(0, 0, 0), size=None):
    if font == "extrabold":
        font = pygame.font.Font("./assets/fonts/CinzelDecorative-Black.ttf", size or 56)
    elif font == "bold":
        font = pygame.font.Font("./assets/fonts/CinzelDecorative-Bold.ttf", size or 48)
    else:
        font = pygame.font.Font("./assets/fonts/CinzelDecorative-Regular.ttf", size or 36)
    return font.render(text, True, color)
    
def text_render_centered(screen, text, font, color=(0, 0, 0), pos=(0, 0), underline = False, size = None):
    text_surface = font_render(text, font, color, size)
    if underline:
        underline_color = (color[0], color[1], color[2], 120)
        text_largueur, text_hauteur = text_surface.get_size()
        underline_start = (pos[0] - text_largueur / 2, pos[1] + text_hauteur / 2)
        underline_end = (pos[0] + text_largueur / 2, pos[1] + text_hauteur / 2)
        pygame.draw.line(transparent_surface, underline_color, underline_start, underline_end, 2)
    position = text_surface.get_rect(center=pos or (screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text_surface, position)

def text_render (screen, text, font, color=(0, 0, 0), pos=(0, 0), underline = False, size = None):
    text_surface = font_render(text, font, color, size)
    screen.blit(text_surface, pos)
    
def draw_rectangle (topleft, botright, color=(0, 0, 0)):
    """
    Dessine un rectangle sur la surface de rendu.
    Fonction qui remplace pygame.draw.rect (qui utilise un point d'origine puis une taille) pour dessiner plus facilement des rectangles à partir de 2 points.
    """
    x1, y1 = topleft
    x2, y2 = botright
    pygame.draw.rect(transparent_surface, color, [x1, y1, x2-x1, y2-y1])