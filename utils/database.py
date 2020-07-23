#!./venv/bin/python
# utils/database.py
# ------------------------------------------------------------------------------
#  Copyright (c) 2019. Anas Abu Farraj
# ------------------------------------------------------------------------------
"""Storing and retrieving books from SQLite database."""

import sqlite3

from utils.database_connection import DatabaseConnection
from typing import List, Dict, Union


def create_table() -> None:
    """Creates books table in the database."""
    with DatabaseConnection('data.sqlite') as connection:
        cursor = connection.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS books ( name TEXT PRIMARY KEY, author TEXT, read INTEGER )'
        )


def add_book(name: str, author: str) -> None:
    """Add book with name and author to database.
    
    :param name: name of the book    
    :param author: author's name
    
    Note:
    To avoid injection attack by using (?, ?),(name, author) syntax,
    instead of ("{name}", "{author}"). For example, if the attacker
    inserts ",0); DROP TABLE books; as the value for 'author' parameter,
    the 'books' table will entirely be deleted.
    """
    with DatabaseConnection('data.sqlite') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute('INSERT INTO books VALUES ( ?, ?, 0 )', (name, author))
        except sqlite3.IntegrityError:
            print('Book already exists!')


def get_all_books() -> List[Dict[str, Union[str, int]]]:
    """Load all books from the database
    
    Storing fetched data in variable as list comprehension,
    while each row in database is a tuple,
    i.e. [(name, author, read), (name, author, read)...]
    """
    with DatabaseConnection('data.sqlite') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books ORDER BY name')

        rows = [{
            'name': row[0],
            'author': row[1],
            'read': row[2]
        } for row in cursor.fetchall()]

        return rows


def change_to_read(name: str) -> None:
    """Change matched book name to read ('1').
    
    Select all books and set only the matched name
    read value to '1' instead of '0'.

    :parameter name: name of the book
    
    Important:
    Even if you have a single parameters in the query, it must be
    explicitly declared in tuple, otherwise a programmatic error
    will be thrown, i.e. (name, ).
    """
    # TODO: send a message to the user if the book to update is not exists.
    with DatabaseConnection('data.sqlite') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read = 1 WHERE name = ?', (name, ))


def remove_book(name: str) -> None:
    """Remove book from the database.
        
    :parameter name: name of the book
    """
    # TODO: send a message to the user if the book to delete is not exists.
    with DatabaseConnection('data.sqlite') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name = ?', (name, ))
