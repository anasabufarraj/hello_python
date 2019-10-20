#!./venv/bin/python3.7
# Copyright 2019. Anas Abu Farraj
# Learning Python

import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             db='data_source')
cursor = connection.cursor()
cursor.execute("SELECT * FROM ca_pop WHERE year LIKE '%19' LIMIT 12")

data_list = cursor.fetchall()

for row in data_list:
    print(row)
