import unittest
from reverse import reverse_string

class TestReverseString(unittest.TestCase):

    def test_is_JavaScript_reversed(self):
        """Did JavaScript reverse correctly"""
        self.assertEqual(reverse_string('JavaScript'), 'tpircSavaJ')

    def test_is_DeeAnn_reversed(self):
        """Did DeeAnn reverse correctly"""
        self.assertEqual(reverse_string('DeeAnn'), 'nnAeeD')
        
if __name__ == '__main__':
    unittest.main()
