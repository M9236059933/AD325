import unittest
from main import *


class TestStudentRecordManager(unittest.TestCase):

    def test_add_and_retrieve(self):
        manager = StudentRecordManager()
        self.assertTrue(manager.add_student(1, "Test", 3.2))
        self.assertFalse(manager.add_student(1, "Duplicate", 3.5))  # ID already exists

    def test_update_gpa(self):
        manager = StudentRecordManager()
        manager.add_student(2, "Update", 2.0)
        self.assertTrue(manager.update_gpa(2, 3.5))
        self.assertFalse(manager.update_gpa(99, 4.0))  # Non-existent ID

    def test_delete_student(self):
        manager = StudentRecordManager()
        manager.add_student(3, "Delete", 3.0)
        self.assertTrue(manager.delete_student(3))
        self.assertFalse(manager.delete_student(3))  # Already deleted

    def test_display_above_gpa(self):
        manager = StudentRecordManager()
        manager.add_student(4, "Good", 3.5)
        manager.add_student(5, "Average", 2.5)
        # for visual confirmation
        manager.display_above_gpa(3.0)

    def test_display_all_sorted(self):
        manager = StudentRecordManager()
        manager.add_student(20, "Zack", 3.1)
        manager.add_student(10, "Aaron", 3.9)
        # for visual confirmation
        manager.display_all()
