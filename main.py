import pygame

win_size = 700
win_color = (0, 0, 0)

win = pygame.display.set_mode((win_size, win_size))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(win_color)
    pygame.display.update()