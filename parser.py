from telethon import TelegramClient, events
from dotenv import load_dotenv

import os

from utils.formater import format_message as fmt_msg

load_dotenv()


api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_API_TOKEN")

CHANNELS = [os.getenv("RAGE_TANG_CHANNEL"),
           os.getenv("IT_NOTES_CHANNEL"),]

client = TelegramClient("parser", api_id, api_hash)
parser_mode = True



@client.on(events.NewMessage(pattern = "/start"))
async def start_cmd(event):
    await event.respond("Hello I'm your bot.")


@client.on(events.NewMessage(chats = CHANNELS))
async def chat_handler(event):
    print(fmt_msg(event.message))


if not parser_mode:
    client.start(bot_token=bot_token)
    print("Bot started ...")
else:
    client.start()
    print("Parser started ...")

client.run_until_disconnected()


