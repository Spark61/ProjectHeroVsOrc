import pygame


class Level2:
    def __init__(self, screen, hero, chestGroup, orcGroup):
        self.screen = screen
        self.hero = hero
        self.chestGroup = chestGroup
        self.orcGroup = orcGroup

        # textures
        self.bg_img = pygame.image.load("img/background_A.png")
        self.orc = pygame.image.load("img/orc.png")

        self.bg_width = self.bg_img.get_width()
        self.bg_index = 0
        self.scroll = True

    def update(self):
        scroll_step = 1

        if self.scroll:
            for chest in self.chestGroup:
                chest.rect.x -= scroll_step
                print(chest.rect.x)

                if chest.rect.x <= -chest.image.get_width():
                    self.chestGroup.remove(chest)

            for orc in self.orcGroup:
                if not orc.fight:
                    orc.calc_x -= scroll_step * 2

            self.bg_index += scroll_step

            print(self.bg_index)

            if self.bg_index >= self.bg_width * 4:
                self.scroll = False

            self.screen.blit(self.bg_img, (-(self.bg_index % self.bg_width), -75))
        else:
            self.screen.blit(self.bg_img, (-10, -75))
