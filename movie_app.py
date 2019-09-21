#!./venv/bin/python3.7
# Copyright 2019. Anas Abu Farraj
"""Movie Name Manager app

Enter 'a' to add movie, 'l' to list movie, 'f' to find movie, and 'q' to quit.

Tasks:
[x]: Decide where to store movies
[x ]: What is the format of a movie?
[x]: Show a user interface and get user input
[ ]: Allow user to add movies
[ ]: List all movies to user
[ ]: Find a movie
[x]: Allow the user to stop running the program

"""


def menu():
    """Show a user interface and get user input."""

    user_message = "Enter 'a' to add movie, 'l' to list movie, 'f' to find movie, and 'q' to quit: "
    user_input = input(user_message)

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            list_movie()
        elif user_input == 'f':
            find_movie()
        else:
            print('Unknown command, please try again')

        user_input = input(user_message)

    print('Quitting...')


def add_movie():
    """Add a movie to a list"""
    movie_name = input('Enter movie name: ')
    movie_director = input('Enter director: ')
    movie_year = input('Enter movie year: ')

    MOVIES.append({
        'name': movie_name,
        'director': movie_director,
        'year': movie_year
    })


def list_movie():
    """List all stored movies in the list."""
    for item in MOVIES:
        print(item)
    if not MOVIES:
        print('No movies stored..')


def find_movie():
    """Finds a movie."""


MOVIES = []
"""
movie = {
    name: (str),
    year: (int)
}
"""

if __name__ == '__main__':
    menu()
