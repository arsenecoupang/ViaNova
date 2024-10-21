import pygame
import autoMoving.car

from autoMoving.noChanges.road import draw_road

pygame.init()

# 화면 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))

    # 도로 그리기
    draw_road(screen)
    for car in cars:
        car.update()
        car.drawcar(screen)
        car.drawradar(screen)  # 자율주행차만 레이더 표시
    pygame.display.flip()

    clock.tick(60)

pygame.quit()