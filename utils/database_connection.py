#!./venv/bin/python
# utils/database_connection.py
# ------------------------------------------------------------------------------
#  Copyright (c) 2019. Anas Abu Farraj
# ------------------------------------------------------------------------------
"""A context manager to handle database connection."""

import sqlite3


class DatabaseConnection:
    def __init__(self, host) -> None:
        self._host = host
        self._connection = sqlite3.connect('data.sqlite')

    def __enter__(self) -> sqlite3.Connection:
        """Enter point: remains a connection with database while managing."""
        return self._connection

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit point: commit and disconnect with database.
        
        If any type exception, value exception, or traceback exception happen,
        the connection to the database will close. Otherwise, it will commit
        and close.
        """
        if exc_type or exc_val or exc_tb:
            self._connection.close()
        else:
            self._connection.commit()
            self._connection.close()
