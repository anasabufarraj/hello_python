#!./venv/bin/python3.7
# Copyright 2019. Anas Abu Farraj

try:
    a = int('hello')
except ValueError:
    print('Oops! Invalid number.')
finally:
    print('Hello, will be printed anyway.')

# Oops! Invalid number.
# Hello, will be printed anyway.