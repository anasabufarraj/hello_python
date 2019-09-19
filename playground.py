#!./venv/bin/python3.7
# Copyright 2019. Anas Abu Farraj

from string import Template

t = Template('${sender} send ${amount} to ${reciever}')

print(t.substitute(sender='Jonny', amount='$40', reciever='Peter'))

# Jonny send $40 to Peter