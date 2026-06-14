import os
import time
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_IDS = os.environ["CHAT_IDS"].split(",")

IMAGE_FILE_ID = "AgACAgQAAxkBAAMEai4T-a20_uR-6NDKnxmjAitfAY0AAqsMaxsnnHFRhQsByueTE0QBAAMCAAN5AAM8BA"
CAPTION = (
    "🔥 ÖDEME ELDEN NAKİT\n"
    "İsmim esmer\n\n"
    "Yaşım 25\n\n\n\"
    " Boyum  160\n\n\n\n\"
    "Kilom  50\n\n\n\n\n\"
    "📲 WhatsApp: https://wa.me/90506069369"
)

INTERVAL_SECONDS = 300  # 5 dakika

def send_ad():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    for chat_id in CHAT_IDS:
        data = {
            "chat_id": chat_id.strip(),
            "photo": IMAGE_FILE_ID,
            "caption": CAPTION,
        }
        resp = requests.post(url, data=data)
        print(chat_id, resp.status_code, resp.text)
        time.sleep(2)

if __name__ == "__main__":
    while True:
        send_ad()
        time.sleep(INTERVAL_SECONDS)
