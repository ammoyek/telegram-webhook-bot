from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "7841058720:AAG6tnJCt5HmRD8cd7x971HgKNtG8kiIFms"
CHAT_ID = "6914865704"

@app.route("/", methods=["POST"])
def handle_webhook():
    data = request.json
    message = data.get("message", "Yeni sinyal geldi ancak mesaj içeriği boş.")
    print("MESAJ:", message)

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f"✅ TradingView Sinyali:\n\n{message}"
    }

    response = requests.post(telegram_url, json=payload)
    print("TELEGRAM'A GÖNDERİLDİ:", response.status_code, response.text)

    return "OK", 200
