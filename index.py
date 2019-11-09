#!./venv/bin/python3.7
# Copyright 2019. Anas Abu Farraj
# Learning BeautifulSoup

from bs4 import BeautifulSoup

index = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>This is Title</title>
  </head>
  <body>
    <h1>Items List</h1>
    <p class="subtitle">Subtitle</p>
    <ul class="items_list">
      <li>Item 1</li>
      <li>Item 2</li>
      <li>Item 3</li>
      <li>Item 4</li>
      <li>Item 5</li>
    </ul>
    <p>Note: this is a note.</p>
  </body>
</html>
'''

soup = BeautifulSoup(index, 'html.parser')

list_items = soup.find('ul')

print(list_items.attrs['class'])
