import requests


def send_telegram_message(chat_id, message):
    """A function to send a message to Telegram."""
    token = "BOT_TOKEN"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    response = requests.post(url, data=data)
    return response.json()
