import pygame
import requests

from autoMoving.autoMove.detect import detect_collision, detect_nearby_car
from autoMoving.noChanges.road import draw_road
from autoMoving.noChanges.config import autoMoving_car

# 초기화
pygame.init()

# 화면 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 메인 루프
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 지우기
    screen.fill((255, 255, 255))

    # 도로 그리기
    draw_road(screen)

    # 자동차 움직임 업데이트 및 그리기
    for car in autoMoving_car:
        car.update()
        car.drawcar(screen)
        car.drawradar(screen)  # 자율주행차만 레이더 표시

    # 모든 자율주행차에 대해 충돌 및 거리/방향 감지
    for car in autoMoving_car:
        if car.is_autonomous:
            collision_status, collision_distance = detect_collision(car, [c for c in autoMoving_car if c != car])
            car.nearest_distance, car.direction_to_nearest, car.car_up, car.car_down, car.car_left, car.car_right = detect_nearby_car(
                car, [c for c in autoMoving_car if c != car])
            headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}
            if collision_status:
                print('충돌 발생!')
            elif car.nearest_distance:
                requests.post('http://localhost:5000/update', data={'message': f"{car.nearest_distance:.2f}m에 {car.direction_to_nearest}에 차량이 있습니다."})
            else:
                requests.post('http://localhost:5000/update', data={'message': "안전합니다!"}, headers=headers)

    # 화면 업데이트
    pygame.display.flip()
    # 프레임 속도 제어
    clock.tick(60)

pygame.quit()