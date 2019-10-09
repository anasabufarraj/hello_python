#!./venv/bin/python3
# Copyright 2019. Anas Abu Farraj
"""Storing and retrieving books from database."""

import sqlite3


def commit_and_close(connection):
    connection.commit()
    connection.close()


def create_table():
    """Creates books table in the database."""
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)'
    )

    commit_and_close(connection)


def add_book(name, author):
    """Add book with name and author to database.

    :param name: name of the book
    :type name: str

    :param author: author's name
    :type author: str
    
    Note:
    To avoid injection attack by using (?, ?),(name, author) syntax,
    instead of ("{name}", "{author}").
    For example:
    If the attacker inserts ",0); DROP TABLE books; for 'author' parameter, 
    this will Delete 'books' table entirely.
    """
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO books VALUES(?, ?, 0)', (name, author))

    commit_and_close(connection)


# FIXME: change all functions to use sqlite3
def get_all_books():
    """Load all books from the database.

    :return: json file
    :rtype: list of dictionaries
    """
    with open(BOOKS_FILE, 'r') as file:
        return json.load(file)


def _write_all_books(books):
    """Write all books to database.

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
    and then save all books to the database again.
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
    """Remove book from the database.

    Read all books, rewrite the database without the matched book.

    :parameter name: name of the book
    :type name: str

    :return: None
    """
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _write_all_books(books)
