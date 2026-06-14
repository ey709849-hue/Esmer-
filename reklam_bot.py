import os
import time
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_IDS = os.environ["CHAT_IDS"].split(",")

# Buraları kendin doldur:
IMAGE_URL = "BURAYA_RESIM_LINKI"
CAPTION = "BURAYA_ACIKLAMA_VE_WHATSAPP_LINKI"

INTERVAL_SECONDS = 300  # 5 dakika

def send_ad():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    for chat_id in CHAT_IDS:
        data = {"chat_id": chat_id.strip(), "caption": CAPTION}
        params = {"photo": IMAGE_URL}
        resp = requests.post(url, data=data, params=params)
        print(chat_id, resp.status_code, resp.text)
        time.sleep(2)

if __name__ == "__main__":
    while True:
        send_ad()
        time.sleep(INTERVAL_SECONDS)
