import pygame
import math

# 초기화
pygame.init()

# 화면 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 색상 설정
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (169, 169, 169)
YELLOW = (255, 255, 0)

# 속성 설정
car_width, car_height = 30, 50  # 자동차 크기
radar_radius = 100  # 레이더 범위
lane_top, lane_bottom = 100, 500  # 도로의 위쪽과 아래쪽 경계 설정
lane_left, lane_right = 300, 500  # 도로의 두 차선 경계 설정


# 자동차 클래스
class Car:
    def __init__(self, x, y, color, vel_x, vel_y, is_autonomous=False):
        self.pos = [x, y]
        self.vel = [vel_x, vel_y]
        self.color = color
        self.width = car_width
        self.height = car_height
        self.is_autonomous = is_autonomous  # 자율주행 여부

    def drawcar(self, screen):
        pygame.draw.rect(screen, self.color, (*self.pos, self.width, self.height))

    def drawradar(self, screen):
        if self.is_autonomous:  # 자율주행차만 레이더를 그림
            pygame.draw.circle(screen, GREEN, (int(self.pos[0] + self.width // 2), int(self.pos[1] + self.height // 2)),
                               radar_radius, 1)

    def update(self):
        # 위-아래 방향으로만 주행
        self.pos[1] -= self.vel[1]

        # 차선을 벗어나지 않도록 Y축 위치를 제한
        if self.pos[1] < lane_top:
            self.pos[1] = lane_top
        elif self.pos[1] + self.height > lane_bottom:
            self.pos[1] = lane_bottom - self.height


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
    nearest_distance = radar_radius + 1  # 레이더 범위보다 큰 초기값
    direction = ""

    for other_car in other_cars:
        other_car_center = (other_car.pos[0] + other_car.width // 2, other_car.pos[1] + other_car.height // 2)
        dist = distance(car_center, other_car_center)

        if dist <= radar_radius:  # 레이더 범위 안에 있는 차량만 감지
            # 가장 가까운 차 찾기
            if dist < nearest_distance:
                nearest_distance = dist
                nearest_car = other_car

            # 방향 설정
            if other_car_center[0] > car_center[0]:  # 오른쪽에 있는 경우
                direction = "오른쪽"
            elif other_car_center[0] < car_center[0]:  # 왼쪽에 있는 경우
                direction = "왼쪽"
            if other_car_center[1] > car_center[1]:  # 아래쪽에 있는 경우
                direction = "아래쪽"
            elif other_car_center[1] < car_center[1]:  # 위쪽에 있는 경우
                direction = "위쪽"

    if nearest_car:
        return nearest_distance, direction
    else:
        return None, None


# 도로 그리기 함수
def draw_road():
    # 도로 경계와 차선 그리기
    pygame.draw.rect(screen, GRAY, (lane_left, lane_top, lane_right - lane_left, lane_bottom - lane_top))  # 차도
    pygame.draw.line(screen, YELLOW, (lane_left, lane_top), (lane_left, lane_bottom), 5)  # 왼쪽 경계선
    pygame.draw.line(screen, YELLOW, (lane_right, lane_top), (lane_right, lane_bottom), 5)  # 오른쪽 경계선
    pygame.draw.line(screen, WHITE, ((lane_left + lane_right) // 2, lane_top),
                     ((lane_left + lane_right) // 2, lane_bottom), 5)  # 중앙 차선


# 자동차 리스트 생성 (초기 위치와 속도 설정)
cars = [
    Car(350, 480, BLUE, 0, 0.5, is_autonomous=True),  # 자율주행 자동차
    Car(380, 300, RED, 0, 0.2),  # 일반 자동차
    Car(370, 260, RED, 0, 0.3),  # 일반 자동차 추가
]
# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 초기화
    screen.fill(WHITE)

    # 도로 그리기
    draw_road()

    # 자동차 움직임 업데이트 및 그리기
    for car in cars:
        car.update()
        car.drawcar(screen)
        car.drawradar(screen)  # 자율주행차만 레이더 표시

    # 충돌 감지 (첫 번째 자동차 기준)
    collision_status, collision_distance = detect_collision(cars[0], cars[1:])

    # 가까운 차의 거리 및 방향 정보 감지 (레이더 범위 안에 있을 때만)
    nearest_distance, direction_to_nearest = detect_nearby_car(cars[0], cars[1:])

    # 출력: 충돌 또는 거리/방향 정보
    if collision_status:
        print(f"충돌 발생!")
    elif nearest_distance:
        print(f"전방 {nearest_distance:.2f}m에 {direction_to_nearest}에 차량이 있습니다.")
    else:
        print("감지된 차량 없음")

    # 화면 업데이트
    pygame.display.flip()

    # 프레임 속도 제어
    pygame.time.Clock().tick(60)

pygame.quit()
