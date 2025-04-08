python3  -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
pip install RPi.GPIO requests

python -c "import RPi.GPIO; import requests; print('Installation OK');"

python -c "from app import db; db.save_telegram_chat_id("YOUR_ID");"

