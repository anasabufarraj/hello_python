#!./venv/bin/python
# utils/database_json.py
# ------------------------------------------------------------------------------
#  Copyright (c) 2019. Anas Abu Farraj
# ------------------------------------------------------------------------------
"""Storing and retrieving books from a JSON file."""

import json

BOOKS_FILE = 'files/books.json'


def add_book(name, author):
    """Append book with name and author to JSON file.
    
    Read all books from JSON and then save all books
    to the JSON file again.

    :param name: book name
    :type name: str

    :param author: author's name
    :type author: str

    :return: None
    """
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    _write_all_books(books)


def get_all_books():
    """Load all books from the JSON file.

    :return: json file
    :rtype: list of dictionaries
    """
    with open(BOOKS_FILE, 'r') as file:
        return json.load(file)


def _write_all_books(books):
    """Write all books to JSON file.

    :parameter books: list of dictionaries
    :type books: list

    :return: None

    NOTE:
    This function is private and should not be called
    outside this module.
    """
    with open(BOOKS_FILE, 'w') as file:
        json.dump(books, file, indent=4)


def change_to_read(name):
    """Change matched book to read ('1').

    Read all books and mark the matched book with '1' instead of '0'
    and then save all books to the JSON file again.
    It's a bad practice to change date while iterating.

    :parameter name: name of the book
    :type name: str

    :return: None
    """
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True

    _write_all_books(books)


def remove_book(name):
    """Remove book from the JSON file.

    Read all books, rewrite the JSON file without the matched book.

    :parameter name: name of the book
    :type name: str

    :return: None
    """
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _write_all_books(books)
