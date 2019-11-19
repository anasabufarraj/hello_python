#!./venv/bin/python3
# utils/database_memory.py
# ------------------------------------------------------------------------------
#  Copyright (c) 2019. Anas Abu Farraj
# ------------------------------------------------------------------------------
"""Storing and retrieving books from a list."""

BOOKS = []


def add_book(name, author):
    """Append book with name and author to list.
    
    :param name: book name
    :type name: string
    
    :param author: author's name
    :type author: string
    """
    BOOKS.append({'name': name, 'author': author, 'read': False})


def get_all_books():
    """List all books in the file."""
    for n, book in enumerate(BOOKS, 1):
        state = 'YES' if book['read'] else 'NO'
        print(
            f"{[n]} - {book['name'].capitalize()}, by {book['author'].capitalize()} - Read: {state}"
        )


def change_to_read(name):
    """Mark book as 'read' in database."""
    for book in BOOKS:
        if book['name'] == name:
            book['read'] = True
        else:
            print('No book with this name!')


def change_to_unread(name):
    """Mark book as 'unread' in the list."""
    for book in BOOKS:
        if book['name'] == name:
            book['read'] = False
        else:
            print('No book with this name!')


def remove_book(name):
    """Remove book from the list.
    
    Using list comprehension to move each books to a new 
    list except the one match deletion.
    It's a bad practice to remove items while iterating. For example:
    
    for book in BOOKS:
         if book['name'] == name:
             BOOKS.remove(book)
    """
    global BOOKS
    BOOKS = [book for book in BOOKS if book['name'] != name]
