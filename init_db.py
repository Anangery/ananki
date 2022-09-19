import sqlite3 as sql

connection = sql.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO cards (front, back) VALUES (?, ?)",
    ('First Post', 'Content for First Post')
    )

cur.execute("INSERT INTO name (name) VALUES (?)",
    ('Name of First Post', )
    )

connection.commit()
connection.close() 
