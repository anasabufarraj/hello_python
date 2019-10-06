#!./venv/bin/python3.7
# Copyright 2019. Anas Abu Farraj
# Learning Python

import json

with open('files/books.json', 'r') as file:
    print(json.load(file))
