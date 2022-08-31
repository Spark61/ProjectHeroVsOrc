import pygame

from level.level1 import Level1
from level.level2 import Level2

clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hero Vs Orc")

# buttons
rasterX = 225
rasterY = 75
gapX = 5
gapY = 3

buttons = pygame.image.load("img/sound_buttons.png")
buttonReact = pygame.Rect(150, 323, 29, 20)

button_infolist = []
img_list_active = []
img_list_passive = []

anzahl = 0

for j in range(3):
    for i in range(5):
        button = buttons.subsurface(5 + i * rasterX, j * rasterY, rasterX - gapX, rasterY - gapY)

        if anzahl % 2 == 0:
            img_list_active.append(button)
            button_infolist.append([100, anzahl // 2 * 100, button.get_width(), button.get_height(), True])
        else:
            img_list_passive.append(button)

        anzahl += 1

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouseDown = True
                mousePos = pygame.mouse.get_pos()

                for i in range(len(button_infolist)):
                    (x, y, width, height, active) = button_infolist[i]
                    imgrect = pygame.Rect(x, y, width, height)
                    if imgrect.collidepoint(mousePos):
                        button_infolist[i] = [x, y, width, height, not active]

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouseDown = False

    if level == 1:
        #     level1.update()
        pass
    else:
        level2.update()

    for i in range(len(button_infolist)):
        (x, y, width, height, active) = button_infolist[i]

        if active:
            image = img_list_active[i]
        else:
            image = img_list_passive[i]

        screen.blit(image, (x, y))

    pygame.display.update()

pygame.quit()
