from multiprocessing.managers import Value

import telebot
from telebot import types


token = '7655017751:AAGd642Q4NM9tmTyCg1ScB8tQBeCyVO89vc'
bot = telebot.TeleBot(token)

filename= "bot_message.txt"
file_number = "bot_number.txt"


def f1(v):
    try:
        int(v)
        return True
    except ValueError:
        return False


@bot.message_handler(content_types=['text'])     # /open
def is_text(message):
    if not f1 (message.text):
        filename = "bot_text.txt"
    else:
        filename = "bot_number.txt"

    with open(filename, 'a') as file:
        file.write(message.text + '\n')
    bot.send_message(message.chat.id, 'Збережено до файла!')


if __name__ == '__main__':
    bot.polling()
