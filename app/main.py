# app/main.py

import time
from datetime import datetime, timedelta

from app import db
from app.config import (
    MOISTURE_THRESHOLD,
    WATER_GIVEN_THRESHOLD,
    CHECK_INTERVAL
)
from app.sensor_manager import read_moisture, read_temperature_and_humidity, read_light
from app.button_manager import check_button_press,led_out
from app.notification import send_telegram_message

def main_loop():
    """
    1) 주기적으로 센서 읽기
    2) DB 저장
    3) 관수 이벤트(센서 임계값 초과 or 버튼 3초 눌림) 감지
    4) 목마름(임계값 미달) 시 알림
    """
    print("Smart Plant Supervisor started.")
    db.init_db()  # DB 초기화 (테이블 없으면 생성)

    last_notify_time = None
    
    is_moist_full = False

    while True:
        # -----------------
        # 1) 센서 읽기
        # -----------------
        moisture = read_moisture()
        temperature, humidity = read_temperature_and_humidity()
        light_val = read_light()
        print(f"[SENSOR] M={moisture}, T={temperature:.1f}, H={humidity:.1f}, L={light_val:.1f}")

        # -----------------
        # 2) DB 저장
        # -----------------
        db.insert_sensor_data(moisture, temperature, humidity, light_val)

        if (moisture < WATER_GIVEN_THRESHOLD) and (is_moist_full):
            is_moist_full = False
        
        water_given_by_sensor = (moisture >= WATER_GIVEN_THRESHOLD) and (not is_moist_full)

        for x in range(30):
            # -----------------
            # 3) 물 준 이벤트 판별
            #    (A) 수분센서 값이 WATER_GIVEN_THRESHOLD 이상일 때
            #    (B) 버튼 3초 이상 눌렀을 때
            # -----------------
            water_given_by_button = check_button_press(press_seconds=3)

            if water_given_by_sensor or water_given_by_button:
                is_moist_full = True
                method = "sensor" if water_given_by_sensor else "button"
                db.insert_watering_event(method=method)
                send_telegram_message(f"[{method}] 방금 물을 준 것으로 인식했어요! 싱싱해지고 있어요~")

            # -----------------
            # 4) 목마름(임계 이하) 알림
            #    - 일정 시간(예: 6시간 or 24시간) 주기로만 알림
            # -----------------
            if moisture < MOISTURE_THRESHOLD:
                if not last_notify_time or (datetime.now() - last_notify_time) > timedelta(hours=6):
                    send_telegram_message("나 목말라요 ㅠ 물 주세요!")
                    last_notify_time = datetime.now()

            # -----------------
            # 5) 대기 후 반복
            # -----------------
            led_out(1)
            time.sleep(CHECK_INTERVAL/60)
            led_out(0)
            time.sleep(CHECK_INTERVAL/60)

if __name__ == "__main__":
    main_loop()
