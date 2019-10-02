#!./venv/bin/python3.7
# Copyright 2019. Anas Abu Farraj
# Learning Python

template = """
From: <{from_email}>
To: <{to_email}>
Subject: {subject}

{message}
"""

print(
    template.format(from_email="sender@domain.com",
                    to_email="recipient@domain.com",
                    subject="Hello!",
                    message="Here's some mail for you. "
                    " Hope you enjoy the message!"))
