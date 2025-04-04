# app/db.py
import sqlite3
from datetime import datetime
from app.config import DB_PATH

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # (1) 센서 데이터 저장 테이블
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            moisture INTEGER,
            temperature REAL,
            humidity REAL,
            light REAL
        )
    """)

    # (2) 관수 이력 테이블
    # water_method: 'sensor' (센서 임계값 초과로 판단) or 'button' (버튼으로 판단)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS watering_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            watering_time TEXT NOT NULL,
            water_method TEXT NOT NULL
        )
    """)

    # (3) 사용자 정보 테이블
    # WiFi 설정 시 사용자 입력(telegram_chat_id 등)을 저장할 수도 있음
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_info (
            id INTEGER PRIMARY KEY,
            telegram_chat_id TEXT
        )
    """)

    conn.commit()
    conn.close()

def insert_sensor_data(moisture, temperature, humidity, light):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    now = datetime.now().isoformat()
    cursor.execute("""
        INSERT INTO sensor_data (timestamp, moisture, temperature, humidity, light)
        VALUES (?, ?, ?, ?, ?)
    """, (now, moisture, temperature, humidity, light))
    conn.commit()
    conn.close()

def insert_watering_event(method="sensor"):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    now = datetime.now().isoformat()
    cursor.execute("""
        INSERT INTO watering_history (watering_time, water_method)
        VALUES (?, ?)
    """, (now, method))
    conn.commit()
    conn.close()

def get_last_watering_time():
    """마지막 관수 시점을 반환 (없으면 None)"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT watering_time
        FROM watering_history
        ORDER BY watering_time DESC
        LIMIT 1
    """)
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def save_telegram_chat_id(chat_id):
    """사용자가 입력한 텔레그램 Chat ID를 DB에 저장"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # 단일 사용자 가정 -> user_info 테이블에 id=1 만 사용
    cursor.execute("DELETE FROM user_info")  # 기존 데이터 초기화
    cursor.execute("""
        INSERT INTO user_info (id, telegram_chat_id)
        VALUES (1, ?)
    """, (chat_id,))
    conn.commit()
    conn.close()

def get_telegram_chat_id():
    """DB에서 텔레그램 Chat ID 조회 (없으면 None)"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT telegram_chat_id FROM user_info WHERE id=1")
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None
