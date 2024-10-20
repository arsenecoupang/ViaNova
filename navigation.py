import pygame
import requests
import time

# 초기화
pygame.init()

# 화면 설정
nav_screen_width, nav_screen_height = 600, 300
nav_screen = pygame.display.set_mode((nav_screen_width, nav_screen_height))

def navishow_text(messages):
    font = pygame.font.SysFont('nanumgothic', 36)
    y_offset = 100
    # Get the last message
    if messages:
        message = messages[-1]
        text_surface = font.render(message, True, (0, 0, 0))
        nav_screen.blit(text_surface, (170, y_offset))
def navishow_emergency():
    font = pygame.font.SysFont('nanumgothic', 36)
    text_surface = font.render("긴급 상황 발생!", True, (255, 0, 0))
    nav_screen.blit(text_surface, (130, 50))
def navishow_human_detected():
    font = pygame.font.SysFont('nanumgothic', 36)
    text_surface = font.render("사람 감지됨!", True, (255, 0, 0))
    nav_screen.blit(text_surface, (130, 50))
# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 초기화
    nav_screen.fill((255, 255, 255))  # 하얀색 배경
    font = pygame.font.SysFont('nanumgothic', 36)
    title = font.render("ViaNova Navigation", True, (0, 0, 0))
    nav_screen.blit(title, (130, 10))  # 텍스트를 화면에 그리기

    # Fetch message from server
    response = requests.get('http://localhost:5000/message')
    if response.status_code == 200:
        try:
            print(response.text)  # Print the response text for debugging
            navishow_text(response.json()['messages'])
        except requests.exceptions.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
    else:
        print(f"Failed to fetch message: {response.status_code}")

    pygame.display.flip()
    time.sleep(1)  # Fetch message every second

pygame.quit()