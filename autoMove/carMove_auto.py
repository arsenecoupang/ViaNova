# carMove_auto.py
def movingAuto(direction, car):
    move_x = 0
    move_y = 0

    if car.nearest_distance is not None and car.nearest_distance <= 60:
        if car.car_up:
            if car.car_right:
                move_x += 0.3
                move_y -= 0.3
            elif car.car_left:
                move_x -= 0.3
                move_y -= 0.3
            else:
                move_y -= 0
                move_x = 0
        elif car.car_down:
            if car.car_right:
                move_x += 0.3
                move_y += 0.3
            elif car.car_left:
                move_x -= 0.3
                move_y += 0.3
            else:
                move_y = 0
                move_x = 0
        else:
            if car.car_right:
                move_x += 0.1
                move_y = 0
            elif car.car_left:
                move_x -= 0.1
                move_y = 0
            else:
                move_x = 0
                move_y = 0

    if direction == 'x':
        return move_x
    elif direction == 'y':
        return move_y