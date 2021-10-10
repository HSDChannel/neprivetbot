import telebot
from telebot import types

token = 'your_token'
bot=telebot.TeleBot(token)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=='Привет':
        photo = open('info.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'https://neprivet.ru')
bot.infinity_polling(interval=0, timeout=20)
