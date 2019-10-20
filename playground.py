#!./venv/bin/python3.7
# Copyright 2019. Anas Abu Farraj
# Learning Python


def words_starts_with_p(word):
    """Function that returns True."""
    return word.startswith('p')


items = 'apple', 'orange', 'pear', 'pineapple', 'banana'
words_iterator = filter(words_starts_with_p, items)

for n in words_iterator:
    print(n)
