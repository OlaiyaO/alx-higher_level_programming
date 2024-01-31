#!/usr/bin/python3
"""Unittests for my_max_integer([..])."""

import unittest
from 6-max_integer import max_integer as my_max_integer

class TestMyMaxInteger(unittest.TestCase):
    """Define unittests for my_max_integer([..])."""

    def test_sorted_list(self):
        """Test a sorted list of integers."""
        sorted_list = [1, 2, 3, 4]
        self.assertEqual(my_max_integer(sorted_list), 4)

    def test_unsorted_list(self):
        """Test an unsorted list of integers."""
        unsorted_list = [1, 2, 4, 3]
        self.assertEqual(my_max_integer(unsorted_list), 4)

    def test_max_at_the_beginning(self):
        """Test a list with a maximum value at the beginning."""
        max_at_the_beginning = [4, 3, 2, 1]
        self.assertEqual(my_max_integer(max_at_the_beginning), 4)

    def test_empty_input(self):
        """Test an empty input list."""
        empty_input = []
        self.assertEqual(my_max_integer(empty_input), None)

    def test_single_element_list(self):
        """Test a list with a single element."""
        single_element_list = [7]
        self.assertEqual(my_max_integer(single_element_list), 7)

    def test_float_values(self):
        """Test a list of floating-point values."""
        float_values = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(my_max_integer(float_values), 15.2)

    def test_mixed_ints_and_floats(self):
        """Test a list of mixed integers and floats."""
        mixed_ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(my_max_integer(mixed_ints_and_floats), 15.5)

    def test_string_input(self):
        """Test a string as input."""
        string_input = "Brennan"
        self.assertEqual(my_max_integer(string_input), 'n')

    def test_list_of_strings(self):
        """Test a list of strings."""
        list_of_strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(my_max_integer(list_of_strings), "name")

    def test_empty_string_input(self):
        """Test an empty string as input."""
        self.assertEqual(my_max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
