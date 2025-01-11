import sqlite3

con = sqlite3.connect('test1.db')
cur = con.cursor()

# Робота з БД ...........

# cur.execute("CREATE TABLE user(name, year, title);")
# cur.execute(''' CREATE TABLE user_all(
#         id INTEGER PRIMARY KEY,
#         name TEXT DEFAULT 'Невідомий',
#         year INTEGER DEFAULT 0,
#         title TEXT NOT NULL
#     );''')
# con.commit()

# Додати до БД інформацію
name = ' Петрович'
year = 2001
title = '...'
# cur.execute("""INSERT INTO user_1 (name, year, title)"
#     VALUES ({name} 2000, 'Дідусь');""")
# con.commit()
cur.execute(f"""INSERT INTO user_1 (name, year, title)
    VALUES (?, ?, ?,);""", (name, year, title,))
con.commit()





con.close()


