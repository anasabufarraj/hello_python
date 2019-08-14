#!./venv/bin/python3.7
# Copyright 2019. Anas Abu Farraj


class BaseClass:
    def __init__(self, company='Some', made='Car!'):
        self._company = company
        self._made = made

    def company(self):
        return self._company

    def made(self):
        return self._made


class ChildClass(BaseClass):
    pass


car = ChildClass('BMW', '2002')

print(car.company(), car.made())
