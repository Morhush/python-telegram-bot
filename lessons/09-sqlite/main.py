import time
import config as c
import config
import telebot
import time
from SQliteManager import SQLNote
import threading

bot = telebot.TeleBot(config.BOT_TOKEN)

# === QSLITE ==================================================
# db = sqlite3.connect('notebook.db')
# cur = db.cursor()

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
def get_db_cursor():
    return SQLNote()

def send_text_message():
    while True:
        # код ...
        bot.send_message('516876967', 'Щось спрацювало')

# === MESSAGE-HANDLERS ==========================================

# start - підписатися
# add - додати
# edit - редагувати
# del - видалити
# help - вивести підказку
# all - показати усі нотатки
# end - відписатися

# /start
@bot.message_handler(commands=['start'])
def bot_start(message):
    with get_db_cursor() as cur:
        cur.execute("SELECT chat_id FROM user WHERE chat_id='%d'" % message.chat.id)
        row = cur.fetchone()

        if not row:
            cur.execute(f"INSERT INTO user (chat_id, name) VALUES ('{message.chat_id}', '{message.from_user.username}') ()")
            bot.send_message(message.chat.id, f'Користувача [{message.from_user.username}] додано!')
        else:
            bot.send_message(message.chat.id, 'Ви вже підписалися на цього бота')


@bot.message_handler(content_types=['text'])
def text_message(message):
    print(message)
    bot.send_message(message.chat.id, 'Працює!')


if __name__ == '__main__':
    # thread = threading.Thread(target=send_text_message)
    # thread.start()
    # запуск бота
    bot.infinity_polling()












