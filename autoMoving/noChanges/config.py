from autoMoving.car import Car

# 자동차 리스트 생성 (초기 위치와 속도 설정)
autoMoving_car = [
    Car(410, 480, (0, 0, 255), 0, 0.5, is_autonomous=True),  # 자율주행 자동차
    Car(420, 380, (255, 0, 0), 0, 0.2),  # 일반 자동차
    Car(340, 260, (255, 0, 0), 0, 0.3),  # 일반 자동차 추가
]

emergency_car = [
    Car(370, 480, (0, 0, 255), 0, 1, is_emergency= True),  # 구급차
    Car(370, 380, (255, 0, 0), 0, 0.5),  # 일반 자동차
    Car(370, 260, (255, 0, 0), 0, 0.5),  # 일반 자동차 추가
    Car(410, 380, (255, 0, 0), 0, 0.5),  # 일반 자동차 추가
    Car(410, 260, (255, 0, 0), 0, 0.5),  # 일반 자동차 추가
]