from flask import Flask, request
import os
import requests

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    message = data.get("message", "No message received.")
    if BOT_TOKEN and CHAT_ID:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": f"{message}"
        }
        requests.post(url, json=payload)
        return "OK", 200
    else:
        return "Missing environment variables", 400

@app.route("/", methods=["GET"])
def home():
    return "Webhook is running.", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
