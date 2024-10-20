# carMove_auto.py
import shared_state

def movingAuto(direction):
    move_x = 0
    move_y = 0

    if shared_state.nearest_distance is not None and shared_state.nearest_distance <= 60:
        if shared_state.direction_to_nearest == "오른쪽":
            move_x += 0.3
        elif shared_state.direction_to_nearest == "왼쪽":
            move_x -= 0.3
        elif shared_state.direction_to_nearest == "위쪽":
            move_y -=  0.3
        elif shared_state.direction_to_nearest == "아래쪽":
            move_y += 0.3

    print(f"movingAuto - direction: {direction}, move_x: {move_x}, move_y: {move_y}")
    if direction == 'x':
        return move_x
    elif direction == 'y':
        return move_y