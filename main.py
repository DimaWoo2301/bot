import telebot
import os
import requests
from dotenv import load_dotenv
load_dotenv() # Подрузка дот инви
bot = telebot.TeleBot(os.getenv('BOT_KEY'),) #Создание бота

PogodaKey = os.getenv('POGODA_KEY') # Ключ погоды
BASE_URL = f'https://api.openweathermap.org/data/2.5/weather?lang=ru' # Адрес сайта
def get_pogoda(city_name):# 
    zapros = requests.get(f'{BASE_URL}&q={city_name}&appid={PogodaKey}') # Получения данных погоды с сайта
    data = zapros.json() # Считывание json 
    if data['cod'] == '404': # Если что ошибкучку скинет
        raise Exception(f"ЭЭЭЭ дарагой, ти попутал радной эжи,такого горада {city_name} не будет🙉") 

    pogoda = data['weather'][0]['description'] # Получение описание
    t = round(data['main']['temp'] - 273)
    face_feel = round(data['main']['feels_like'] - 273)

    return {
        'city': data['name'],
        'pogoda': pogoda,
        't': t,
        'face_feel': face_feel
    }

@bot.message_handler(commands=['start']) 
def send_welcome(message):
    bot.send_message(message.chat.id, '🙊Салам Алекум, напищи горад и я тэбе скажю пагоду!🙉', parse_mode='html')

@bot.message_handler(content_types=['text']) # обработка сообщения(Текст)
def weather_handler(message):
    t_smile = '☀'
    p_smile = '☀'
    f_smile = '😸'
    try:
        data = get_pogoda(message.text)
        if data['t'] <= 0 : 
            t_smile = '❄'
        if data['pogoda'] == 'пасмурно':
            p_smile = '☔'
        if data['pogoda'] == 'облочно':
            p_smile = '☁'
        if data['pogoda'] == 'переменная облачность':
            p_smile = '⛅'
        if data['pogoda'] == 'небольшая облачность':
            p_smile = '⛅'    
        if data['face_feel'] <= 0 : 
            f_smile = '😿'

        bot.send_message(message.chat.id,
        
                            f'⛪Город: {data["city"]}\n'
                            f'{p_smile}Погода: {data["pogoda"]}\n'
                            f'{t_smile}Температура: {data["t"]}\n'
                            f'{f_smile}Ощущение: {data["face_feel"]}'
                            )

    except Exception as err: # Вывод ошибки бото
        bot.send_message(message.chat.id, err)
print('Бот запущен')
bot.polling()