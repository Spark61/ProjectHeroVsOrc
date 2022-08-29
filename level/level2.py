import pygame


class Level2:
    def __init__(self, screen):
        self.screen = screen

        # textures
        self.bg_img = pygame.image.load("img/background_A.png")
        self.orc = pygame.image.load("img/orc.png")

    def update(self):
        self.screen.blit(self.bg_img, (-10, -75))
