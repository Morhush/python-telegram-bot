import config as c
import telebot
import time
import threading
from SQliteManager import SQLNote


bot = telebot.TeleBot(c.BOT_TOKEN)

# === SQLITE =============================================
# db = sqlite3.connect('notebook.db')
# cur = db.cursor()
#
# cur.execute('''CREATE TABLE users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         chat_id INTEGER NOT NULL,
#         name TEXT DEFAULT 'Невідомий',
#         deleted INTEGER DEFAULT 0
#     )''')
# db.commit()
#
# cur.execute('''CREATE TABLE IF NOT EXISTS notes (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user_id INTEGER NOT NULL,
#         title TEXT NOT NULL,
#         content TEXT DEFAULT '',
#         notification DATETIME DEFAULT CURRENT_TIMESTAMP,
#         is_send INTEGER DEFAULT 0,
#         deleted INTEGER DEFAULT 0
#     )''')
# db.commit()

# === FUNCTIONS ==========================================
def send_text_message():
    while True:
        # код .....
        bot.send_message('516876967', 'Щось спрацювало')
        time.sleep(10)


def get_db_cursor():
    return SQLNote(c.BD_NAME)

def bot_add_title(message):

    # TODO: add note ...........

    bot.send.message(message.chat.id, 'Нотатку додано!')

def bot_start(message):
    print(message)
    with get_db_cursor() as cur:
        cur.execute("SELECT chat_id FROM users WHERE chat_id='%d'" % message.chat.id)
        row = cur.fetchone()

        if not row:
            cur.execute(f"INSERT INTO users (chat_id, name) VALUES ('{message.chat.id}', '{message.from_user.username}')")
            bot.send_message(message.chat.id, f'Користувача [{message.from_user.username}] додано!')
        else:
            bot.send_message(message.chat.id, 'Ви вже підписалися на цього бота')




# === MESSAGE-HANDLERS ===================================

@bot.message_handler(commands=['start', 'add', 'edit', 'del', 'help', 'end'])
def bot_commands(message):
    if '/start' == message.text:
        bot_start(message)
    elif '/add' == message.text:
        bot.send_message(message.chat.id, 'Ведіть Нотатку:')
        bot.register_next_step_handler(message, bot_add_title)
    elif '/edit' == message.text:
        pass

# /start

@bot.message_handler(content_types=['text'])
def text_message(message):
    print(message)
    bot.send_message(message.chat.id, 'Працює!')


if __name__ == '__main__':
    # thread = threading.Thread(target=send_text_message)
    # thread.start()

    # запуск бота
    bot.infinity_polling()
