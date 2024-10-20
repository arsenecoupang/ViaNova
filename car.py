# car.py
import pygame
from autoMove.carMove_auto import movingAuto

class Car:
    def __init__(self, x, y, color, vel_x, vel_y, is_autonomous=False):
        self.pos = [x, y]
        self.vel = [vel_x, vel_y]
        self.color = color
        self.width = 30
        self.height = 50
        self.is_autonomous = is_autonomous
        self.nearest_distance = None
        self.direction_to_nearest = None
        self.car_up = False
        self.car_down = False
        self.car_left = False
        self.car_right = False

    def drawcar(self, screen):
        pygame.draw.rect(screen, self.color, (*self.pos, self.width, self.height))

    def drawradar(self, screen):
        if self.is_autonomous:
            pygame.draw.circle(screen, (0, 255, 0), (int(self.pos[0] + self.width // 2), int(self.pos[1] + self.height // 2)), 100, 1)

    def update(self):
        if self.is_autonomous:
            move_x = movingAuto('x', self)
            move_y = movingAuto('y', self)
            self.pos[1] += self.vel[1] + move_y
            self.pos[0] += self.vel[0] + move_x
        else:
            self.pos[1] -= self.vel[1]
            self.pos[0] -= self.vel[0]

        if self.pos[1] < 100:
            self.pos[1] = 100
        elif self.pos[1] + self.height > 500:
            self.pos[1] = 500 - self.height