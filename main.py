# main.py
import pygame
import requests
from car import Car
from detect import detect_collision, detect_nearby_car, detect_radar_in_car
from road import draw_road
from config import cars # Import the function

# 초기화
pygame.init()

# 화면 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 폰트 초기화
font = pygame.font.SysFont('applegothicttf', 36)

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 초기화
    screen.fill((255, 255, 255))

    # 도로 그리기
    draw_road(screen)

    # 자동차 움직임 업데이트 및 그리기
    for car in cars:
        car.update()
        car.drawcar(screen)
        car.drawradar(screen)  # 자율주행차만 레이더 표시

    # 충돌 감지 (첫 번째 자동차 기준)
    collision_status, collision_distance = detect_collision(cars[0], cars[1:])

    # 가까운 차의 거리 및 방향 정보 감지 (레이더 범위 안에 있을 때만)
    nearest_distance, direction_to_nearest, car_up, car_down, car_left, car_right = detect_nearby_car(cars[0], cars[1:])
    radar_in_cars = detect_radar_in_car(cars[0], cars[1:])

    # 출력: 충돌 또는 거리/방향 정보
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}
    if collision_status:
            requests.post('http://localhost:5000/update', data={'message': "충돌 발생!"}, headers=headers)
    elif radar_in_cars:
        for dist, direction in radar_in_cars:
            requests.post('http://localhost:5000/update', data={'message': f"{dist:.2f}m에 {direction}에 차량이 있습니다."}, headers=headers)
    else:
        requests.post('http://localhost:5000/update', data={'message': "감지된 차량 없음"}, headers=headers)

    # 화면 업데이트
    pygame.display.flip()

    # 프레임 속도 제어
    pygame.time.Clock().tick(60)

pygame.quit()