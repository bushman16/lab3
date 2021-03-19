import telebot
import requests
import json
import time

d = {}
c = {}
b = {}
g = {}
f = {}

bot = telebot.TeleBot('1625005510:AAE4gXNVgpJM8r7ILVJu24dJdgtUBnE-5TY')
keyboard3 = telebot.types.ReplyKeyboardMarkup()
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('EUR', 'RUB', 'USD', 'AUD', 'BRL', 'CAD', 'CHF', 'CLP', 'CNY', 'DKK', 'GBP', 'HKD', 'INR', 'ISK', 'JPY', 'KRW', 'NZD', 'PLN', 'SEK', 'SGB', 'THB', 'TRY', 'TWD', 'назад')
keyboard3.row('узнать курс', 'выводить курс каждые 5 минут', 'узнать изменения с последнего запроса')
keyboard2.row('EUR5', 'RUB5', 'USD5', 'AUD5', 'BRL5', 'CAD5', 'CHF5', 'CLP5', 'CNY5', 'DKK5', 'GBP5', 'HKD5', 'INR5', 'ISK5', 'JPY5', 'KRW5', 'NZD5', 'PLN5', 'SEK5', 'SGB5', 'THB5', 'TRY5', 'TWD5', 'назад')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, 'Приветствую!\n'
                                           'Этот бот предназначен для поиска курса биткоина по необходимой вам валюте.\n'
                                           'Выберите интересующую вас валюту на клавиатуре.', reply_markup=keyboard3)

@bot.message_handler(content_types=['text'])
def get_text_massages(message):
    if message.text.lower() == 'rub' or 'eur' or 'usd' or 'aud' or 'brl' or 'cad' or 'chf' or 'clp' or 'cny' or 'dkk' or 'gbp' or 'hkd' or 'inr' or 'isk' or 'jpy' or 'krw' or 'nzd' or 'pln' or 'sek' or 'sgb' or 'thb' or 'try' or 'twd':
        b = requests.get('https://blockchain.info/ru/ticker').text
        d = json.loads(b)
        с = message.text
        for key in d:
            if key == message.text:
                c = json.dumps(d[key])
                bot.send_message(message.from_user.id, text=key + c, reply_markup=keyboard1)

    if message.text.lower() == 'rub5':
        b = requests.get('https://blockchain.info/ru/ticker').text
        d = json.loads(b)
        while True:
            for key in d:
                if key == 'RUB':
                    c = json.dumps(d[key])
                    bot.send_message(message.from_user.id, text=key + c, reply_markup=keyboard2)
            time.sleep(300)

    if message.text.lower() == 'eur5':
        b = requests.get('https://blockchain.info/ru/ticker').text
        d = json.loads(b)
        while True:
            for key in d:
                if key == 'EUR':
                    c = json.dumps(d[key])
                    bot.send_message(message.from_user.id, text=key + c, reply_markup=keyboard2)
            time.sleep(300)

    if message.text.lower() == 'usd5':
        b = requests.get('https://blockchain.info/ru/ticker').text
        d = json.loads(b)
        while True:
            for key in d:
                if key == 'USD':
                    c = json.dumps(d[key])
                    bot.send_message(message.from_user.id, text=key + c, reply_markup=keyboard2)
            time.sleep(300)

    if message.text.lower() == 'aud5':
        b = requests.get('https://blockchain.info/ru/ticker').text
        d = json.loads(b)
        while True:
            for key in d:
                if key == 'AUD':
                    c = json.dumps(d[key])
                    bot.send_message(message.from_user.id, text=key + c, reply_markup=keyboard2)
            time.sleep(300)

    if message.text.lower() == 'brl5':
        b = requests.get('https://blockchain.info/ru/ticker').text
        d = json.loads(b)
        while True:
            for key in d:
                if key == 'BRL':
                    c = json.dumps(d[key])
                    bot.send_message(message.from_user.id, text=key + c, reply_markup=keyboard2)
            time.sleep(300)

    if message.text.lower() == 'cad5':
        b = requests.get('https://blockchain.info/ru/ticker').text
        d = json.loads(b)
        while True:
            for key in d:
                if key == 'CAD':
                    c = json.dumps(d[key])
                    bot.send_message(message.from_user.id, text=key + c, reply_markup=keyboard2)
            time.sleep(300)

    if message.text.lower() == 'chf5':
        b = requests.get('https://blockchain.info/ru/ticker').text
        d = json.loads(b)
        while True:
            for key in d:
                if key == 'CHF':
                    c = json.dumps(d[key])
                    bot.send_message(message.from_user.id, text=key + c, reply_markup=keyboard2)
            time.sleep(300)

    if message.text.lower() == 'clp5':
        b = requests.get('https://blockchain.info/ru/ticker').text
        d = json.loads(b)
        while True:
            for key in d:
                if key == 'CLP':
                    c = json.dumps(d[key])
                    bot.send_message(message.from_user.id, text=key + c, reply_markup=keyboard2)
            time.sleep(300)

    if message.text.lower() == 'cny5':
        b = requests.get('https://blockchain.info/ru/ticker').text
        d = json.loads(b)
        while True:
            for key in d:
                if key == 'CNY':
                    c = json.dumps(d[key])
                    bot.send_message(message.from_user.id, text=key + c, reply_markup=keyboard2)
            time.sleep(300)

    if message.text.lower() == 'dkk5':
        b = requests.get('https://blockchain.info/ru/ticker').text
        d = json.loads(b)
        while True:
            for key in d:
                if key == 'DKK':
                    c = json.dumps(d[key])
                    bot.send_message(message.from_user.id, text=key + c, reply_markup=keyboard2)
            time.sleep(300)

    if message.text.lower() == 'gbp5':
        b = requests.get('https://blockchain.info/ru/ticker').text
        d = json.loads(b)
        while True:
            for key in d:
                if key == 'GBP':
                    c = json.dumps(d[key])
                    bot.send_message(message.from_user.id, text=key + c, reply_markup=keyboard2)
            time.sleep(300)

    if message.text.lower() == 'hkd5':
        b = requests.get('https://blockchain.info/ru/ticker').text
        d = json.loads(b)
        while True:
            for key in d:
                if key == 'HKD':
                    c = json.dumps(d[key])
                    bot.send_message(message.from_user.id, text=key + c, reply_markup=keyboard2)
            time.sleep(300)

    if message.text.lower() == 'inr5':
        b = requests.get('https://blockchain.info/ru/ticker').text
        d = json.loads(b)
        while True:
            for key in d:
                if key == 'INR':
                    c = json.dumps(d[key])
                    bot.send_message(message.from_user.id, text=key + c, reply_markup=keyboard2)
            time.sleep(300)

    if message.text.lower() == 'isk5':
        b = requests.get('https://blockchain.info/ru/ticker').text
        d = json.loads(b)
        while True:
            for key in d:
                if key == 'ISK':
                    c = json.dumps(d[key])
                    bot.send_message(message.from_user.id, text=key + c, reply_markup=keyboard2)
            time.sleep(300)

    if message.text.lower() == 'jpy5':
        b = requests.get('https://blockchain.info/ru/ticker').text
        d = json.loads(b)
        while True:
            for key in d:
                if key == 'JPY':
                    c = json.dumps(d[key])
                    bot.send_message(message.from_user.id, text=key + c, reply_markup=keyboard2)
            time.sleep(300)

    if message.text.lower() == 'krw5':
        b = requests.get('https://blockchain.info/ru/ticker').text
        d = json.loads(b)
        while True:
            for key in d:
                if key == 'KRW':
                    c = json.dumps(d[key])
                    bot.send_message(message.from_user.id, text=key + c, reply_markup=keyboard2)
            time.sleep(300)

    if message.text.lower() == 'nzd5':
        b = requests.get('https://blockchain.info/ru/ticker').text
        d = json.loads(b)
        while True:
            for key in d:
                if key == 'NZD':
                    c = json.dumps(d[key])
                    bot.send_message(message.from_user.id, text=key + c, reply_markup=keyboard2)
            time.sleep(300)

    if message.text.lower() == 'pln5':
        b = requests.get('https://blockchain.info/ru/ticker').text
        d = json.loads(b)
        while True:
            for key in d:
                if key == 'PLN':
                    c = json.dumps(d[key])
                    bot.send_message(message.from_user.id, text=key + c, reply_markup=keyboard2)
            time.sleep(300)

    if message.text.lower() == 'sek5':
        b = requests.get('https://blockchain.info/ru/ticker').text
        d = json.loads(b)
        while True:
            for key in d:
                if key == 'SEK':
                    c = json.dumps(d[key])
                    bot.send_message(message.from_user.id, text=key + c, reply_markup=keyboard2)
            time.sleep(300)

    if message.text.lower() == 'sgb5':
        b = requests.get('https://blockchain.info/ru/ticker').text
        d = json.loads(b)
        while True:
            for key in d:
                if key == 'SGB':
                    c = json.dumps(d[key])
                    bot.send_message(message.from_user.id, text=key + c, reply_markup=keyboard2)
            time.sleep(300)

    if message.text.lower() == 'thb5':
        b = requests.get('https://blockchain.info/ru/ticker').text
        d = json.loads(b)
        while True:
            for key in d:
                if key == 'THB':
                    c = json.dumps(d[key])
                    bot.send_message(message.from_user.id, text=key + c, reply_markup=keyboard2)
            time.sleep(300)

    if message.text.lower() == 'try5':
        b = requests.get('https://blockchain.info/ru/ticker').text
        d = json.loads(b)
        while True:
            for key in d:
                if key == 'TRY':
                    c = json.dumps(d[key])
                    bot.send_message(message.from_user.id, text=key + c, reply_markup=keyboard2)
            time.sleep(300)

    if message.text.lower() == 'twd5':
        b = requests.get('https://blockchain.info/ru/ticker').text
        d = json.loads(b)
        while True:
            for key in d:
                if key == 'TWD':
                    c = json.dumps(d[key])
                    bot.send_message(message.from_user.id, text=key + c, reply_markup=keyboard2)
            time.sleep(300)

    if message.text.lower() == 'узнать изменения с последнего запроса':
        q = requests.get('https://blockchain.info/ru/ticker').text
        f = json.loads(q)
        if d == f:
            bot.send_message(message.from_user.id, text="курс не изменился", reply_markup=keyboard3)
        elif d != f:
            bot.send_message(message.from_user.id, text="курс изменился", reply_markup=keyboard3)

    if message.text.lower() == 'назад':
        bot.send_message(message.from_user.id, "выберите пункт меню: ", reply_markup=keyboard3)

    if message.text.lower() == 'выводить курс каждые 5 минут':
        bot.send_message(message.from_user.id, "выберите валюту: ", reply_markup=keyboard2)

    if message.text.lower() == 'узнать курс':
        bot.send_message(message.from_user.id, "выберите валюту: ", reply_markup=keyboard1)

bot.polling(none_stop=True, interval=0)