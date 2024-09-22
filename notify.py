import os
import requests
from datetime import datetime
from dotenv import load_dotenv
import logging
from zoneinfo import ZoneInfo

logging.basicConfig(level=logging.INFO)

load_dotenv()
LINE_NOTIFY_TOKEN = os.environ.get('LINE_NOTIFY_TOKEN')

def send_line_notify(message):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {LINE_NOTIFY_TOKEN}'}
    data = {'message': message}
    response = requests.post(url, headers=headers, data=data)
    logging.info(f"Notification sent. Status Code: {response.status_code}")

def main():
    if not LINE_NOTIFY_TOKEN:
        logging.error("Error: LINE_NOTIFY_TOKEN is not set.")
        return

    current_day = datetime.now(ZoneInfo("Asia/Taipei")).strftime("%A")
    current_time = datetime.now(ZoneInfo("Asia/Taipei")).strftime("%H:%M:%S")

    message = f"""
    🕒 Time Check: {current_time}
    📅 Today is {current_day}!!!!
    🌟 Daily Notification:

    ✨ 1. You should provide a weekly report! ✨
    test

    Have a great day! 😊🎉
    """
    send_line_notify(message)

if __name__ == "__main__":
    main()
