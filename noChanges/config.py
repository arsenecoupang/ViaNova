# config.py
from car import Car

# 자동차 리스트 생성 (초기 위치와 속도 설정)
cars = [
    Car(370, 480, (0, 0, 255), 0, 0.5, is_autonomous=True),  # 자율주행 자동차
    Car(380, 380, (255, 0, 0), 0, 0.2, is_autonomous=True),  # 자율주행 자동차
    Car(390, 260, (255, 0, 0), 0, 0.3, is_autonomous=True),  # 자율주행 자동차
]

# 원하는 만큼 차를 추가하는 함수
def add_car(x, y, color, vel_x, vel_y):
    cars.append(Car(x, y, color, vel_x, vel_y, is_autonomous=True))