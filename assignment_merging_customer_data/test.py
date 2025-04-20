import unittest
from main import merge_customer_data

class TestMergeCustomerData(unittest.TestCase):
    def test_normal_case(self):
        data1 = [101, 104, 107, 0, 0, 0]
        merge_customer_data(data1, 3, [102, 105, 108], 3)
        self.assertEqual(data1, [101, 102, 104, 105, 107, 108])

    def test_data2_empty(self):
        data1 = [103]
        merge_customer_data(data1, 1, [], 0)
        self.assertEqual(data1, [103])

    def test_data1_empty(self):
        data1 = [0]
        merge_customer_data(data1, 0, [101], 1)
        self.assertEqual(data1, [101])

    def test_all_from_data2(self):
        data1 = [0, 0]
        merge_customer_data(data1, 0, [100, 101], 2)
        self.assertEqual(data1, [100, 101])

    def test_duplicates(self):
        data1 = [100, 101, 101, 0, 0]
        merge_customer_data(data1, 3, [101, 102], 2)
        self.assertEqual(data1, [100, 101, 101, 101, 102])