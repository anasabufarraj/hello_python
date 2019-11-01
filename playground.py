#!./venv/bin/python3.7
# Copyright 2019. Anas Abu Farraj
# Learning Python

from collections import ChainMap

baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}

print(list(ChainMap(adjustments, baseline)))
