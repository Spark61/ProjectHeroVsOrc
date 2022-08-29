import pygame

from level.level1 import Level1
from level.level2 import Level2

clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hero Vs Orc")

# levels
level = 1

level1 = Level1(screen)
level2 = Level2(screen)

game_running = True
while game_running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    if level == 1:
        level1.update()
    else:
        level2.update()

    pygame.display.update()

pygame.quit()
