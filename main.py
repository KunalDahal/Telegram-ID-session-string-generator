from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'
session_string = 'YOUR_GENERATED_SESSION_STRING'

client = TelegramClient(StringSession(session_string), api_id, api_hash)
await client.start()
