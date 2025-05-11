import unittest
from main import PatientNode, merge_patient_lists

def build_list(records):
    if not records:
        return None
    head = PatientNode(*records[0])
    current = head
    for r in records[1:]:
        current.next = PatientNode(*r)
        current = current.next
    return head

def list_to_array(head):
    result = []
    while head:
        result.append((head.ssn, head.name, head.age))
        head = head.next
    return result

class TestMergePatients(unittest.TestCase):

    # Normal test cases
    def test_merge_sorted_lists(self):
        a = build_list([(111, "A", 30), (222, "C", 45)])
        b = build_list([(123, "B", 40), (250, "D", 60)])
        result = merge_patient_lists(a, b)
        self.assertEqual(list_to_array(result), [
            (111, "A", 30),
            (123, "B", 40),
            (222, "C", 45),
            (250, "D", 60),
        ])

    def test_merge_with_duplicates(self):
        a = build_list([(111, "A", 30), (222, "C", 45)])
        b = build_list([(111, "B", 40), (222, "D", 50)])
        result = merge_patient_lists(a, b)
        self.assertEqual(list_to_array(result), [
            (111, "A", 30),
            (111, "B", 40),
            (222, "C", 45),
            (222, "D", 50),
        ])

    def test_merge_alternating(self):
        a = build_list([(100, "A", 20), (200, "C", 40)])
        b = build_list([(150, "B", 30), (250, "D", 50)])
        result = merge_patient_lists(a, b)
        self.assertEqual(list_to_array(result), [
            (100, "A", 20),
            (150, "B", 30),
            (200, "C", 40),
            (250, "D", 50),
        ])

    # Edge test cases
    def test_merge_with_empty_a(self):
        a = None
        b = build_list([(123, "B", 40)])
        result = merge_patient_lists(a, b)
        self.assertEqual(list_to_array(result), [(123, "B", 40)])

    def test_merge_with_empty_b(self):
        a = build_list([(123, "B", 40)])
        b = None
        result = merge_patient_lists(a, b)
        self.assertEqual(list_to_array(result), [(123, "B", 40)])

    def test_merge_both_empty(self):
        result = merge_patient_lists(None, None)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()