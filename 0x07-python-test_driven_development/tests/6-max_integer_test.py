#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test max interger"""

    def test_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)
        self.assertEqual(max_integer([1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([1]), 1)

    def test_negatives(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)


if __name__ == "__main__":
    unittest.main()
