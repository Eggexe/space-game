import pygame
from physics import PhysicsLibrary
from rocket import RocketBase

# whoopsie variable in case something breaks and i need to crash early to close
game_end = False

# window config
(width, height) = (1800, 1000)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rocket Simulation")

# clock
clock = pygame.time.Clock()

# instantiate physics lib
phys = PhysicsLibrary()
rocket_1 = RocketBase(0,0,0,0)

# screen colour, can change later to a blue for sky
background_colour = (255, 255, 255)
screen.fill(background_colour)
pygame.display.flip()

# game loop
while not game_end:
    dt = clock.tick(60) / 1000  # delta time in seconds

    # event pygame handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = True

    # make screen look nice
    screen.fill(background_colour)

    # update and draw rocket position with dt and physics lib
    rocket_1.update(dt, phys)
    rocket_1.draw(screen)

    # update display
    pygame.display.flip()

pygame.quit()
