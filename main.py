import requests
import time
import random
import os

TOKEN = os.getenv("8647508858:AAFLsdlgvgiFEPGm4f5M8JoToQ7nYkLZ4Ms") or "YOUR_TOKEN"
CHAT_ID = os.getenv("-1003993079945") or "YOUR_CHAT_ID"

sizes = ["BIG", "SMALL"]
colors = ["RED", "GREEN", "VIOLET"]
numbers = [str(i) for i in range(10)]

def generate_signal():
    size = random.choice(sizes)
    color = random.choice(colors)
    number = random.choice(numbers)

    message = f"""ARIYAN BHAI!! 👋
SIZE : {size} 📏
COLOUR : {color} 🎨
NUMBER : {number} 🔢
"""
    return message

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

while True:
    send_message(generate_signal())
    time.sleep(30)  # 30 seconds delay
