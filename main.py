import telebot
import os
print(telebot)
from dotenv import load_dotenv


load_dotenv()
bot = telebot.TeleBot(os.getenv('BOT_KEY'))

@bot.message_handler(content_types=['text'])

def xyi (message):
    if message.text.lower() == 'привет': 
        bot.send_message(message.chat.id,'Пока)')
    else:
        bot.send_message(message.chat.id,message.text)
bot.polling()

