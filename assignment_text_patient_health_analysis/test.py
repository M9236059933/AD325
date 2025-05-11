import unittest
from main import HealthNode, isHealthRecordSymmetric

def build_linked_list(values):
    if not values:
        return None
    head = HealthNode(values[0])
    current = head
    for v in values[1:]:
        current.next = HealthNode(v)
        current = current.next
    return head

class TestHealthRecordSymmetry(unittest.TestCase):
    # Normal cases
    def test_symmetric_even(self):
        head = build_linked_list([70, 80, 80, 70])
        self.assertTrue(isHealthRecordSymmetric(head))

    def test_symmetric_odd(self):
        head = build_linked_list([60, 75, 60])
        self.assertTrue(isHealthRecordSymmetric(head))

    def test_not_symmetric(self):
        head = build_linked_list([90, 100, 110])
        self.assertFalse(isHealthRecordSymmetric(head))

    # Edge cases
    def test_empty_list(self):
        self.assertTrue(isHealthRecordSymmetric(None))

    def test_single_node(self):
        head = build_linked_list([100])
        self.assertTrue(isHealthRecordSymmetric(head))

    def test_two_nodes_not_equal(self):
        head = build_linked_list([100, 90])
        self.assertFalse(isHealthRecordSymmetric(head))

if __name__ == "__main__":
    unittest.main()