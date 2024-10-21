import pygame
from autoMoving.autoMove.carMove_auto import movingAuto
class Car:
    def __init__(self, x, y, color, vel_x, vel_y, is_autonomous=False, is_emergency=False, network_message=None):
        self.pos = [x, y]
        self.vel = [vel_x, vel_y]
        self.color = color
        self.width = 30
        self.height = 50
        self.is_autonomous = is_autonomous
        self.is_emergency = is_emergency
        self.network_message = network_message

    def drawcar(self, screen):
        pygame.draw.rect(screen, self.color, (*self.pos, self.width, self.height))

    def drawradar(self, screen):
        if self.is_autonomous:
            pygame.draw.circle(screen, (0, 255, 0), (int(self.pos[0] + self.width // 2), int(self.pos[1] + self.height // 2)), 100, 1)

    def update(self):
        if self.is_autonomous:
            if self.vel[0] >= 0:
                self.pos[1] -= self.vel[1] + movingAuto('y')
                self.pos[0] -= self.vel[0] + movingAuto('x')
            else:
                self.pos[1] -= self.vel[1]
                self.pos[0] -= self.vel[0]
        else:
            self.pos[1] -= self.vel[1]
            self.pos[0] -= self.vel[0]

    def car_pos(self, xy: str):
        if xy == 'x':
            result = self.pos[0]
        if xy == 'y':
            result = self.pos[1]
        return result

    def set_network_message(self, message):
        self.network_message = message