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
Surface
- regular surfaces (rendered e.g. images (text is essentially image too!)) -> display surface -> players' eyes! :D
- Texts = font (size and style) -> write on surface -> bilt the surface
"""
# image
planet_surface = pygame.image.load("media/purple_planet.jpg").convert()
planet_surface = pygame.transform.smoothscale(planet_surface, screen.get_size())

ground_surface = pygame.image.load("media/grey_ground.png").convert()
ground_surface = pygame.transform.scale(ground_surface, (size_x, 100))

# text
text_surface = score_font.render("start adventure!", True, "White")

"""
Rectangle
- can be placed more precisely than surface
- useful for detecting collisions
"""
character_surface = pygame.image.load("media/swordwoman.png").convert_alpha()  # run faster than basic convert
character_surface = pygame.transform.scale(character_surface, (80, 70.4))

skeleton_surface = pygame.image.load("media/skeleton.png").convert_alpha()
skeleton_surface = pygame.transform.scale(skeleton_surface, (60, 50.4))

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
    screen.blit(skeleton_surface, (size_x-100,size_y-130))
    
    pygame.display.update()  # -> would keep the window forever open if wo the above block
    clock.tick(60)  # set max 60 loops per sec

