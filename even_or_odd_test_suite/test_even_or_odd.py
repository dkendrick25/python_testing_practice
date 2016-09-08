import unittest
from even_or_odd import is_even
from even_or_odd import is_odd
from even_or_odd import even_or_odd

class isEvenTestCase(unittest.TestCase):

    def test_is_two_even(self):
        """Is 2 successfully determined True?"""
        self.assertTrue(is_even(2))

    def test_is_three_even(self):
        """Is 3 successfully determined False?"""
        self.assertFalse(is_even(3))


class isOddTestCase(unittest.TestCase):

    def test_is_three_odd(self):
        """Is 3 successfully True?"""
        self.assertTrue(is_odd(3))

    def test_is_two_odd(self):
        """Is 2 successfully False"""
        self.assertFalse(is_odd(2))


class EvenOrOddTestCase(unittest.TestCase):

    def test_is_ten_even(self):
        """is 10 successfully even?"""
        self.assertEqual(even_or_odd(10), "even")

    def test_is_eleven_odd(self):
        """is 11 successfully odd?"""
        self.assertEqual(even_or_odd(11), "odd")

if __name__ == '__main__':
    unittest.main()
