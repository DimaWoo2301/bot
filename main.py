import telebot
import os
from dotenv import load_dotenv


load_dotenv()
bot = telebot.Telebot(os.getenv('BOT_KEY'))

@bot.message_handler(content_types['text'])

def xyi (message):
    bot.send_message('Что нибудь')

bot.polling()

