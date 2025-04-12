import pygame
from physics import PhysicsLibrary

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
# place screen mods above here

rocket_1 = pygame.Rect(200, 100, 150, 100) #

pygame.display.flip()

while not game_end:
    clock.tick(60)

    pygame.draw.rect(screen, (200, 200, 200), rocket_1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
