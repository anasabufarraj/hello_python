#!./venv/bin/python3.7
# Copyright 2019. Anas Abu Farraj
# Learning Python

import pymysql

connection = pymysql.connect(host='localhost',
                             db='data_source',
                             user='root',
                             password='password')
cursor = connection.cursor()
cursor.execute('SELECT * FROM ca_pop WHERE year LIKE "%19" LIMIT 12')

rows = cursor.fetchall()  # Tuple of tuples
connection.close()


def func():
    for row in rows:
        print(row)


func()
