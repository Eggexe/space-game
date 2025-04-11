import pygame
from physics import PhysicsLibrary

phys = PhysicsLibrary(0,0,0,0,0)

#make crash variable to quit game if game crashes
game_end = False
(width, height) = (1800, 1000)
screen = pygame.display.set_mode((width,height))

#flip must happen before screen effects take place
# put screen mods INSIDE this comment
background_colour = (255, 255, 255)
screen.fill(background_colour)
# place screen mods above here
pygame.display.flip()

while not game_end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = True
