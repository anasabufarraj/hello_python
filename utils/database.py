#!./venv/bin/python3
# Copyright 2019. Anas Abu Farraj
"""Storing and retrieving books from a list."""

BOOKS_FILE = 'files/books.txt'


def add_book(name, author):
    """Append book with name and author to file.
    
    :param name: book name
    :type name: string
    
    :param author: author's name
    :type author: string
    """
    with open(BOOKS_FILE, 'a') as file:
        file.write(f'{name},{author},0\n')
    # BOOKS.append({'name': name, 'author': author, 'read': False})


def get_all_books():
    """List all books in the file."""
    with open(BOOKS_FILE, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    return [{
        'name': line[0],
        'author': line[1],
        'read': line[2]
    } for line in lines]

    # if not BOOKS:
    #     print('No Stored Books...')
    #
    # for n, book in enumerate(BOOKS, 1):
    #     state = 'YES' if book['read'] else 'NO'
    #     print(
    #         f"{[n]} - {book['name'].capitalize()}, by {book['author'].capitalize()} - Read: {state}"
    #     )


def change_to_read(name):
    """Mark book as 'read' in database."""
    for book in BOOKS:
        if book['name'] == name:
            book['read'] = True
        else:
            print('No book with this name!')


def change_to_unread(name):
    """Mark book as 'unread' in database."""
    for book in BOOKS:
        if book['name'] == name:
            book['read'] = False
        else:
            print('No book with this name!')


def remove_book(name):
    """Remove book from the list.
    
    Using list comprehension to move each books to a new 
    list except the one match deletion.
    """
    global BOOKS
    BOOKS = [book for book in BOOKS if book['name'] != name]

    # Bad practice:
    # To remove items while iterating:
    # for book in BOOKS:
    #     if book['name'] == name:
    #         BOOKS.remove(book)
