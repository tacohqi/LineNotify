import os
import requests
from datetime import datetime
from dotenv import load_dotenv
import logging

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

    current_day = datetime.now().strftime("%A")
    message = f"Hello! Today is {current_day}. Have a great day!"
    send_line_notify(message)

if __name__ == "__main__":
    main()