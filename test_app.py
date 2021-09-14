#!./venv/bin/python
# ------------------------------------------------------------------------------
#  Copyright (c) 2019. Anas Abu Farraj
# ------------------------------------------------------------------------------
"""Write all test for app.py in test_app.py"""

import unittest


class TestAddOne(unittest.TestCase):
    def test_that_func_add_one(self):
        from playground import add_one
        self.assertEqual(add_one(4), 5)

    # @unittest.expectedFailure
    def test_that_func_add_one_in_negative(self):
        from playground import add_one
        self.assertEqual(add_one(-4), -3)
