#!./venv/bin/python3.7
# Copyright 2019. Anas Abu Farraj
"""Movie Name Manager app

Enter 'a' to add movie, 'l' to list movie, 'f' to find movie, and 'q' to quit.

Tasks:
[x]: Decide where to store movies
[x]: What is the format of a movie?
[x]: Show a user interface and get user input
[x]: Allow user to add movies
[x]: List all movies to user
[ ]: Find a movie
[x]: Allow the user to stop running the program

"""


def menu():
    """Show a user interface and get user input."""

    user_message = "\nEnter 'a' to add movie, " \
                   "'l' to list movie, " \
                   "'f' to find movie, " \
                   "and 'q' to quit: "
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

    print('Listing movies before quitting:')
    list_movie()


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

    for movie in MOVIES:
        print(
            f"{movie['name']} ({movie['year']}) - Director by '{movie['director']}'"
        )

    if not MOVIES:
        print('No stored movies yet')


def find_movie():
    """Finds a movie."""

    keyword = input('Enter the movie detail: ').casefold()
    for movie in MOVIES:
        found = [
            keyword in movie['name'].casefold(),
            keyword in movie['director'].casefold(),
            keyword in movie['year'].casefold()
        ]
        if any(found):
            print(
                f"{movie['name']} ({movie['year']}) - Director by '{movie['director']}'"
            )
    print('Not found')


MOVIES = [{
    'name': 'Harry Potter',
    'director': 'David Fischer',
    'year': '2008'
}, {
    'name': 'The matrix',
    'director': 'Peter David',
    'year': '1998'
}]

if __name__ == '__main__':
    list_movie()
    menu()
