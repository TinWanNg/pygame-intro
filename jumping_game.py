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
- can be placed via (topleft, midbottom, etc.) compareed to plain number
- useful for detecting collisions
- use rectangle.left, for e.g., to measure its x position
"""
ground_y = size_y-100
object_y = ground_y-30

character_surface = pygame.image.load("media/swordwoman.png").convert_alpha()  # run faster than basic convert
character_surface = pygame.transform.scale(character_surface, (80, 70.4))
character_rect = character_surface.get_rect(topleft=(100, object_y))  # get_rect for generating the eaxct same size as the surface

skeleton_surface = pygame.image.load("media/skeleton.png").convert_alpha()
skeleton_surface = pygame.transform.scale(skeleton_surface, (60, 50.4))
sekleton_rect = skeleton_surface.get_rect(topleft=(size_x, object_y))

while True:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    
    # static surfaces
    screen.blit(planet_surface, (0,0))
    screen.blit(ground_surface, (0,ground_y))
    screen.blit(text_surface, (25,25))
    # moving surfaces
    screen.blit(character_surface, character_rect)
    screen.blit(skeleton_surface, sekleton_rect)
    
    sekleton_rect.left -= 3
    if sekleton_rect.left <= 0: sekleton_rect.left = size_x
    
    
    pygame.display.update()  # -> would keep the window forever open if wo the above block
    clock.tick(60)  # set max 60 loops per sec

