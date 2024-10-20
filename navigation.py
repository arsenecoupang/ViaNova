import pygame
import pygame
from car import Car
from detect import detect_collision, detect_nearby_car
from road import draw_road
from config import cars

# 초기화
pygame.init()

# 화면 설정
screen_width, screen_height = 600, 300
screen = pygame.display.set_mode((screen_width, screen_height))

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 초기화
    screen.fill((255, 255, 255))

    # 도로 그리

pygame.quit()