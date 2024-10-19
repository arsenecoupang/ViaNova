import pygame
import math
# finish the code below
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
radar_radius = 150  # 레이더 범위
lane_top, lane_bottom = 100, 500  # 도로의 위쪽과 아래쪽 경계 설정
lane_left, lane_right = 300, 500  # 도로의 두 차선 경계 설정

# 감지 결과를 저장할 변수
detection_results = {
    "right": False,
    "left": False,
    "up": False,
    "down": False
}


# 자동차 클래스
class Car:
    def __init__(self, x, y, color, vel_x, vel_y):
        self.pos = [x, y]
        self.vel = [vel_x, vel_y]
        self.color = color
        self.width = car_width
        self.height = car_height

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (*self.pos, self.width, self.height))
        # 레이더 범위 표시
        pygame.draw.circle(screen, GREEN, (int(self.pos[0] + self.width // 2), int(self.pos[1] + self.height // 2)),
                           radar_radius, 1)

    def update(self):
        # 위-아래 방향으로만 주행
        self.pos[1] += self.vel[1]

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
    global detection_results
    car_center = (car.pos[0] + car.width // 2, car.pos[1] + car.height // 2)
    for other_car in other_cars:
        other_car_center = (other_car.pos[0] + other_car.width // 2, other_car.pos[1] + other_car.height // 2)

        # 레이더 범위 내에 있는지 확인
        if distance(car_center, other_car_center) <= radar_radius:
            # 방향별로 감지 여부 업데이트
            if other_car_center[0] > car_center[0]:  # 오른쪽에 있는 경우
                detection_results["right"] = True
            else:
                detection_results["left"] = True

            if other_car_center[1] > car_center[1]:  # 아래쪽에 있는 경우
                detection_results["down"] = True
            else:
                detection_results["up"] = True

            return distance(car_center, other_car_center), detection_results
    # 감지된 것이 없을 때는 모두 False로 설정
    detection_results = {key: False for key in detection_results}
    return None, detection_results


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
    Car(350, 150, RED, 0, 2),  # 자율주행 자동차 (아래 방향으로 이동)
    Car(380, 300, BLUE, 0, 1),  # 다른 자동차 (아래 방향으로 이동)
    Car(360, 450, RED, 0, 2),  # 다른 자동차 추가
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
        car.draw(screen)

    # 충돌 감지 (첫 번째 자동차 기준)
    distance_to_collision, detection_results = detect_collision(cars[0], cars[1:])

    # 충돌 정보 출력
    if distance_to_collision is not None:
        print(f"충돌 발생! 충돌한 자동차와의 거리: {distance_to_collision}")
        print(f"감지된 방향: {detection_results}")
    else:
        print("감지된 충돌 없음")

    # 화면 업데이트
    pygame.display.flip()

    # 프레임 속도 제어
    pygame.time.Clock().tick(60)

pygame.quit()
