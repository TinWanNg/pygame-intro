import pygame
from sys import exit

# basic setups
pygame.init()
size_x, size_y = 810, 348
size = (size_x, size_y)  # (x, y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("(`･Θ･´)")
score_font = pygame.font.Font(None, 25)

clock = pygame.time.Clock()  # control fps -- too much would break, while too less makes it looks unnatural

"""
Surfaces
- regular surfaces (rendered e.g. images (text is essentially image too!)) -> display surface -> players' eyes! :D
- Texts = font (size and style) -> write on surface -> bilt the surface
"""
# image
planet_surface = pygame.image.load("/Users/tinwanng/Dev-personal/pygame-intro/purple_planet.jpg").convert()
planet_surface = pygame.transform.smoothscale(planet_surface, screen.get_size())

ground_surface = pygame.image.load("/Users/tinwanng/Dev-personal/pygame-intro/grey_ground.png").convert()
ground_surface = pygame.transform.scale(ground_surface, (size_x, 100))

character_surface = pygame.image.load("/Users/tinwanng/Dev-personal/pygame-intro/swordwoman.png").convert_alpha()
character_surface = pygame.transform.scale(character_surface, (80, 70.4))

# text
text_surface = score_font.render("start adventure!", True, "White")




character_position_x = 0


while True:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(planet_surface, (0,0))
    screen.blit(ground_surface, (0,size_y-100))
    screen.blit(text_surface, (25,25))

    if character_position_x >= size_x:
        character_position_x = 0
    else:
        character_position_x += 3.5
    screen.blit(character_surface, (character_position_x,size_y-130))
    
    pygame.display.update()  # -> would keep the window forever open if wo the above block
    clock.tick(60)  # set max 60 loops per sec

