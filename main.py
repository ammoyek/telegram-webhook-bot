from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def handle_webhook():
    data = request.json
    message = data.get("message", "Yeni sinyal geldi ancak mesaj içeriği boş.")
    print("MESAJ:", message)

    telegram_url = f"https://api.telegram.org/bot{os.getenv('BOT_TOKEN')}/sendMessage"
    payload = {
        "chat_id": os.getenv('CHAT_ID'),
        "text": f"📈 TradingView Sinyali:\n\n{message}"
    }

    response = requests.post(telegram_url, json=payload)
    print("TELEGRAM'A GÖNDERİLDİ:", response.status_code, response.text)

    return "OK", 200
