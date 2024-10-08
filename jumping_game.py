import pygame
from sys import exit

"""
1. Control animation frames/second via clock:
too much would break, while too less makes it looks unnatural

2. Surfaces
- regular surfaces (rendered e.g. images (text is essentially image too!)) -> display surface -> players' eyes! :D
- Texts = font (size and style) -> write on surface -> bilt the surface
"""

pygame.init()
size = (810, 348)  # (x, y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mirach and Ngan's adventure (`･Θ･´)")
clock = pygame.time.Clock()
score_font = pygame.font.Font(None, 25)


# display_surface = pygame.Surface(size)
# display_surface.fill((152,212,230))
planet_surface = pygame.image.load("/Users/tinwanng/Dev-personal/pygame-intro/purple_planet.jpg").convert()
planet_surface = pygame.transform.smoothscale(planet_surface, screen.get_size())

ground_surface = pygame.image.load("/Users/tinwanng/Dev-personal/pygame-intro/grey_ground.png")
ground_surface = pygame.transform.scale(ground_surface, (810, 100))

text_surface = score_font.render("start adventure!", True, "White")







while True:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(planet_surface, (0,0))
    screen.blit(ground_surface, (0,size[1]-100))
    screen.blit(text_surface, (25,25))
    
    pygame.display.update()  # -> would keep the window forever open if wo the above block
    clock.tick(60)  # set max 60 loops per sec