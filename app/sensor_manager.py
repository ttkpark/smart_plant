# app/sensor_manager.py
import random
# 예시: 실제 센서의 경우 RPi.GPIO, Adafruit_DHT, smbus2 등 라이브러리를 import

def read_moisture():
    """
    토양 수분 센서 값 읽어오기 (예: ADC)
    여기서는 테스트를 위해 랜덤 값 리턴
    """
    return random.randint(0, 1023)

def read_temperature_and_humidity():
    """
    온도/습도 센서 (DHT22 등)에서 값 읽어오기
    """
    temperature = random.uniform(18, 30)
    humidity = random.uniform(30, 60)
    return temperature, humidity

def read_light():
    """
    조도 센서(BH1750 등)에서 값 읽어오기
    """
    return random.uniform(100, 1000)
