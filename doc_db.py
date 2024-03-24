import sqlite3

# Введение в БД, работа с SQL-таблицами и отображение данных в PyQT. Часть 1
base_name = 'db.db'
con = sqlite3.connect(base_name)
cur = con.cursor()
result = cur.execute(f"""тело запроса с фигурными скобками, у строк не забыть '' """"").fetchall()
