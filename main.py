# main.py
import pygame
import requests

from autoMove.carMove_auto import movingAuto
from autoMove.detect import detect_collision, detect_nearby_car
from noChanges.road import draw_road
from noChanges.config import cars, add_car

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

    # 모든 자율주행차에 대해 충돌 및 거리/방향 감지
    for car in cars:
        if car.is_autonomous:
            collision_status, collision_distance = detect_collision(car, [c for c in cars if c != car])
            car.nearest_distance, car.direction_to_nearest, car.car_up, car.car_down, car.car_left, car.car_right = detect_nearby_car(
                car, [c for c in cars if c != car])
            headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}
            if collision_status:
                requests.post('http://localhost:5000/update', data={'message': "충돌 발생!"}, headers=headers)
            elif car.nearest_distance:
                requests.post('http://localhost:5000/update', data={'message': f"{car.nearest_distance:.2f}m에 {car.direction_to_nearest}에 차량이 있습니다."})
                print(f"move_x: {movingAuto('x', car)}, move_y: {movingAuto('y', car)}, vel_x: {car.vel[0]}, vel_y: {car.vel[1]}")

                # 각 방향에 차량이 있는지 여부 출력
                print(f"차량 감지 - 위쪽: {car.car_up}, 아래쪽: {car.car_down}, 왼쪽: {car.car_left}, 오른쪽: {car.car_right}")
            else:
                requests.post('http://localhost:5000/update', data={'message': "안전합니다!"}, headers=headers)

    # 화면 업데이트
    pygame.display.flip()

    # 프레임 속도 제어
    pygame.time.Clock().tick(60)

pygame.quit()