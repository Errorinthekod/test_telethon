import logging
from telethon import TelegramClient, events, connection 
from dotenv import load_dotenv


import os
load_dotenv() # loading env vars

# Setup logging
LOGGING = os.getenv("LOGGING")
if LOGGING:
    logging.basicConfig(level=logging.INFO)


# Your API ID and hash from my.telegram.org
# TODO: get api keys
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_API_TOKEN")  # Replace with your actual bot token

# Create the client and connect
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,




# Handler for the /start command
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Hello! I am a Telethon bot. How can I assist you today?')
    logging.info(f'Start command received from {event.sender_id}')


@client.on(events.NewMessage(pattern='/advice'))
async def advice(event):
    if event.sender_id == "5505163057":
        await event.respond('You are doing well AT')
    else:
        await event.respond('The strongest ones also need some rest.')
    logging.info(f"Advice command received from {event.sender_id}")


# Handler for the /help command
@client.on(events.NewMessage(pattern='/help'))
async def help(event):
    help_text = (
        "Here are the commands you can use:\n"
        "/start - Start the bot\n"
        "/help - Get help information\n"
        "/info - Get information about the bot\n"
        "/echo <message> - Echo back the message\n"
    )
    await event.respond(help_text)
    logging.info(f'Help command received from {event.sender_id}')

# Handler for the /info command
@client.on(events.NewMessage(pattern='/info'))
async def info(event):
    await event.respond('This bot is created using Telethon in Python. It can respond to various commands and messages.')
    logging.info(f'Info command received from {event.sender_id}')

# Handler for the /echo command
@client.on(events.NewMessage(pattern='/echo (.+)'))
async def echo(event):
    message = event.pattern_match.group(1)
    await event.respond(f'Echo: {message}')
    logging.info(f'Echo command received from {event.sender_id} with message: {message}')

# Keyword-based response handler
@client.on(events.NewMessage)
async def keyword_responder(event):
    message = event.text.lower()

    responses = {
        'hello': 'Hi there! How can I help you today?',
        'how are you': 'I am just a bot, but I am here to assist you!',
        'what is your name': 'I am MyAwesomeBot, your friendly Telegram assistant.',
        'bye': 'Goodbye! Have a great day!',
        'time': 'I cannot tell the current time, but you can check your device!',
        'date': 'I cannot provide the current date, but your device surely can!',
        'weather': 'I cannot check the weather, but there are many apps that can help you with that!',
        'thank you': 'You are welcome!',
        'help me': 'Sure! What do you need help with?',
        'good morning': 'Good morning! I hope you have a great day!',
        'good night': 'Good night! Sweet dreams!',
        'who created you': 'I was created by a developer using the Telethon library in Python.',
    }

    response = responses.get(message, None)

    if response:
        await event.respond(response)
    else:
        # Default response
        default_response = (
            "I didn't understand that command. Here are some commands you can try:\n"
            "/start - Start the bot\n"
            "/help - Get help information\n"
            "/info - Get information about the bot\n"
            "/echo <message> - Echo back the message\n"
        )
        await event.respond(default_response)
    logging.info(f'Message received from {event.sender_id}: {event.text}')

# Start the client
client.start()
client.run_until_disconnected()



