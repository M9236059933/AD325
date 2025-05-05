import unittest
from main import sortedSquares

class TestSortedSquares(unittest.TestCase):
    def test_normal_cases(self):
        self.assertEqual(sortedSquares([-5, -2, 0, 3, 10]), [0, 4, 9, 25, 100])
        self.assertEqual(sortedSquares([-8, -3, 2, 4, 12]), [4, 9, 16, 64, 144])
        self.assertEqual(sortedSquares([-3, -1, 1, 2]), [1, 1, 4, 9])

    def test_edge_cases(self):
        self.assertEqual(sortedSquares([-1]), [1])
        self.assertEqual(sortedSquares([3]), [9])
        self.assertEqual(sortedSquares([-7, -6, -5]), [25, 36, 49])

if __name__ == "__main__":
    unittest.main()