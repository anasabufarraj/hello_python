#!./venv/bin/python3.7
# Copyright 2019. Anas Abu Farraj
# Learning Python

users = {1: "Alice", 2: "Bob", 3: "Dilbert"}

print(f"Hi {users.get(1, 'there')}!")  # Hi Alice!
print(f"Hi {users.get(4, 'there')}!")  # Hi there!
