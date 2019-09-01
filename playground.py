#!./venv/bin/python3.7
# Copyright 2019. Anas Abu Farraj

is_designer = True
is_developer = False
is_learner = True

# Accept the guy if designer and developer, or a lerner.
is_accepted = is_designer and is_developer or is_learner

print(is_accepted)  # True


# ---------------------------------------------------------
def length(n):
    return len(n)


items = 'apple', 'orange', 'pear', 'orange', 'banana'
length_list = list(x for x in map(length, items))

print(length_list)  # [5, 6, 4, 6, 6]
