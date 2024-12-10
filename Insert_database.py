import random
import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# for i in range(10):
#    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#               (f"User{i}", f"example{i}@gmail.com", f"{i*10}", f"{1000}"))

# for i in range(10):
#     if i % 2 == 0:
#         cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"User{i}"))

# for i in range(10):
#     if i % 3 == 0 or i == 0:
#         cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{i}",))

cursor.execute("SELECT username, email, age, balance FROM Users GROUP BY AGE")
users = cursor.fetchall()
for user in users:
    if user[2] != 60:
        print(f"Имя: {user[0]}, email: {user[1]}, Возраст: {user[2]}, Баланс: {user[3]}")

connection.commit()
connection.close()