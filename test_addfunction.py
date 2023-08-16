import unittest
from addfunction import add

class addTest(unittest.TestCase):

    def test_two_nums(self):
        result = add(1,2)
        self.assertEqual(result,3)

    def test_three_nums(self):
        result = add(1,2,4)
        self.assertEqual(result,7)

if __name__ == '__main__':
    unittest.main()