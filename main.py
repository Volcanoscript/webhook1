from flask import Flask
import threading
import time
import requests
import os

app = Flask(__name__)

# Your webhook URL (set in Render "Environment Variables")
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# Your default message (you can edit anytime)
MESSAGE = "@everyone Join now! New Roblox Condo[https*:*//www.roblox.com/games/132560227965463/Neko?privateServerLinkCode=79949483018803329508950212279688](https://rbx-url.com/W-UggYLz)"

# Interval in seconds (example: 600 = 10 minutes, 60 = 1 minute)
INTERVAL_SECONDS = 600  

def send_webhook():
    while True:
        try:
            payload = {"content": MESSAGE, "allowed_mentions": {"parse": ["everyone"]}}
            r = requests.post(WEBHOOK_URL, json=payload, timeout=10)
            print("Status:", r.status_code, "| Response:", r.text)
        except Exception as e:
            print("❌ Error:", e)
        time.sleep(INTERVAL_SECONDS)

@app.route("/")
def home():
    return "✅ Bot is running and sending webhooks!"

# Start webhook loop in background
threading.Thread(target=send_webhook, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
