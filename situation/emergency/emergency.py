import pygame
import autoMoving.car
from autoMoving.noChanges.config import emergency_car
from situation.emergency.autoMove.detect import detect_nearby_car
from autoMoving.noChanges.road import draw_road
from situation.emergency.autoMove.carMove_auto import network_message, move_normal

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
    for car in emergency_car:
        car.update()
        car.drawcar(screen)
        car.drawradar(screen)  # 자율주행차만 레이더 표시
    for car in emergency_car:
        if car.is_emergency:
            nearby_car = detect_nearby_car(car, [c for c in emergency_car if c != car])
            if nearby_car:
                nearby_car.set_network_message("emergency_coming")
                move_normal(nearby_car)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()