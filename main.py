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

    # 출력: 충돌 또는 거리/방향 정보 및 각 방향에 차량이 있는지 여부
    if collision_status:
        print(f"충돌 발생!")
    elif shared_state.nearest_distance:
        print(f"전방 {shared_state.nearest_distance:.2f}m에 {shared_state.direction_to_nearest}에 차량이 있습니다.")
        print(f"move_x: {movingAuto('x')}, move_y: {movingAuto('y')}, vel_x: {cars[0].vel[0]}, vel_y: {cars[0].vel[1]}")

        # 각 방향에 차량이 있는지 여부 출력
        print(f"차량 감지 - 위쪽: {shared_state.car_up}, 아래쪽: {shared_state.car_down}, 왼쪽: {shared_state.car_left}, 오른쪽: {shared_state.car_right}")
    else:
        print("감지된 차량 없음")

    # 화면 업데이트
    pygame.display.flip()

    # 프레임 속도 제어
    pygame.time.Clock().tick(60)

pygame.quit()