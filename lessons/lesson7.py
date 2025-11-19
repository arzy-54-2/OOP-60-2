import sqlite3

# A4 - Бумага
connect = sqlite3.connect('users.db')
# Рука с карандашом
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (20) NOT NULL,
    age INTEGER NOT NULL,
    hobby TEXT
    )
''')
connect.commit()


# CRUD - Create Read Update Delete

def create_user(name, age, hobby):
    # cursor.execute(f"INSERT INTO users(name, age, hobby) VALUES('{name}', {age}, '{hobby}')")

    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES(?, ?, ?)',
        (name, age, hobby)
    )

    connect.commit()
    print("Пользователь добавлен!!!")

# create_user("John", 16, "Горы")
# create_user("Oleg", 33, "Плавать")
# create_user("ARdager", 26, "Плавать")


def read_users():
    cursor.execute('SELECT name, age FROM users')
    users = cursor.fetchall()

    print(users)
    # for i in users:
        # print(f"NAME: {i[0]} AGE: {i[1]}")

def detail_user(id):
    cursor.execute(
        'SELECT name, age, hobby FROM users WHERE id = ?',
        (id,)
    )
    user = cursor.fetchone()

    print(user)

detail_user(1)

# read_users()


def update_user(name, id):
    cursor.execute(
        'UPDATE users SET name = ? WHERE id = ?',
        (name, id)
    )
    connect.commit()
    print(f"Пользователь с id {id} обновлен!!!")

# update_user("Nikita", 3)

def delete_user(id):
    cursor.execute('DELETE FROM USERS WHERE id = ?', (id,))
    connect.commit()
    print(f"Пользователь с id {id} удален!!!")


# delete_user(2)


