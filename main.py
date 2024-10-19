import pygame
pygame.init()
running = True
# 화면 크기 설정
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Car Movement')

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.display.update()



