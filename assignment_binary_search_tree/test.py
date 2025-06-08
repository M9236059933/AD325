import unittest
from main import *


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_insert_and_inorder(self):
        values = [5, 3, 7, 2, 4, 6, 8]
        for v in values:
            self.bst.insert(v)
        self.assertEqual(self.bst.inorder_traversal(), sorted(values))

    def test_search(self):
        self.bst.insert(10)
        self.assertTrue(self.bst.search(10))
        self.assertFalse(self.bst.search(99))

    def test_delete_leaf_node(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.delete(5)
        self.assertFalse(self.bst.search(5))

    def test_delete_node_with_one_child(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.delete(5)
        self.assertTrue(self.bst.search(3))
        self.assertFalse(self.bst.search(5))

    def test_delete_node_with_two_children(self):
        for v in [10, 5, 15, 3, 7, 13, 18]:
            self.bst.insert(v)
        self.bst.delete(10)
        self.assertFalse(self.bst.search(10))
        self.assertEqual(self.bst.inorder_traversal(), sorted([5, 3, 7, 15, 13, 18]))