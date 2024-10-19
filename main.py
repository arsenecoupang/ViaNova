import pygame
from car import Car
from detect import detect_collision, detect_nearby_car

# 초기화
pygame.init()

# 화면 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 색상 설정
WHITE = (255, 255, 255)
GRAY = (169, 169, 169)
YELLOW = (255, 255, 0)

# 도로 경계 설정
lane_top, lane_bottom = 100, 500
lane_left, lane_right = 300, 500

# 도로 그리기 함수
def draw_road():
    pygame.draw.rect(screen, GRAY, (lane_left, lane_top, lane_right - lane_left, lane_bottom - lane_top))  # 차도
    pygame.draw.line(screen, YELLOW, (lane_left, lane_top), (lane_left, lane_bottom), 5)  # 왼쪽 경계선
    pygame.draw.line(screen, YELLOW, (lane_right, lane_top), (lane_right, lane_bottom), 5)  # 오른쪽 경계선
    pygame.draw.line(screen, WHITE, ((lane_left + lane_right) // 2, lane_top),
                     ((lane_left + lane_right) // 2, lane_bottom), 5)  # 중앙 차선

# 자동차 리스트 생성 (초기 위치와 속도 설정)
cars = [
    Car(350, 480, (0, 0, 255), 0, 0.5, is_autonomous=True),  # 자율주행 자동차
    Car(380, 300, (255, 0, 0), 0, 0.2),  # 일반 자동차
    Car(370, 260, (255, 0, 0), 0, 0.3),  # 일반 자동차 추가
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