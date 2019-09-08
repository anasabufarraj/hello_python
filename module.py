#!./venv/bin/python3
# # Copyright 2019. Anas Abu Farraj


# class Hello:
def __say_hello__(name):
    """ Say Hello to 'name' """
    print(f'Hello, {name}!')


__name__ = '__module__'

if __name__ == '__module__':
    # True only if the module run as main script.
    print('Hello main script...')