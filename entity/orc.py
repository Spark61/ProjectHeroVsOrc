import pygame
import pygame.sprite
from pygame.sprite import Sprite


class Orc(Sprite):
    def __init__(self, screen, x, y):
        Sprite.__init__(self)

        self.screen = screen

        self.left_image = pygame.image.load("img/orc.png").convert_alpha()
        self.left_image = pygame.transform.scale2x(self.left_image)

        self.right_image = pygame.transform.flip(self.left_image, True, False)

        self.image = self.left_image

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.calc_x = self.rect.x

        self.step = 1
        self.step_distance_x = 5
        self.direction = True
        self.direction_x = 0
        self.max_step = 100

        self.fight = False
        self.fight_counter = 0

    def fighting(self, fight):
        self.last_direction = self.direction_x
        self.fight = fight

        if self.fight:
            self.direction_x = 0

    def update_position(self):
        if self.direction:
            self.step += self.step_distance_x
            self.calc_x += self.step_distance_x

            if self.step >= self.max_step:
                self.direction = not self.direction
        else:
            self.step -= self.step_distance_x
            self.calc_x -= self.step_distance_x

            if self.step <= 0:
                self.direction = not self.direction

        if self.direction:
            self.image = self.right_image
        else:
            self.image = self.left_image

        self.rect.x = self.calc_x

    def update(self):
        if self.fight:
            if self.fight_counter % 9 > 0:
                self.rect.x += self.step_distance_x
            elif self.fight_counter % 9 == 0:
                self.rect.x -= (8 * self.step_distance_x)
            self.fight_counter += 1

        else:
            self.update_position()
