# carMove_auto.py
from autoMoving.autoMove.carMove_auto import move_auto
network_message = ""

def move_normal(self):
    if self.network_message == "emergency_coming":
        if self.pos<=400:
            move_auto("go_left")

        else:
            move_auto("go_right")



