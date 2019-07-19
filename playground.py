#!/usr/local/bin/python3
# Copyright 2019. Anas Abu Farraj
""" Python Learning Project """

import time

try:
    with open('files/filename.txt', 'r') as src:
        FILE_DATA = src.read()
        """ writing text data to file """
        with open('files/file_new.txt', 'w') as dist:
            dist.write(FILE_DATA + '\n...done\n')

except FileNotFoundError:
    print('File not found')

for items in dir(time):
    print(items.strip('\n'))
