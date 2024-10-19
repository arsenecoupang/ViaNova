import pygame
pygame.init()
running = True
# 화면 크기 설정

window_width = 800
window_height = 600

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Car Detection')

x = window_width // 2
y = window_height // 2
carScale_x = 100
carScale_y = 40
detectLine_radius = ((carScale_x//2)**2 + (carScale_y//2)**2)**(1/2)+ 20


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    car = pygame.draw.rect(screen, (0, 255, 0), (x - carScale_x // 2, y - carScale_y // 2, carScale_x, carScale_y))


    detectLine = pygame.draw.circle(screen, (255, 0, 0), (x, y), int(detectLine_radius), 2)
    detectLine.centerx = x
    detectLine.centery = y
    detectLine_rect = pygame.Rect(x - detectLine_radius, y - detectLine_radius, detectLine_radius * 2, detectLine_radius * 2)
    if detectLine_rect.colliderect(car):
        print('Collision!')




    pygame.display.update()



