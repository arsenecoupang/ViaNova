import pygame

# 자동차 클래스
class Car:
    def __init__(self, x, y, color, vel_x, vel_y, is_autonomous=False):
        self.pos = [x, y]
        self.vel = [vel_x, vel_y]
        self.color = color
        self.width = 30
        self.height = 50
        self.is_autonomous = is_autonomous  # 자율주행 여부

    def drawcar(self, screen):
        pygame.draw.rect(screen, self.color, (*self.pos, self.width, self.height))

    def drawradar(self, screen):
        if self.is_autonomous:  # 자율주행차만 레이더를 그림
            pygame.draw.circle(screen, (0, 255, 0), (int(self.pos[0] + self.width // 2), int(self.pos[1] + self.height // 2)),
                               100, 1)

    def update(self):
        # 위-아래 방향으로만 주행
        self.pos[1] -= self.vel[1]

        # 차선을 벗어나지 않도록 Y축 위치를 제한
        if self.pos[1] < 100:
            self.pos[1] = 100
        elif self.pos[1] + self.height > 500:
            self.pos[1] = 500 - self.height