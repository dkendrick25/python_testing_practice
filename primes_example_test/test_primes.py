import unittest
from primes import is_prime

class PrimesTestCase(unittest.TestCase):
    """Tests for 'primes.py'."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

    def test_is_four_non_prime(self):
        """Is four correctly determined not to be prime?"""
        self.assertFalse(is_prime(4), msg='Four is not Prime!')

    #edge cases
    def test_is_zero_not_prime(self):
        """Is zero correctly determined not to be prime?"""
        self.assertFalse(is_prime(0))

    def test_negative_number(self):
        """Is a negative number correctly determined not to be prime?"""
        for index in range(-1, -10, -1):
            self.assertFalse(is_prime(index), msg='{} should not be determined to be prime'.format(index))

    #equivilant test for above version
    # def test_negative_number(self):
    # """Is a negative number correctly determined not to be prime?"""
    # self.assertFalse(is_prime(-1))
    # self.assertFalse(is_prime(-2))
    # self.assertFalse(is_prime(-3))
    # self.assertFalse(is_prime(-4))
    # self.assertFalse(is_prime(-5))
    # self.assertFalse(is_prime(-6))
    # self.assertFalse(is_prime(-7))
    # self.assertFalse(is_prime(-8))
    # self.assertFalse(is_prime(-9))

if __name__ == '__main__':
    unittest.main()
