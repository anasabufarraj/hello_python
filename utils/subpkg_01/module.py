#!./venv/bin/python3
# # Copyright 2019. Anas Abu Farraj


def say_hello(name='there'):
    """ Say Hello to 'name' """
    print(f'Hello, {name}!')


if __name__ == '__main__':
    # True only if the module run as main script.
    print('Hello main script...')
