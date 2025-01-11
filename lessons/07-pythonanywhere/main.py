import telebot
from telebot import types

token = '7655017751:AAGd642Q4NM9tmTyCg1ScB8tQBeCyVO89vc'
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])     # /open
def is_text(message):
    bot.send_message(message.chat.id, message.text + '\n[Бот працює]')


if __name__ == '__main__':
    bot.polling()







