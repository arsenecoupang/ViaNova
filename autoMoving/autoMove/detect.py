import math
import pygame


# 두 물체의 거리 계산
def distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

# 충돌 감지 함수
def detect_collision(car, other_cars):
    car_rect = pygame.Rect(car.pos[0], car.pos[1], car.width, car.height)

    for other_car in other_cars:
        other_car_rect = pygame.Rect(other_car.pos[0], other_car.pos[1], other_car.width, other_car.height)

        # 충돌 감지 (사각형의 겹침 여부)
        if car_rect.colliderect(other_car_rect):
            return True, car_rect.collidepoint(other_car.pos[0] + other_car.width // 2, other_car.pos[1] + other_car.height // 2)

    return False, None

# 가까운 차의 거리 및 방향 감지 함수 (레이더 범위 안에 있을 때만 감지)
def detect_nearby_car(car, other_cars):
    car_center = (car.pos[0] + car.width // 2, car.pos[1] + car.height // 2)
    nearest_car = None
    nearest_distance = 101  # 레이더 범위보다 큰 초기값
    direction = ""

    # 방향별 차 존재 여부를 저장하는 변수
    car_up = False
    car_down = False
    car_left = False
    car_right = False

    for other_car in other_cars:
        other_car_center = (other_car.pos[0] + other_car.width // 2, other_car.pos[1] + other_car.height // 2)
        dist = distance(car_center, other_car_center)

        if dist <= 100:  # 레이더 범위 안에 있는 차량만 감지
            # 가장 가까운 차 찾기
            if dist < nearest_distance:
                nearest_distance = dist
                nearest_car = other_car

            # 방향별로 차가 있는지 확인
            if other_car_center[0] > car_center[0]:  # 오른쪽에 있는 경우
                car_right = True
            elif other_car_center[0] < car_center[0]:  # 왼쪽에 있는 경우
                car_left = True
            if other_car_center[1] > car_center[1]:  # 아래쪽에 있는 경우
                car_down = True
            elif other_car_center[1] < car_center[1]:  # 위쪽에 있는 경우
                car_up = True

    # 가장 가까운 차량이 있을 때 방향 결정
    if nearest_car:
        if car_right:
            direction = "오른쪽"
        elif car_left:
            direction = "왼쪽"
        if car_down:
            direction = "아래쪽"
        elif car_up:
            direction = "위쪽"
        return nearest_distance, direction, car_up, car_down, car_left, car_right
    else:
        return None, None, car_up, car_down, car_left, car_right
