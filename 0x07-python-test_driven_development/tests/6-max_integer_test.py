#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_cases(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -2]), -1)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, 2.5, -3, 4.5]), 4.5)

if __name__ == "__main__":
    unittest.main()
