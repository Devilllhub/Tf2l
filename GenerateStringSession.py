from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""Please go-to my.telegram.org for details""")
APP_ID = int(input("19972681"))
API_HASH = input("2f3c727cedf7472a67b3151f5f652268")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
