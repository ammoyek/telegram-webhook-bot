from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route("/", methods=["POST"])
def handle_webhook():
    data = request.json
    message = data.get("message", "📡 Yeni sinyal geldi ancak mesaj içeriği boş.")

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f"📬 TradingView Sinyali:\n\n{message}"
    }

    requests.post(telegram_url, json=payload)
    return "OK", 200
