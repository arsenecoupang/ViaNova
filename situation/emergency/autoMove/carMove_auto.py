# carMove_auto.py
from autoMoving import shared_state
import autoMoving.car
from autoMoving.autoMove.carMove_auto import move_x , move_y

network_message = None : str

def move_normal(is_emergency : bool, moveValue : str):
    if network_message == "emergency_coming":
        if moveValue == 'move_x':
            return



