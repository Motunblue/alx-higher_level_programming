#!/usr/bin/python3
"""Unittests for base.py
"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Unittest for class base"""

    def test_without_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_with_args(self):
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

if __name__ == "__main__":
    unittest.main()
