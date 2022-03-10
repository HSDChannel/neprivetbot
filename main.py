import telebot
from telebot import types
from retry import retry

@retry()
def make_trouble():
    '''Retry until succeed'''

token = 'your_token'
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, 'Для начала, напишите мне "Привет" (без кавычек).')

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=='Привет':
        photo = open('info.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'https://neprivet.ru')

    if message.text=='привет':
        photo = open('info.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'https://neprivet.ru')

    if message.text=='Ку':
        photo = open('info.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'https://neprivet.ru')

    if message.text=='ку':
        photo = open('info.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'https://neprivet.ru')
bot.infinity_polling()