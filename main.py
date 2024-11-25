# !!!!!! у себя этот код не запускается, тк нет telebot
from telebot import TeleBot

token = "7743150963:AAHL97qBMIZ-WqwBcZr7zk7LN-0umztXyz8"
bot = TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, пользователь!')


bot.infinity_polling()
