import unittest
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_is_three_fizz(self):
        """given 3 does fizz print?"""
        self.assertEqual(fizzbuzz(3), "fizz")

    def test_is_five_buzz(self):
        """given 5 does buzz print?"""
        self.assertEqual(fizzbuzz(5), "buzz")

    def test_is_fifteen_fizzubzz(self):
        """given 15 does fizzbuzz print?"""
        self.assertEqual(fizzbuzz(15), "fizzbuzz")

    def test_is_four_print_four(self):
        """given 4 does 4 print?"""
        self.assertEqual(fizzbuzz(12), 12)

if __name__ == '__main__':
    unittest.main()
