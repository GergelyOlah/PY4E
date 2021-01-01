import sqlite3

conn = sqlite3.connect('Assigment_15_2.sqlite')
cur = conn.cursor()

# cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('CREATE TABLE Ages (name VARCHAR(128), age INTEGER)')

