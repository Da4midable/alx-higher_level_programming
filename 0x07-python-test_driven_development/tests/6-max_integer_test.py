#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_max_integer_unordered(self):
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_max_integer_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_max_integer_negative_numbers(self):
        result = max_integer([-1, -5, -2, -3])
        self.assertEqual(result, -1)

    def test_max_integer_duplicate_max(self):
        result = max_integer([5, 5, 5, 5])
        self.assertEqual(result, 5)

    def test_max_integer_single_element(self):
        result = max_integer([42])
        self.assertEqual(result, 42)

if __name__ == '__main__':
    unittest.main()
