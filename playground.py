#!./venv/bin/python3.7
# Copyright 2019. Anas Abu Farraj
# Learning Python

import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()
cursor.execute('SELECT * FROM books')

row1 = cursor.fetchmany(1)
row2 = cursor.fetchmany(1)
row3 = cursor.fetchmany(1)

connection.close()

print(row1)
print(row2)
print(row3)

# ('The Pragmatic Programmer', 'Andy Hunt', 0)
