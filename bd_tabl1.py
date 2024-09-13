import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(  
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER
)
''')
cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",('User1', 'example1@gmail.com', '10', '1000'))
#for i in range(1, 11):
    #cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                    #(f'User{i}', f'example{i}@gmail.com', f'{i*10}', 1000))

#cursor.execute('SELECT id, username, email, age, balance FROM Users')
#users = cursor.fetchall()

#for i, user in enumerate(users):
    #if (i + 1) % 2 != 0:
        #cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, user[0]))

#for i, user in enumerate(users):
    #if (i + 1) % 3 == 1:
        #cursor.execute('DELETE FROM Users WHERE id = ?', (user[0],))

#cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
#users = cursor.fetchall()
#for user in users:
    #print(user)

connection.commit()
connection.close()