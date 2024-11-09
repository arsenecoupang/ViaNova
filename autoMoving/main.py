import pygame
import requests

from autoMove.carMove_auto import movingAuto
from autoMove.detect import detect_collision, detect_nearby_car
from noChanges.road import draw_road
from noChanges.config import autoMoving_car as cars
from autoMoving import shared_state
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "600,200"
# 초기화
pygame.init()

# 화면 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 지우기
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
    shared_state.nearest_distance, shared_state.direction_to_nearest, shared_state.car_up, shared_state.car_down, shared_state.car_left, shared_state.car_right = detect_nearby_car(
        cars[0], cars[1:])

    # Debug print statements
    #print(f"nearest_distance: {shared_state.nearest_distance}")
    #print(f"direction_to_nearest: {shared_state.direction_to_nearest}")
    #print(f"car_up: {shared_state.car_up}, car_down: {shared_state.car_down}, car_left: {shared_state.car_left}, car_right: {shared_state.car_right}")

    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}
    # 출력: 충돌 또는 거리/방향 정보 및 각 방향에 차량이 있는지 여부
    if collision_status:
        requests.post('http://127.0.0.1:5000/update', data={'message': "충돌 발생!"}, headers=headers)
    elif shared_state.nearest_distance:
        requests.post('http://127.0.0.1:5000/update', data={'message': f"{shared_state.nearest_distance:.2f}m에 {shared_state.direction_to_nearest}에 차량이 있습니다."})
        #print(f"move_x: {movingAuto('x')}, move_y: {movingAuto('y')}, vel_x: {cars[0].vel[0]}, vel_y: {cars[0].vel[1]}")

        # 각 방향에 차량이 있는지 여부 출력
        print(f"차량 감지 - 위쪽: {shared_state.car_up}, 아래쪽: {shared_state.car_down}, 왼쪽: {shared_state.car_left}, 오른쪽: {shared_state.car_right}")
    else:
        requests.post('http://127.0.0.1:5000/update', data={'message': "안전합니다!"}, headers=headers)
    # 화면 업데이트
    pygame.display.flip()

    # 프레임 속도 제어
    pygame.time.Clock().tick(60)

pygame.quit()