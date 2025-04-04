# app/config.py

# ----- DB -----
DB_PATH = "plant_data.db"  # SQLite DB 파일 이름/경로

# ----- SENSOR THRESHOLDS -----
MOISTURE_THRESHOLD = 300   # 특정 센서 기준 (예: 0~1023)
WATER_GIVEN_THRESHOLD = 900  # 이 값 이상이면 '물을 줬다'고 간주
CHECK_INTERVAL = 60        # 센서/버튼 체크 주기(초)

# ----- TELEGRAM BOT -----
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# 개발 시 실제로는 사용자에게 이 값을 입력받아서 DB에 저장하는 방법이 좋음.
# 다만 샘플로 config에 미리 넣어둔 상태.
DEFAULT_TELEGRAM_CHAT_ID = None  
