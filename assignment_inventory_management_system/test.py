import unittest
from main import duplicate_zeros

class TestDuplicateZeros(unittest.TestCase):
    def test_example_1(self):
        arr = [4,0,1,3,0,2,5,0]
        duplicate_zeros(arr)
        self.assertEqual(arr, [4,0,0,1,3,0,0,2])

    def test_example_2(self):
        arr = [3,2,1]
        duplicate_zeros(arr)
        self.assertEqual(arr, [3,2,1])

    def test_normal_case(self):
        arr = [1,0,2,3,0,4,5,0]
        duplicate_zeros(arr)
        self.assertEqual(arr, [1,0,0,2,3,0,0,4])

    def test_all_zeros(self):
        arr = [0,0,0,0]
        duplicate_zeros(arr)
        self.assertEqual(arr, [0,0,0,0])

    def test_no_zero(self):
        arr = [1,2,3,4]
        duplicate_zeros(arr)
        self.assertEqual(arr, [1,2,3,4])

    def test_zero_at_end(self):
        arr = [1,2,3,0]
        duplicate_zeros(arr)
        self.assertEqual(arr, [1,2,3,0])

if __name__ == "__main__":
    unittest.main()