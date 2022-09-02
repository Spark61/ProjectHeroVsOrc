import random

import pygame
import pygame.sprite
from pygame.sprite import Sprite


class Chest(Sprite):
    def __init__(self, screen, x):
        Sprite.__init__(self)

        self.screen = screen

        self.full_image = pygame.image.load("img/chest.png").convert_alpha()
        self.images = []

        for i in range(4):
            image = self.full_image.subsurface(i * 32, 0, 32, 32)
            image = pygame.transform.scale2x(image)

            self.images.append(image)

        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, 510)

        self.animate = False
        self.animation_index = 0
        self.open_animation = (0, 1, 3)

        self.hero = None

    def open(self, hero):
        if self.hero != None:
            return
        self.animate = True
        self.hero = hero

    def update(self):
        if self.animate:
            self.animation_index += 1

            if (self.animation_index // 10) >= len(self.open_animation):
                self.animate = False

                self.hero.add_score(random.randint(1, 10))

        self.image = self.images[self.animation_index // 10]
