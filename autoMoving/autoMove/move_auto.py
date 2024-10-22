# autoMoving/autoMove/move_auto.py
def move_auto(direction):
    # autoMoving/autoMove/move_auto.py
    def move_auto(direction):
        move_x = 0
        move_y = 0

        if direction == "go_left":
            move_x = -1  # Move left
        elif direction == "go_right":
            move_x = 1  # Move right
        elif direction == "go_up":
            move_y = -1  # Move up
        elif direction == "go_down":
            move_y = 1  # Move down

        return move_x, move_y
    pass