#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test with a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        """Test with a list of one element"""
        self.assertEqual(max_integer([10]), 10)

    def test_negative_numbers(self):
        """Test with a list of negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with a list of positive and negative numbers"""
        self.assertEqual(max_integer([-1, 3, -4, 2]), 3)

    def test_floats(self):
        """Test with a list of floats"""
        self.assertEqual(max_integer([1.5, 2.8, 3.3, 0.4]), 3.3)

if __name__ == "__main__":
    unittest.main()
