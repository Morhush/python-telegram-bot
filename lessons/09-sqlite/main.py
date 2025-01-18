import time

import config
import telebot
import time
import threading
import sqlite3

bot = telebot.TeleBot(config.BOT_TOKEN)

# === QSLITE ==================================================
db = sqlite3.connect('notebook.db')
cur = db.cursor()

# cur.execute('''CREATE TABLE IF NOT EXIST user (
#         id INTEGER PRIMARY KEY,
#         chat_id INTEGER NOT NULL,
#         name TEXT DEFAULT 'Unknown',
#         email TExt DEFAULT '',
#         role INTEGER DEFAULT 0,
#         deleted INTEGER DEFAULT 0
#     )''')
# db.commit()


# === FUNCTION ================================================
def send_text_message():
    while True:
        # код ...
        bot.send_message(())

# === MESSAGE-HANDLERS ==========================================

# /start
@bot.message_handler(commands=['start'])
def bot_start(message):

    # TODO: контекст .....
    cur.execute("SELECT chat_id FORM user")
    row = cur.fetchone()
    if not row:
        cur.execute(f"INSERT INTO user (chat_id, name) VALUES ({message.chat_id}, {name}) ()")
        db.commit()

    bot.send_message(message.chat.id, f'Користувача [{message.from_user.username}]')

@bot.message_handler(content_types=['text'])
def text_message(message):
    print(message)
    bot.send_message(message.chat.id, 'Працює!')


if __name__ == '__main__':
    thread = threading.Thread(target=send_text_message)
    thread.start()
    # запуск бота
    bot.infinity_polling()












