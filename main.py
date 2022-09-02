import random

import pygame
from pygame import mixer

from entity.chest import Chest
from entity.hero import Hero
from entity.orc import Orc
from level.level1 import Level1
from level.level2 import Level2

clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Starting the mixer
mixer.init()

# Loading & playing the song
mixer.music.load("smd/Messersmith.mp3")

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hero Vs Orc")

# hero
hero = Hero(screen)
heroGroup = pygame.sprite.GroupSingle()
heroGroup.add(hero)

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

# orc
orc = Orc(screen, 600, 510)
orcGroup = pygame.sprite.Group()
orcGroup.add(orc)

# chest
chestGroup = pygame.sprite.Group()

for i in range(5):
    chest = Chest(screen, random.randint(80 * i, 80 * (i + 1)))
    chestGroup.add(chest)

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
level = 2

level1 = Level1(screen)
level2 = Level2(screen, hero, chestGroup, orcGroup)

game_running = True

chest_tick_spawn = 0
max_chest_tick_spawn = 60

orc_tick_spawn = 0
max_orc_tick_spawn = 60

while game_running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                hero.walk(-1)
            elif event.key == pygame.K_d:
                hero.walk(1)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                hero.walk(-0.000000000000001)
            elif event.key == pygame.K_d:
                hero.walk(0)
            elif event.key == pygame.K_e:
                for chest in chestGroup:
                    if hero.rect.colliderect(chest.rect):
                        chest.open(hero)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouseDown = True
                mousePos = pygame.mouse.get_pos()

                for i in range(len(button_infolist)):
                    (x, y, width, height, active) = button_infolist[i]
                    imgrect = pygame.Rect(x, y, width, height)
                    if imgrect.collidepoint(mousePos):
                        button_infolist[i] = [x, y, width, height, not active]

                        match i:
                            case 0:
                                mixer.music.play()
                            case 1:
                                mixer.music.pause()
                            case 2:
                                mixer.music.unpause()
                            case 3:
                                pass
                            case 4:
                                mixer.music.set_volume(0.5)
                            case 5:
                                mixer.music.set_volume(1)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouseDown = False

    if level == 1:
        level1.update()
    else:
        level2.update()

    for i in range(len(button_infolist)):
        (x, y, width, height, active) = button_infolist[i]

        if active:
            image = img_list_active[i]
        else:
            image = img_list_passive[i]

        # screen.blit(image, (x, y))

    if hero.get_fighting() < 0:
        pygame.sprite.spritecollide(hero, orcGroup, True)
        hero.add_score(random.randint(1, 5))

    if pygame.sprite.spritecollide(hero, orcGroup, False):
        hero.fighting(True)

        for orc in orcGroup:
            if orc.rect.colliderect(hero.rect):
                orc.fighting(True)

    chest_tick_spawn += 1
    orc_tick_spawn += 1

    if chest_tick_spawn % max_chest_tick_spawn == 0:
        if len(chestGroup) < random.randint(0, 2):
            max_chest_tick_spawn += 60

            chestGroup.add(Chest(screen, (screen.get_width())))
    if orc_tick_spawn % max_orc_tick_spawn == 0:
        if len(chestGroup) < random.randint(0, 3):
            orcGroup.add(Orc(screen, (screen.get_width()), 510))

    chestGroup.update()
    chestGroup.draw(screen)

    heroGroup.update()
    heroGroup.draw(screen)

    orcGroup.update()
    orcGroup.draw(screen)

    text_surface = my_font.render('Score: ' + str(hero.score), False, (0, 0, 0))
    screen.blit(text_surface, (screen.get_width() - text_surface.get_width() - 25, text_surface.get_height()))

    pygame.display.update()

pygame.quit()
