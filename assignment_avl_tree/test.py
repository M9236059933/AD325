import unittest
from main import *

class TestAVLTree(unittest.TestCase):
    def setUp(self):
        self.tree = AVLTree()

    def test_insert_simple(self):
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)
        self.assertEqual(self.tree.inorder_traversal(), [10, 20, 30])

    def test_insert_with_rotation(self):
        self.tree.insert(30)
        self.tree.insert(20)
        self.tree.insert(10)
        self.assertEqual(self.tree.inorder_traversal(), [10, 20, 30])

    def test_search(self):
        self.tree.insert(10)
        self.tree.insert(20)
        self.assertTrue(self.tree.search(10))
        self.assertFalse(self.tree.search(99))

    def test_delete_leaf(self):
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.delete(20)
        self.assertEqual(self.tree.inorder_traversal(), [10])

    def test_delete_with_rotation(self):
        values = [20, 10, 30, 5, 15, 25, 40]
        for v in values:
            self.tree.insert(v)
        self.tree.delete(30)
        self.assertEqual(self.tree.inorder_traversal(), [5, 10, 15, 20, 25, 40])

    def test_duplicate_insert(self):
        self.tree.insert(10)
        self.tree.insert(10)
        self.assertEqual(self.tree.inorder_traversal(), [10])

    def test_delete_nonexistent(self):
        self.tree.insert(10)
        self.tree.delete(99) 
        self.assertEqual(self.tree.inorder_traversal(), [10])

