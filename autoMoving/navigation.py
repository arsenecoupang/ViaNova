import pygame
import requests
import time

from pygame.examples.cursors import image
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
# 초기화
pygame.init()

# 화면 설정
nav_screen_width, nav_screen_height = 600, 300
nav_screen = pygame.display.set_mode((nav_screen_width, nav_screen_height))

def navishow_text(message):
    font = pygame.font.SysFont('nanumgothic', 36)
    y_offset = 100
    text_surface = font.render(message, True, (0, 0, 0))
    nav_screen.blit(text_surface, (10, y_offset))

def navishow_emergency():
    image = pygame.image.load('./noChanges/assets/emergency.jpeg')
    image = pygame.transform.scale(image, (nav_screen_width, nav_screen_height))
    nav_screen.blit(image, (0, 0))
def navishow_collision():
    image = pygame.image.load('./noChanges/assets/collision.jpeg')
    image = pygame.transform.scale(image, (nav_screen_width, nav_screen_height))
    nav_screen.blit(image, (0, 0))

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 초기화
    nav_screen.fill((255, 255, 255))  # 하얀색 배경
    # Fetch message from server
    response = requests.get('http://127.0.0.1:5000/message')
    if response.status_code == 200:
        print(response.text)  # Print the response text for debugging
        if response.text == "emergency!":
            navishow_emergency()
        elif response.text == "충돌 발생!":
            navishow_collision()
        else:
            navishow_text(response.text)
    else:
        print(f"Failed to fetch message: {response.status_code}")

    pygame.display.flip()
    time.sleep(1)  # Fetch message every second

pygame.quit()