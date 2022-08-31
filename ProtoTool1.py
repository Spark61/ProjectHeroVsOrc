import pygame

clock = pygame.time.Clock()

positions = [[15, 5, 32, 32], [12, 38, 32, 32], [13, 71, 32, 32], [12, 421, 32, 32], [132, 5, 32, 33], [257, 5, 32, 32]]

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hero Vs Orc")

buttons = pygame.image.load("img/basic-icon-set.png")
buttonReact = pygame.Rect(150, 323, 29, 20)

button_infolist = []
img_list_active = []
img_list_passive = []

anzahl = 0

for position in positions:
    button = buttons.subsurface(position)

    img_list_active.append(button)
    button_infolist.append([anzahl * 50, 50, button.get_width(), button.get_height(), True])

    anzahl += 1

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

                for position in button_infolist:
                    x, y, width, height, active = position
                    rect = pygame.Rect(x, y, width, height)

                    if rect.collidepoint(mousePos):
                        print("click")
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouseDown = False

    screen.fill((0, 0, 0))
    screen.fill((255, 255, 255), (0, 44, 300, 45))

    for i in range(len(button_infolist)):
        (x, y, width, height, active) = button_infolist[i]

        if active:
            image = img_list_active[i]
        else:
            image = img_list_passive[i]

        screen.blit(image, (x, y))

    pygame.display.update()

pygame.quit()
