import pygame


class Level1:
    def __init__(self, screen):
        self.screen = screen

        # textures
        self.heroAnimationPosition = 0
        self.bg_img = pygame.image.load("img/bg.png")
        self.orc = pygame.image.load("img/orc.png")
        self.hero = pygame.image.load("img/hero.png")

    def update(self):
        self.screen.blit(self.bg_img, (-10, -75))

        self.heroAnimationPosition += 1
        if self.heroAnimationPosition >= 12:
            self.heroAnimationPosition = 0
        print(self.heroAnimationPosition)
        self.screen.blit(self.orc, (500, 515))
        self.screen.blit(self.hero, (400, 515),
                         (self.heroAnimationPosition * 32, 0, 32, 32))
