#!./venv/bin/python3.7
# Copyright 2019. Anas Abu Farraj

# yes_votes = 42_572_654
# no_votes = 43_132_459
# percentage_yes_votes = yes_votes / (yes_votes + no_votes)
# percentage_no_votes = no_votes / (yes_votes + no_votes)

# print(f'{yes_votes:,} YES Votes {percentage_yes_votes:.1%}')
# print(f'{no_votes:,} NO Votes {percentage_no_votes:.1%}')
# -------------------------------------------------------

import json

text_data = {
    "name": "hello_jquery",
    "version": "1.0.0",
    "description": "learning jQuery",
    "main": "index.html"
}

# Writing text data to file:
json.dump(text_data,
          open('files/data_dump.json', 'wt'),
          indent=4,
          sort_keys=True)
