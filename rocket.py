import pygame

class RocketBase():
    def __init__(self, rocket_type, fuel_type, oxidiser, fuel_oxi_ratio):
        # thruster variables
        self.fuel_mass = 500
        self.fuel_type = fuel_type
        self.oxidiser = oxidiser
        self.fuel_oxi_ratio = fuel_oxi_ratio
        self.thrust = 0
        self.mass = 1000

        # movement variables
        self.pos_x = 900 #change to looser opt eventually
        self.pos_y = 500 #change to looser opt eventually
        self.velocity = 0
        self.acceleration = 0

        #images - preloads image from images dir and adds it to transform var and renders
        self.image = pygame.image.load("rocket_1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))

        self.thrusting = True
        

    def update(self, dt, physics_engine): # global physics updater v2
        # hours spent on this: idk like 2.5 (way too long imo)
        forces = physics_engine.calculate_forces(self) # calls physics engine code to calculate forces
        # okay physics nerds will remember F=ma (big guy's second law)
        # this then means that F=ma can be rewritten as a = F/m
        # acceleration is then used to well, accelerate
        # the forces['net'] is just the total force added, hence the term 'net'
        self.acceleration = forces["net"] / self.mass

        # this is just velocity, not much to explain apart from dt meaning deltatime
        # delta timing is a good thing to use to keep framerates the same
        # this is why it's forced to be 60 in main.py as 60 fps is a standard
        self.velocity += self.acceleration * dt
        self.pos_y -= self.velocity * dt # since pygame has y being at the top of screen, we subtract to go down
        self.rect.center = (self.pos_x, self.pos_y) # this just draws the image, not special

    def draw(self, surface): # draw function to update position of rocket
        surface.blit(self.image, self.rect)
