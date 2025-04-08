# 1. 프로젝트 구조
```text
smart_plant/
├── app/
│   ├── __init__.py           # 파이썬 패키지임을 알려주는 파일 (비어있어도 됨)
│   ├── config.py             # 환경 설정, 상수, 토큰 등
│   ├── db.py                 # DB 연결, 테이블 생성, CRUD 함수
│   ├── sensor_manager.py     # 센서 읽기 로직
│   ├── notification.py       # 텔레그램/카카오톡 등 알림 전송 로직
│   └── main.py               # 메인 실행 스크립트 (수퍼바이저)
├── requirements.txt          # 설치해야 할 Python 라이브러리 목록
└── README.md                 # 프로젝트 개요/설명
```

# 2. Windows 설치 및 검증 (예시)

## 2.1 파이썬 버전 확인  
- **Python 3.8+** 권장 (예: 3.9, 3.10 등)  
```powershell
python --version
```
- 설치되어 있지 않다면 [공식 Python 사이트](https://www.python.org/downloads/)에서 설치.

## 2.2 가상환경(venv) 생성 및 활성화
```powershell
# smart_plant 폴더로 이동
cd C:\path\to\smart_plant

# venv 폴더(이름 자유)를 생성
python -m venv venv

# 가상환경 활성화
.\venv\Scripts\activate
```

## 2.3 라이브러리 설치
```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

> **참고**: Windows 환경에서는 `RPi.GPIO`, `Adafruit_DHT` 설치가 실패하거나, 설치되어도 실제 하드웨어 동작은 불가.  
> - GPIO 없이 테스트할 경우, `button_manager.py` 등 GPIO 종속 코드를 빼거나 예외 처리해두세요.

## 2.4 설치 검증
```powershell
# 1) 버전 확인
python --version

# 2) 라이브러리 목록 확인
pip list

# 3) 특정 라이브러리 버전 확인
python -c "import requests; print(requests.__version__)"
```

- 위 명령으로 `requests`, `python-telegram-bot` 등이 정상 설치되었는지 확인 가능.  
- 라즈베리 파이 전용 라이브러리는 Windows에서 설치 자체가 실패할 수 있으므로 유의.

---

# 3. Linux(Raspberry Pi) 설치 및 검증 (예시)

## 3.1 파이썬 버전 확인
```bash
python3 --version
```
- Raspberry Pi OS (라즈비안)은 기본적으로 Python 3.x가 설치됨.

## 3.2 사전 패키지 설치 (GPIO, DHT 등 필요시)
```bash
sudo apt-get update
sudo apt-get install -y python3-pip python3-venv libgpiod2
```
- `libgpiod2`는 일부 DHT 라이브러리/Adafruit 라이브러리에서 필요할 수 있음.

## 3.3 프로젝트 폴더로 이동 후 가상환경 생성/활성화
```bash
cd /home/pi/smart_plant
python3 -m venv venv
source venv/bin/activate
```

## 3.4 라이브러리 설치
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 3.5 설치 검증
```bash
# 1) 파이썬 버전
python --version

# 2) 라이브러리 목록
pip list

# 3) 특정 라이브러리 임포트 테스트
python -c "import RPi.GPIO; import Adafruit_DHT; import requests; print('OK')"
```
- 에러 없이 `'OK'`가 출력되면, 필요한 라이브러리가 정상적으로 설치된 것입니다.

---

# 4. 주의 및 팁

> **주의**  
> - **RPi.GPIO**, **Adafruit_DHT** 등 라즈베리파이 전용 라이브러리는 Windows 환경에서 정상적으로 설치/동작하기 어렵습니다(주로 라즈베리파이의 GPIO 하드웨어에 의존).  
> - Windows 환경에서 센서와 GPIO 관련 부분은 테스트/에뮬레이션이 제한될 수 있음을 감안하세요.  
> - 본 예시에서는 **가상환경(venv)** 사용을 권장합니다.  

1. **RPi.GPIO 버전 호환**  
   - Raspberry Pi OS 버전에 따라 RPi.GPIO 최신 버전이 다를 수 있으니, `apt-get install python3-rpi.gpio`로 설치하거나, `pip install RPi.GPIO` 중 선택하세요.  
2. **Adafruit_DHT 사용 시**  
   - `Adafruit_Python_DHT` 레포는 오래된 것이므로, 현재는 `pip install Adafruit_DHT`나 `adafruit-circuitpython-dht`를 쓰는 방법이 있습니다. 사용 라이브러리별로 예제가 조금씩 다릅니다.  
3. **시스템 서비스 등록**  
   - 실제 장비에서는 `main.py`를 **시스템 서비스(systemd)**로 등록해 부팅 시 자동 실행하도록 구성할 수 있습니다.  
4. **Windows vs. Linux 기능 차이**  
   - Windows는 **GPIO 제어**가 불가능하거나 매우 제한적입니다. 센서 연동 테스트는 대개 라즈베리 파이에서 직접 진행하는 것이 좋습니다. Windows에서는 “코드 구조”나 “로직”을 테스트하기 위한 용도로만 가상환경 구성이 가능합니다.  

---

## 마무리

위 **설치 명령어**(Windows / Linux)와 **검증 커맨드**를 통해,  
- **가상환경**을 만들고,  
- **`requirements.txt`에 명시된 라이브러리**를 설치한 뒤,  
- **필요한 종속 패키지**(libgpiod2 등)를 갖추면,  

이전에 작성한 **스마트 플랜트(Planty) 프로젝트**가 문제없이 실행될 것입니다.  
필요 시, **버튼 GPIO**나 **DHT 센서** 등도 실제 하드웨어 연결에 맞춰 설치 및 설정을 보완해 주시면 됩니다.  




# 스마트 식물 대화 기기(‘나 목말라’ 알림 시스템) **개발 계획서**

---

## 1. 프로젝트 개요

1. **프로젝트 이름**  
   - (예시) **“플랜티(Planty) – 스마트 식물 대화 기기”**  

2. **기능 개요**  
   - 라즈베리 파이(Raspberry Pi)와 센서를 이용하여 식물의 상태(수분, 조도, 온도 등)를 파악  
   - 일정 조건(수분 부족, 햇빛 부족 등)이 되면 텔레그램/카카오톡/알림톡 등으로 사용자에게 메시지 전송  
   - 초기 설정 시, 사용자가 간단한 페이지(SoftAP, Captive Portal 등) 접속해 WiFi 정보를 등록 → 라즈베리 파이가 WiFi에 연결되어 인터넷 통신 가능  
   - OpenAI API를 활용하여 보다 자연스러운 대화 형태로 알림 메세지를 사용자에게 전달(선택 사항)  

3. **프로젝트 목표**  
   - **하드웨어 + 소프트웨어 + 클라우드**가 통합된 솔루션  
   - 사용자 친화적이며, 추후 앱 확장성(메시지 자동 전송, 로그 관리, 식물별 커스텀 메시지) 고려  

---

## 2. 필요 준비물 및 부품

### 2.1 하드웨어

1. **라즈베리 파이 4 (Raspberry Pi 4)**  
   - RAM 4GB 이상 모델 권장(여유 성능 확보 위해)  
   - 전원 어댑터(5V 3A 이상)  
   - 마이크로 SD 카드(8GB 이상, Raspbian OS 설치용)  

2. **수분 센서(Soil Moisture Sensor)**  
   - 예시: FC-28(아날로그 출력) + ADC 모듈(MCP3008 등)  
   - 센서 종류에 따라 직접적인 금속 침투형 센서 or 캐패시티 방식 센서 고려  
   - 수명이 긴 캐패시티 방식 권장  

3. **조도 센서**  
   - 예시: BH1750(디지털 I2C 센서), 혹은 LDR + ADC  
   - 식물의 빛 환경 모니터링을 위해 사용  

4. **온습도 센서**  
   - 예시: DHT22, AM2302, BME280 등  
   - 정확도와 안정성을 위해 DHT11보다는 DHT22 이상 추천  

5. **통신(와이파이 모듈)**  
   - 라즈베리 파이 4에는 이미 온보드 WiFi가 있음 → 추가 모듈 필요 없음  

6. **기타**  
   - 점퍼 케이블, 브레드보드(또는 PCB), 저항, LED 표시등(테스트용)  
   - 프로젝트 박스(하우징)  

### 2.2 소프트웨어 스택

1. **운영체제**  
   - 라즈비안(Raspberry Pi OS) 또는 Ubuntu for Raspberry Pi  

2. **개발 언어**  
   - **Python 3** (주요 로직, 센서 데이터 처리, OpenAI API 연동, 텔레그램/카카오톡 API 연동)  

3. **개발 툴 및 라이브러리**  
   - `Python` 라이브러리  
     - 센서 제어: `Adafruit_DHT`, `smbus2`(I2C), `RPi.GPIO`(또는 `gpiozero`), `spidev`(MCP3008 등)  
     - HTTP 통신: `requests`  
     - OpenAI API: `openai`  
     - 텔레그램: `python-telegram-bot`  
     - 카카오톡(알림톡) API 연동 시: Restful API 요청(`requests` 활용)  
   - **MQTT 브로커** (선택): Mosquitto, EMQX, HiveMQ 등 → 여러 기기 확장 시 사용 가능  
   - **데이터베이스** (선택): SQLite(간단), InfluxDB(시간 시리즈), Firebase RealTime DB 등  

4. **서비스/호스팅(선택)**  
   - **Webhook 기반 알림**: 텔레그램/카카오톡에 Webhook 등록이 필요할 수 있으므로, 외부에 노출 가능한 서버나 클라우드 사용 고려  
   - **VPN / 포트포워딩**: 가정용 인터넷 환경에서 라즈베리 파이를 직접 노출하는 방식 vs 클라우드 서버에 라즈베리 파이가 주기적 요청(Polling)  

### 2.3 기타 준비물

1. **OpenAI Key**  
   - ChatGPT 등 OpenAI API 사용을 위해서는 계정과 유료 결제가 가능한 Key 필요  

2. **텔레그램 봇 토큰**  
   - [텔레그램 ‘BotFather’](https://core.telegram.org/bots) 통해 발급받는 API 토큰  

3. **카카오 디벨로퍼스(Kakao Developers) 계정**  
   - 카카오톡 알림톡, 메시지 API 발급을 위해 필요  

4. **와이파이 SSID / 비밀번호**  
   - 초기 설정 시, 라즈베리 파이가 연결될 WiFi 정보  

---

## 3. 개발 단계

### 3.1 하드웨어 구성

1. **라즈베리 파이 OS 설치**  
   - 라즈베리 파이 이미저(Raspberry Pi Imager)나 Etcher 사용하여 마이크로 SD 카드에 Raspbian OS 등 설치  
2. **센서 연결**  
   - **수분 센서** → 아날로그 출력이므로 MCP3008, ADS1115 등 ADC 모듈을 통해 SPI/I2C 인터페이스 연결  
   - **조도 센서**(BH1750) → I2C 연결, GPIO(I2C) 핀에 연결  
   - **온습도 센서**(DHT22) → 1개의 GPIO 핀 + 전원 + 그라운드 연결  
3. **배선 및 센서 작동 테스트**  
   - 브레드보드 활용, 점퍼 케이블로 배선 후 `Adafruit_DHT` 라이브러리 등으로 테스트 코드 작성  
   - 수분 센서 값, 조도 센서 값, 온습도 센서 값 정상 수집되는지 CLI에서 확인  

### 3.2 소프트웨어 개발

1. **라즈베리 파이 환경 설정**  
   - `sudo raspi-config` → 인터페이스 I2C, SPI 활성화  
   - Python 3.x 버전 설치(기본 포함됨), 필요 라이브러리 설치  
     ```bash
     sudo apt-get update
     sudo apt-get install python3-pip
     pip3 install RPi.GPIO gpiozero adafruit-circuitpython-dht smbus2 spidev python-telegram-bot requests openai
     ```
2. **수퍼바이저 스크립트(상시 가동 프로세스) 작성**  
   - 예시 파일명: `main.py`
   - 주요 기능
     - **(1) 센서 데이터 읽기**: 일정 주기로 센서 값 수집 (예: 1분 단위)  
     - **(2) 데이터 저장/가공**: 최근 관수 일자 판단 로직(수분 값이 일정 임계점 이상 올라갔을 때 ‘물을 준 시점’으로 판단)  
     - **(3) 조건 체크**:  
       - ‘관수 주기 일주일’ 정책 → 오늘 날짜에서 7일 이상 지난 경우 알림  
       - 적정 수분도 미달 시, 실시간 알림  
     - **(4) 메시지 전송(알림)**: 텔레그램/카카오톡/푸시 API 호출  
       - 하드코딩 메시지(“나 목말라요. 물 주세요!”) or OpenAI API 호출로 자연스러운 문장 생성  
     - **(5) 대기**: 무한 루프 or cron job 등으로 반복  
   - 고려 사항: 향후 웹 서버(플라스크, FastAPI 등)와 연동하여 DB에 데이터 저장, 사용자별 기기 관리 가능  

3. **알림 API 연동**  
   - **텔레그램**  
     - `python-telegram-bot` 라이브러리를 사용하면 편리  
     - 봇 생성(토큰 획득) 후 특정 Chat ID로 메시지 전송  
   - **카카오톡(알림톡)**  
     - [Kakao Developers](https://developers.kakao.com/)에서 앱 생성  
     - 알림톡이나 메시지 API 사용 시 REST API 방식으로 `requests` 통해 메시지 전송  
   - 메시지 예시  
     ```python
     import requests

     def send_kakao_message(user_key, message):
         url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
         headers = {
             "Authorization": f"Bearer {user_key}",
         }
         data = {
             "template_object": {
                 "object_type": "text",
                 "text": message,
                 "link": {
                     "web_url": "http://your_web_url.com"
                 }
             }
         }
         response = requests.post(url, headers=headers, json=data)
         print(response.json())
     ```  

4. **OpenAI API 연동(선택)**  
   - 안내 문구를 ChatGPT 형식으로 생성하고 싶다면, OpenAI의 Completion or ChatCompletion API 사용  
   - 예시(Pseudocode)  
     ```python
     import openai
     openai.api_key = "YOUR_API_KEY"

     def generate_plant_message(condition):
         prompt = f"식물 상태가 '{condition}'입니다. 사용자에게 친근하게 물을 달라고 안내하는 문장을 만들어줘."
         response = openai.Completion.create(
             engine="text-davinci-003",
             prompt=prompt,
             max_tokens=50,
             temperature=0.7
         )
         return response.choices[0].text.strip()
     ```  

5. **WiFi 설정(SoftAP, Captive Portal)**  
   - **초기등록 절차**:  
     - Planty(라즈베리 파이)가 SoftAP(Access Point) 모드 → 스마트폰 WiFi 설정에서 “Planty-Setup” 연결 → 자동으로 열리는 페이지(Captive Portal)에서 집 WiFi SSID/Password 입력 → 라즈베리 파이가 이를 저장 후 재부팅 → 집 WiFi에 접속  
   - Raspberry Pi에서 SoftAP 세팅: `hostapd`, `dnsmasq` 설정 등  
   - Captive Portal 구현: 간단한 Flask 앱 + iptables 리다이렉션 사용  
   - 시제품 단계(간단 버전)이라면 **hdmi 연결 + 키보드**로 직접 SSID/PW 세팅 가능  

### 3.3 프로토타입 테스트

1. **하드웨어 완성 → 센서 데이터 정상 수집 확인**  
2. **네트워크 확인 → 텔레그램/카카오 메시지 전송 정상 동작 확인**  
3. **수분 임계값 테스트**  
   - 물 주기 전/후 데이터 로깅 → 알림 발송 로직 점검  
4. **오류 로그 확인**  
   - Python 예외처리, 센서 오류, 네트워크 오류 등 로그를 파일로 남기고, 주기적으로 확인  

### 3.4 시제품 완성 후 보완

1. **하우징(디자인) 보완**  
   - 배선/센서 위치 고정  
2. **UI/UX 개선**  
   - 앱 or 웹 대시보드 통해 식물 상태 조회, 수분 그래프, 지난 관수 이력, 알림 이력 조회 등  
3. **안정화 작업**  
   - 라즈베리 파이 자가 재부팅 대책(Watchdog)  
   - 네트워크 끊김 대응(재시도 로직)  

---

## 4. 예상 개발 일정(샘플)

| 단계                       | 소요기간    | 주요 내용                                       |
|---------------------------|------------|------------------------------------------------|
| 기획 및 요구사항 정의       | 1주        | - 기능 정의, 센서 종류 결정, 메시지 서비스 결정                         |
| 하드웨어 준비 & 테스트       | 1~2주      | - 라즈베리 파이 세팅, 센서 연결/테스트, ADC 설정                      |
| 소프트웨어 기본 로직 구현    | 2주        | - Python Supervisor, 센서 데이터 수집 로직, 알림 API 통합            |
| WiFi 설정(SoftAP) & 설정 웹 | 1~2주      | - Captive Portal 구현, AP 전환/재부팅 처리                           |
| 오픈AI API 연동             | 1주        | - 자연어 문구 생성 (필요 시)                                       |
| 통합 테스트 & 디버깅         | 1~2주      | - 실제 테스트, 상황별 알림 로직 확인, 네트워크 안정성                 |
| 시제품 완성 및 피드백        | 1주        | - 사용자 피드백, 외관, UI/UX 보완                                  |

---

## 5. 예산/비용 개요 (대략)

1. **하드웨어**  
   - 라즈베리 파이 4 세트: 약 10만 ~ 12만원 내외(한국 시세 기준 변동 가능)  
   - 센서: 수분 센서(2천~1만원), 조도 센서(BH1750 모듈 5천원~1만원), 온습도(DHT22 약 5천원)  
   - ADC 모듈(MCP3008 등): 5천원 내외  
   - 기타 부품(케이블, 브레드보드 등): 1~2만원  

2. **소프트웨어/서비스**  
   - 텔레그램: 무료  
   - 카카오톡: 기본적으로 무료이나, 알림톡(비즈니스) API는 건당 요금이 있을 수 있음(카카오 비즈 메시지 정책 참조)  
   - OpenAI API: 메시지 길이에 따라 과금(월 5달러~ 수십 달러, 트래픽량에 따라 상이)  

3. **기타**  
   - 클라우드(서버 호스팅): 월 5~10달러(예: AWS Lightsail, Vultr 등) - 웹서버/DB 운용 시  

---

## 6. 확장 및 고려사항

1. **추가 센서**  
   - CO2 센서, pH 센서 등을 추가해 식물 생장 컨디션 모니터링 고도화  
2. **자동 관수 시스템 연동**  
   - 솔레노이드 밸브 + 펌프 + 물통을 연결하면 부족 시 자동 물공급 → “나 대신 물 주기” 기능  
3. **스마트폰 앱 개발**  
   - MVP 단계에서는 텔레그램/카카오로 충분  
   - 정식 출시 시, 앱 내에서 푸시 알림, 그래프, 사용자별 다중 기기 관리 가능  
4. **보안**  
   - HTTPS 통신, 사용자 인증(토큰/세션)  
   - 센서 데이터 및 사용자 정보 보호  
5. **데이터 분석**  
   - 장기 데이터(수분, 온도, 빛)를 모아서 식물 성장 패턴/추천 정보 제공  
6. **AI 대화 엔진 고도화**  
   - OpenAI API 이외에도 Hugging Face, KoGPT 등 다른 모델 연동 가능  

---

## 7. 결론 및 요약

- 이 솔루션은 **라즈베리 파이 4 + 수분/조도/온습도 센서**를 활용해 식물 상태를 **실시간 모니터링**하고, 일정 주기에 **자동으로 물 주기 알림**을 발송하는 시스템이다.  
- 초기 설정(SoftAP/Captive Portal, 또는 간단히 수동 WiFi 설정)을 통해 현장 네트워크와 연결되면 **텔레그램/카카오톡 API** 등을 이용해 간편하게 알림을 수신할 수 있다.  
- **OpenAI API**를 연동하면 하드코딩된 문구보다 더욱 풍부하고 자연스러운 대화형 알림이 가능해진다.  
- 향후 **자동 관수 시스템**, **추가 센서**, **전용 앱** 등의 확장이 용이하다.  

이상으로, **스마트 식물 기기**(“나 목말라” 알림 솔루션) 구현을 위한 **개발환경, 필요 부품, 준비물, 그리고 단계별 개발 로드맵**을 제시해 드렸습니다. 이 계획을 기반으로 프로토타입을 빠르게 제작한 뒤, 테스트 결과를 토대로 기능을 보완해 나가면 성공적인 제품 개발을 진행하실 수 있을 것입니다. 

--- 

### 부록: 참고 링크 (실제 개발 시 유용)

- [Raspberry Pi 공식 문서](https://www.raspberrypi.org/documentation/)  
- [Adafruit Sensor Guides (파이썬 예제)](https://learn.adafruit.com/category/sensors)  
- [텔레그램 BotFather 사용법](https://core.telegram.org/bots)  
- [카카오톡 메시지/알림톡 API Docs](https://developers.kakao.com/)  
- [OpenAI Python Library](https://pypi.org/project/openai/)  

> **주의**: 상기 링크들은 실제 환경에 따라 URL이 변경되거나 문서 내용이 바뀔 수 있으므로, 배포 전 최신 문서를 확인하시기 바랍니다.

모쪼록 도움이 되길 바라며, 원활한 개발 진행을 기원합니다!

**DB(데이터베이스) 활용 여부**는 궁극적으로 **어떤 데이터를 얼마나 오래·많이 축적**하고, **그 데이터를 어떻게 활용**할 것인지에 따라 결정됩니다.  
단순히 “7일이 지났는지” 정도만 매번 실시간으로 센서 값을 읽고 판단하는 수준이라면 **파일 시스템에 날짜를 기록**하거나, **간단한 로컬 DB(예: SQLite)** 하나로도 충분합니다.  

---

## 1. 어떤 프로그램(엔티티)이 DB를 사용하게 될까?

1. **수퍼바이저(메인 파이썬 프로그램)**  
   - 센서 데이터를 주기적으로 읽고, **“마지막으로 물을 준 시점”**이나 **현재 수분·조도·온습도**를 기록할 필요가 있습니다.  
   - 하드코딩하거나 단순 텍스트 파일로 저장해도 되지만, “최근 관수 이력(예: 1주 전, 2주 전)”과 같은 이력을 누적 관리하고 싶다면 DB가 편리합니다.

2. **(추가 기능 시) 웹 서버나 앱**  
   - 만약 나중에 시제품에서 확장해, **“사용자가 직접 식물 상태 그래프를 보고 싶다”**거나  
   - **“특정 시간대마다 센서값 변화를 통계적으로 보고 싶다”** 같은 기능이 생길 수 있습니다.  
   - 이때는 DB에서 지난 기록(히스토리)을 **조회**하고 **시각화**하는 로직이 추가됩니다.

---

## 2. 언제, 어디서 DB를 사용하게 될까?

1. **“언제”**:  
   - 센서값을 일정 주기(예: 1분, 10분 등)로 측정할 때마다 DB에 저장.  
   - 식물에 물을 줄 때(또는 수분센서 값이 갑자기 올라 ‘관수’ 사실이 감지될 때) → “최근 관수 시점”을 기록.

2. **“어디서”**:  
   - **로컬(라즈베리 파이 내부)**에서 DB가 구동되도록 설정하는 것이 간단합니다.  
   - 라즈베리 파이 안에 **SQLite** 또는 **파일 DB(예: CSV, JSON)**를 두고 쓰면, 복잡한 설정 없이도 빠르게 개발할 수 있습니다.  
   - 여러 기기가 하나의 데이터를 공유해야 하거나, 외부 모니터링 시스템과 통합해야 할 필요가 크다면 **클라우드 DB**를 쓰는 방향을 고려할 수 있습니다.

---

## 3. 무슨 목적으로 사용할까?

1. **상태 이력 관리 / 로그 기능**  
   - “**언제 마지막으로 물을 줬는가**”를 기록하고, 주기가 넘었을 때 알림 전송 로직을 실행.  
   - “**센서값 변화**”를 시간 순서대로 쌓아두고, 온도·습도·조도 변화를 추적.

2. **사용자별(혹은 식물별) 데이터 관리** (개발 확장 시)  
   - 만약 사용자/식물 여러 개를 한 대의 라즈베리 파이가 관리한다면, 각 식물별로 DB에 row를 두고 식별(plant_id)해서 관리할 수 있습니다.  
   - 알림을 보낼 때도 “이 식물의 기록”을 참조해 “이제 물 줄 때가 됐어요”라고 안내.

3. **기타 부가 기능**  
   - 식물이름, 물주는 주기, 사용자가 선호하는 알림 방법(텔레그램/카카오톡 여부) 같은 **환경 설정**을 DB에 저장.  
   - 오프라인 구간이 있었을 때(예: 네트워크가 끊겼다가 복구됨), “그동안 기록된 센서 값”을 한꺼번에 모아서 어떤 서버에 **동기화**할 수도 있음.

---

## 4. 굳이 클라우드 DB가 필요할까?

> “굳이 클라우드 DB를 쓸 필요가 없다고 생각하거든.”

**결론적으로**,  
- 단일 기기(라즈베리 파이 1대)에서,  
- “언제 물 줬는지” 정도만 관리하고,  
- 사용자도 **현지(파이)에서만** 확인하면 된다면  
  → **클라우드 DB**는 필수가 아닙니다.  

아래 상황에서는 클라우드 DB가 **선택** 혹은 **장점**이 있을 수 있습니다:

1. **여러 대의 스마트 식물 기기가 각각 센서 데이터를 모아서 중앙 서버에서 통계/분석/관리**  
2. **사용자가 스마트폰 앱이나 웹 대시보드**로 외부 어디서나 접근해서 **실시간 식물 상태** 확인  
3. **‘IoT 플랫폼(MQTT 서버, Firebase, etc.)**’ 활용해 푸시 알림, 데이터 분석, 확장 기능 개발  

하지만 **시제품/개인 프로젝트** 단계에서, **로컬의 SQLite**나 **간단한 JSON/CSV** 파일 로그만으로도 충분히 기능 동작이 가능합니다. 나중에 서비스가 커지고, 데이터 양이 많아져서 통합 모니터링을 해야 한다면, 그때 **클라우드 DB**(혹은 로컬 DB→클라우드 동기화)로 넘어가면 됩니다.

---

### 정리

- **DB는 주로 “수퍼바이저(메인 파이썬)”에서 센서 데이터를 주기적으로 기록하고, 마지막 관수 시점을 저장**하는 용도로 사용합니다.  
- 시제품 수준에서는 **라즈베리 파이 내부**에 **SQLite** 또는 간단한 **CSV/JSON** 기록 방식을 쓰면 관리가 쉽습니다.  
- 클라우드 DB는 “모든 기기를 하나의 서버에서 통합 관리”하거나, “원격에서 다수 기기의 데이터를 모아서 큰 분석을 하고 싶을 때” 필요할 수 있지만, **단순 알림 기능**이라면 필수가 아닙니다.  

이렇게 **데이터 보관 및 이력 조회를 쉽게 하고 싶을 때** DB가 편리하나,  
**프로젝트 요구사항**에 따라 **최소한의 로컬 저장**만으로도 충분히 돌아갈 수 있다는 점을 참고하시면 되겠습니다.
# 시작법
```bash
python -m app.main
```

# bot 정보
- invitation link : t.me/smart_plant_a123_bot

- how to get : https://api.telegram.org/bot7568892274:AAGk9j4hJ76p96aJWYi8a8nBWqHl7fAVg6k/getUpdates
여기서 from id를 잘 찾아보라.

- [메시지 조회](https://api.telegram.org/bot봇Token값/getUpdates)

- [메시지 보내기](https://api.telegram.org/bot[봇토큰]/sendmessage?chat_id=[챗아이디]&text=[보낼메시지])

# 이 앱에 사용자 ID 넣는 법
```python
# project directory로 들어간다.
python
from app import db
db.save_telegram_chat_id("YOUR_ID")

#확인법
print(db.get_telegram_chat_id())
```