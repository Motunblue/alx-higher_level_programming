#!/usr/bin/python3
"""Unittests for rectangle
"""

import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestBase(unittest.TestCase):
    """Unittest for class Rectangle"""

    def test_if_instance_base(self):
        self.assertIsInstance(Rectangle(2, 3), Base)

    def test_with_twoandthree_args(self):
        r1 = Rectangle(12, 13)
        r2 = Rectangle(13, 14, 4)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 13)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r1.id, r2.id - 1)

    def test_with_fourandfive_args(self):
        r1 = Rectangle(6, 7, 8, 9)
        r2 = Rectangle(2, 3, 4, 5, 12)
        self.assertEqual(r1.x, 8)
        self.assertEqual(r2.y, 5)
        self.assertEqual(r2.id, 12)

    def test_string_as_width(self):
        r1 = Rectangle("1", 4)
        self.assertEqual(r1.width, "1")

    def test_string_as_height(self):
        r1 = Rectangle(4, "1")
        self.assertEqual(r1.height, "1")

    def test_x_as_string(self):
        self.assertEqual(Rectangle(2, 3, "4").x, "4")

    def test_y_as_string(self):
        self.assertEqual(Rectangle(2, 3, 4, "5").y, "5")


if __name__ == "__main__":
    unittest.main()
