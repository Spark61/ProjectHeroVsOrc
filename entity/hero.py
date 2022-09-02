import pygame
import pygame.sprite
from pygame.sprite import Sprite


class Hero(Sprite):
    def __init__(self, screen):
        Sprite.__init__(self)

        self.screen = screen

        self.full_image = pygame.image.load("img/hero.png").convert_alpha()

        self.max_walk_animation_index = 12
        self.walk_animation_index = 0

        self.img_left = []
        self.img_right = []

        for i in range(self.max_walk_animation_index):
            image = self.full_image.subsurface(i * 32, 0, 32, 32)
            image = pygame.transform.scale2x(image)

            self.img_right.append(image)

            image = pygame.transform.flip(image, True, False)

            self.img_left.append(image)

        self.image = self.img_right[self.walk_animation_index]
        self.rect = self.image.get_rect()
        self.rect.center = (100, 510)

        self.direction = 0
        self.last_direction = self.direction
        self.step_distance_x = 5
        self.calc_x = self.rect.x
        self.score = 0

        self.fight = False
        self.fight_counter = 0

    def fighting(self, fight):
        self.fight = fight

        if self.fight:
            self.fight_counter += 1

    def get_fighting(self):
        if self.fight:
            return 1
        else:
            return self.fight_counter

    def add_score(self, emeralds):
        self.score += emeralds

    def walk(self, direction):
        self.last_direction = self.direction
        self.direction = direction

    def update_position(self):
        self.calc_x += self.step_distance_x * self.direction

        image_pos = self.screen.get_width() - self.image.get_width()

        if self.calc_x < 0:
            self.calc_x = 0
        elif self.calc_x > image_pos:
            self.calc_x = image_pos

        self.rect.x = self.calc_x

    def update_image(self, direction):
        if -0.1 < direction < 0.1:
            self.walk_animation_index = 0
        else:
            self.walk_animation_index += 1

            if self.walk_animation_index >= self.max_walk_animation_index:
                self.walk_animation_index = 0

        if direction < 0:
            self.image = self.img_left[self.walk_animation_index]
        else:
            self.image = self.img_right[self.walk_animation_index]

    def update(self):
        if self.fight:
            self.fight_counter += 1
            self.update_image(self.last_direction)

            print(self.fight_counter, 2 * len(self.img_left), self.walk_animation_index)
            if self.fight_counter >= 2 * len(self.img_left) and self.walk_animation_index == 0:
                self.fight = False
                self.fight_counter = -1
        else:
            self.fight_counter = 0
            self.update_position()
            self.update_image(self.direction)
