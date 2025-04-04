# app/button_manager.py

import time
import RPi.GPIO as GPIO

# 예시 GPIO 핀 번호
BUTTON_PIN = 17

# 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def check_button_press(press_seconds=3):
    """
    푸시버튼을 press_seconds (기본 3초) 이상 길게 누르면 True를 반환.
    버튼 체크는 main 루프에서 주기적으로 호출.
    """
    start_time = None

    # 버튼이 눌렸는지 확인
    if GPIO.input(BUTTON_PIN) == GPIO.LOW:  # 눌림 인식
        # 눌린 시점 기록
        start_time = time.time()

        # 버튼이 올라가기 전까지 계속 체크
        while GPIO.input(BUTTON_PIN) == GPIO.LOW:
            duration = time.time() - start_time
            if duration >= press_seconds:
                return True
            time.sleep(0.1)
    return False