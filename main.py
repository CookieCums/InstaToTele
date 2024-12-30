from telethon import TelegramClient
from dotenv import load_dotenv
import os
import pyperclip
import time
import re

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
RECIPIENT_USERNAME = os.getenv("Receiver_Username")

last_sent_text = None

def send_message(text):
    client = TelegramClient("session_name", API_ID, API_HASH)
    async def main():
        await client.start()
        await client.send_message(RECIPIENT_USERNAME, text)
        print("Message sent successfully: ", text)
    with client:
        client.loop.run_until_complete(main())
      
def monitor_clipboard():
    global last_sent_text
  
    instagram_reel_pattern = r'https://www\.instagram\.com/(reel|reels)/[A-Za-z0-9_-]+/?'
  
    while True:
        try:
            current_text = pyperclip.paste()
            if current_text and current_text != last_sent_text:
                if re.match(instagram_reel_pattern, current_text):
                    last_sent_text = current_text
                    send_message(current_text)
            time.sleep(1)
        except Exception as e:
            print("An error occurred:", e)
          
if __name__ == "__main__":
    print("Monitoring clipboard for new copied text...")
    monitor_clipboard()  
