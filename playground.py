#!./venv/bin/python3.7
# Copyright 2019. Anas Abu Farraj

# is_designer = True
# is_developer = False
# is_learner = True

# # Accept the guy if he designer and developer, or a lerner.
# is_accepted = is_designer and is_developer or is_learner

# print(is_accepted)  # True

from collections import deque

queue = deque(['Eric', 'John', 'Michael'])
queue.append('Terry')  # Terry arrives
queue.append('Graham')  # Graham arrives

print(queue.popleft())  # 'Eric' first to arrive now leaves
print(queue.popleft())  # 'John' second to arrive now leaves

print(queue)  # deque(['Michael', 'Terry', 'Graham'])
