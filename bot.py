import time
import os
import telebot
import sys

try:
    token = os.environ["BOT_TOKEN"]
    chat_id = os.environ["CHAT_TOKEN"]
except KeyError:
    print("You must set BOT_TOKEN & CHAT_TOKEN environment variable \n\nexport BOT_TOKEN=your_telegram_token & export CHAT_TOKEN=your_chat_id")
    sys.exit(1)

bot = telebot.TeleBot(token, parse_mode="MARKDOWN")

def send_message(message_data):
    bot.send_message(chat_id, message_data)

