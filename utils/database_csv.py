#!./venv/bin/python
# utils/database_csv.py
# ------------------------------------------------------------------------------
#  Copyright (c) 2019. Anas Abu Farraj
# ------------------------------------------------------------------------------
"""Storing and retrieving books from a file."""

BOOKS_FILE = 'files/books.csv'


def add_book(name, author):
    """Append book with name and author to file.
    
    :param name: book name
    :type name: str
    
    :param author: author's name
    :type author: str

    :return: None
    """
    with open(BOOKS_FILE, 'a') as file:
        file.write(f'{name},{author},0\n')


def get_all_books():
    """List all books in the file.
    
    :return: list of all books
    :rtype: list
    """
    with open(BOOKS_FILE, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    return [{'name': line[0], 'author': line[1], 'read': line[2]} for line in lines]


def _write_all_books(books):
    """Write all  books to file.

    :parameter books: list of dictionaries
    :type books: list

    :return: None

    **Note**
    Private function, should not be call outside the module.
    """
    with open(BOOKS_FILE, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def change_to_read(name):
    """Change matched book to read ('1').
    
    Read all books and mark the matched book with '1' instead of '0'
    and then save all books to the file again.
    It's a bad practice to change date while iterating.
    
    :parameter name: name of the book
    :type name: str
    
    :return: None
    """
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'

    _write_all_books(books)


def remove_book(name):
    """Remove book from the file.
    
    Read all books, rewrite the file without the matched book.
    
    :parameter name: name of the book
    :type name: str
    
    :return: None
    """
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _write_all_books(books)
