import pygame

# 색상 설정
GRAY = (169, 169, 169)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# 도로 경계 설정
lane_top, lane_bottom = 100, 500
lane_left, lane_right = 300, 500

# 도로 그리기 함수
def draw_road(screen):
    pygame.draw.rect(screen, GRAY, (lane_left, lane_top, lane_right - lane_left, lane_bottom - lane_top))  # 차도
    pygame.draw.line(screen, YELLOW, (lane_left, lane_top), (lane_left, lane_bottom), 5)  # 왼쪽 경계선
    pygame.draw.line(screen, YELLOW, (lane_right, lane_top), (lane_right, lane_bottom), 5)  # 오른쪽 경계선
    pygame.draw.line(screen, WHITE, ((lane_left + lane_right) // 2, lane_top),
                     ((lane_left + lane_right) // 2, lane_bottom), 5)  # 중앙 차선