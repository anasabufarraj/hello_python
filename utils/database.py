#!./venv/bin/python3
# utils/database.py
# Copyright 2019. Anas Abu Farraj
"""Storing and retrieving books from database."""

import sqlite3
from .database_connection import DatabaseConnection


def create_table():
    """Creates books table in the database.
    
    :return: None
    """
    with DatabaseConnection('data.sqlite') as connection:
        cursor = connection.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS books (name text primary key, author text, read integer)'
        )


def add_book(name, author):
    """Add book with name and author to database.
    
    :param name: name of the book
    :type name: str
    
    :param author: author's name
    :type author: str
    
    :return: None
    
    Note:
    To avoid injection attack by using (?, ?),(name, author) syntax,
    instead of ("{name}", "{author}"). For example, if the attacker
    inserts ",0); DROP TABLE books; as the value for 'author' parameter,
    the 'books' table will entirely be deleted.
    """
    with DatabaseConnection('data.sqlite') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute('INSERT INTO books VALUES (?, ?, 0)',
                           (name, author))
        except sqlite3.IntegrityError:
            print('Book already exists!')


def get_all_books():
    """Load all books from the database
    
    Storing fetched data in variable as list comprehension,
    while each row in database is a tuple,
    i.e. [(name, author, read), (name, author, read)...]
    
    :return: list of dictionaries
    :rtype: list
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


def change_to_read(name):
    """Change matched book name to read ('1').
    
    Select all books and set only the matched name
    read value to '1' instead of '0'.

    :parameter name: name of the book
    :type name: str
    
    :return: None
    
    Important:
    Even if you have a single parameters in the query, it must be
    explicitly declared in tuple, otherwise a programmatic error
    will be thrown, i.e. (name, ).
    """
    # TODO: send a message to the user when the book he want to update is not exists.
    with DatabaseConnection('data.sqlite') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read = 1 WHERE name = ?', (name, ))


def remove_book(name):
    """Remove book from the database.
    
    Read all books, rewrite the database without the matched book.
    
    :parameter name: name of the book
    :type name: str
    
    :return: None
    """
    # TODO: send a message to the user when the book he wants to delete is not exists.
    with DatabaseConnection('data.sqlite') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name=?', (name, ))
