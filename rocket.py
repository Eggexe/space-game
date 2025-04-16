import pygame

class RocketBase():
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

        # add images for rockets here
        self.image = pygame.image.load("rocket_1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 100))
        # end of images
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)
