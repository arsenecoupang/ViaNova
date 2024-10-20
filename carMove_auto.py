import shared_state

move_x = 0
move_y = 0

# 자율주행차의 이동 방향 조절
if shared_state.nearest_distance is not None and shared_state.nearest_distance <= 60:
    if shared_state.direction_to_nearest == "오른쪽":
        print("왼쪽 회피 조향 중")
        move_x += -0.2
    elif shared_state.direction_to_nearest == "왼쪽":
        print("오른쪽으로 회피 조향 중")
        move_x += 0.2
    elif shared_state.direction_to_nearest == "위쪽":
        print("아래쪽으로 회피 조향 중")
        move_y += 0.2
    elif shared_state.direction_to_nearest == "아래쪽":
        print("위쪽으로 회피 조향 중")
        move_y += -0.2