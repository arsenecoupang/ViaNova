import pygame

from detect import window_height, window_width

pygame.init()
running = True
# 화면 크기 설정
window_height = 600
window_width = 800

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Car Movement')

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.display.update()



