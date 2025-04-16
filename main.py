import pygame
from physics import PhysicsLibrary
from rocket import RocketBase

#make crash variable to quit game if game crashes
game_end = False
(width, height) = (1800, 1000)
screen = pygame.display.set_mode((width,height))

#flip must happen before screen effects take place
# put screen mods INSIDE this comment
background_colour = (255, 255, 255)
screen.fill(background_colour)
clock = pygame.time.Clock() # sets FPS to 60, the "t" of suvat from phys obj
phys = PhysicsLibrary(0,0,0,0,clock)
rocket_1 = RocketBase(900, 500)
# place screen mods above here

pygame.display.flip()

while not game_end:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    rocket_1.draw(screen)
    pygame.display.flip()

pygame.quit()
