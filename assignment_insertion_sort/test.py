import unittest
from main import insertion_sort

class TestInsertionSort(unittest.TestCase):

    def test_random_array(self):
        arr = [64, 25, 12, 22, 11]
        insertion_sort(arr)
        self.assertEqual(arr, [11, 12, 22, 25, 64])

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_descending_array(self):
        arr = [5, 4, 3, 2, 1]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_same_elements(self):
        arr = [7, 7, 7, 7, 7]
        insertion_sort(arr)
        self.assertEqual(arr, [7, 7, 7, 7, 7])

    def test_empty_array(self):
        arr = []
        insertion_sort(arr)
        self.assertEqual(arr, [])

    def test_single_element(self):
        arr = [42]
        insertion_sort(arr)
        self.assertEqual(arr, [42])

