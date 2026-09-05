import unittest

from calculator import add
from calculator import divide
from calculator import multiply
from calculator import subtract


class TestCalculator(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(10, 5), 15)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-10, -5), -15)

    def test_subtract_numbers(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply_numbers(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(10, 0), 0)

    def test_divide_numbers(self):
        self.assertEqual(divide(10, 5), 2)

    def test_divide_decimal_numbers(self):
        self.assertEqual(divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()