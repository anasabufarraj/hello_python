"""Write all test for app.py in test_app.py"""
import unittest
from playground import add_one


class TestAddOne(unittest.TestCase):
    def test_that_func_add_one(self):
        self.assertEqual(add_one(4), 5)

    # @unittest.expectedFailure
    def test_that_func_add_one_in_negative(self):
        self.assertEqual(add_one(-4), -3)


if __name__ == '__main__':
    unittest.main()
