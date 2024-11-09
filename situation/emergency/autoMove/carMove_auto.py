# situation/emergency/autoMove/carMove_auto.py
from situation.emergency.autoMove.move_auto import move_auto

network_message = ""

def move_normal(self):
    if self.network_message == "emergency_coming":
        if self.pos[0] <= 400:
            move_x, move_y = move_auto("go_left")
        else:
            move_x, move_y = move_auto("go_right")
        self.pos[0] += move_x
        self.pos[1] += move_y
        ''''''