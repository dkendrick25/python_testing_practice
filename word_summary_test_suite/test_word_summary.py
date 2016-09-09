import unittest
from word_summary import word_summary

class TestWordSummary(unittest.TestCase):

    def test_is_count_the_three(self):
        """Does the count of the return 3?"""
        self.assertEqual(word_summary("the cat and the hat and the dog"), {'and': 2, 'cat': 1, 'dog': 1, 'hat': 1, 'the': 3})

    def test_str_count(self):
        self.assertEqual(word_summary("to be or not to be"), {'to': 2, 'be': 2, 'or': 1, 'not': 1})

    #edge case
    def test_empty_str(self):
        self.assertEqual(word_summary(""), {})


if __name__ == '__main__':
    unittest.main()
