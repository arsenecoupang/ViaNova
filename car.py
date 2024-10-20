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

        # 차선을 벗어나지 않도록 Y축 위치를 제한
        if self.pos[1] < 100:
            self.pos[1] = 100
        elif self.pos[1] + self.height > 500:
            self.pos[1] = 500 - self.height