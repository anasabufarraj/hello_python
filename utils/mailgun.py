#!./venv/bin/python3.7
# utils/mailgun.py
# ------------------------------------------------------------------------------
#  Copyright (c) 2019. Anas Abu Farraj
# ------------------------------------------------------------------------------
"""A class to send em-mails suing Mailgun."""

import requests


class Mailgun:
    """Sending e-mails using Mailgun."""
    API_URL = 'api_url'
    API_KEY = 'api_key'

    FROM_NAME = 'from_name'
    FROM_EMAIL = 'from_e-mail'

    @classmethod
    def send_emails(cls,
                    to_emails,
                    subject,
                    content,
                    from_name=FROM_NAME,
                    from_email=FROM_EMAIL):

        requests.post(cls.API_URL,
                      auth=('api', cls.API_KEY),
                      data={
                          'from': f'{from_name} <{from_email}>',
                          'to': to_emails,
                          'subject': subject,
                          'content': content
                      })
