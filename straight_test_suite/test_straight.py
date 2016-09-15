import unittest
from is_straight import is_straight


class TestIsStraight(unittest.TestCase):

    def test_ordered_straight_true(self):
        '''ordered straight should return True'''
        self.assertTrue(is_straight([1,2,3,4,5,6,7]))

    def test_is_straight_false(self):
        '''not a straight should return false'''
        self.assertFalse(is_straight([1,9,2,6,3,10,4]))

    def test_unordered_straight_true(self):
        '''unordered straight should return True'''
        self.assertTrue(is_straight([6,3,7,4,2,1,5]))

    def test_repeated_cards_true(self):
        '''repeated cards can still return True straight'''
        self.assertTrue(is_straight([1,3,4,1,1,2,5]))

#edge case
    def test_not_enough_cards(self):
        '''not enough cards given for a straight should be false'''
        self.assertFalse(is_straight([4,2,1,3]))

    def test_empty_list(self):
        '''empty list should return false'''
        self.assertFalse(is_straight([]))

if __name__ == '__main__':
    unittest.main()
