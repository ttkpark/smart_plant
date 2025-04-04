# app/notification.py
import requests
from app.db import get_telegram_chat_id
from app.config import TELEGRAM_BOT_TOKEN

def send_telegram_message(message):
    """
    DB에 저장된 telegram_chat_id를 이용해 메시지 전송.
    """
    chat_id = get_telegram_chat_id()
    if not TELEGRAM_BOT_TOKEN or not chat_id:
        print("No Telegram Bot Token or Chat ID set. Cannot send message.")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    try:
        resp = requests.post(url, data=data, timeout=5)
        print("Telegram response:", resp.json())
    except Exception as e:
        print("Telegram send error:", e)
