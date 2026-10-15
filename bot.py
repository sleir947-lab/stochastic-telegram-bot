


import os
import requests

token = os.getenv("8680702032:AAEm2ROI15ko_Xe8ptw-CMtTmd5D18SAsyg")
chat_id = os.getenv("767353805")

if not token or not chat_id:
    raise ValueError("Brakuje TELEGRAM_TOKEN lub CHAT_ID w GitHub Secrets")

url = f"https://api.telegram.org/bot{token}/sendMessage"

response = requests.post(
    url,
    json={
        "chat_id": chat_id,
        "text": "✅ Test bota działa! GitHub Actions połączony z Telegramem."
    },
    timeout=15
)

response.raise_for_status()
result = response.json()

if not result.get("ok"):
    raise RuntimeError(f"Telegram API error: {result}")

print("Wiadomość testowa została wysłana.")
