import unittest
from main import *


class TestBinaryTreeFunctions(unittest.TestCase):
    def setUp(self):
        self.pre = ['A', 'B', 'D', 'E', 'C', 'F']
        self.ino = ['D', 'B', 'E', 'A', 'C', 'F']
        self.root = build_tree_from_pre_in(self.pre, self.ino)

    def test_preorder(self):
        self.assertEqual(preorder_traversal(self.root), self.pre)

    def test_inorder(self):
        self.assertEqual(inorder_traversal(self.root), self.ino)

    def test_postorder(self):
        self.assertEqual(postorder_traversal(self.root), ['D', 'E', 'B', 'F', 'C', 'A'])

    def test_level_order(self):
        self.assertEqual(level_order_traversal(self.root), ['A', 'B', 'C', 'D', 'E', 'F'])

    def test_empty_tree(self):
        self.assertEqual(preorder_traversal(None), [])
        self.assertEqual(inorder_traversal(None), [])
        self.assertEqual(postorder_traversal(None), [])
        self.assertEqual(level_order_traversal(None), [])

    def test_left_skewed_tree(self):
        pre = ['A', 'B', 'C', 'D']
        ino = ['D', 'C', 'B', 'A']
        root = build_tree_from_pre_in(pre, ino)
        self.assertEqual(preorder_traversal(root), pre)
        self.assertEqual(inorder_traversal(root), ino)
        self.assertEqual(postorder_traversal(root), ['D', 'C', 'B', 'A'])
        self.assertEqual(level_order_traversal(root), ['A', 'B', 'C', 'D'])

    def test_right_skewed_tree(self):
        pre = ['A', 'B', 'C', 'D']
        ino = ['A', 'B', 'C', 'D']
        root = build_tree_from_pre_in(pre, ino)
        self.assertEqual(preorder_traversal(root), pre)
        self.assertEqual(inorder_traversal(root), ino)
        self.assertEqual(postorder_traversal(root), ['D', 'C', 'B', 'A'])
        self.assertEqual(level_order_traversal(root), ['A', 'B', 'C', 'D'])

    def test_complex_tree(self):
        pre = ['M', 'B', 'A', 'C', 'Q', 'P', 'Z']
        ino = ['A', 'B', 'C', 'M', 'P', 'Q', 'Z']
        root = build_tree_from_pre_in(pre, ino)
        self.assertEqual(preorder_traversal(root), pre)
        self.assertEqual(inorder_traversal(root), ino)
        self.assertEqual(postorder_traversal(root), ['A', 'C', 'B', 'P', 'Z', 'Q', 'M'])
        self.assertEqual(level_order_traversal(root), ['M', 'B', 'Q', 'A', 'C', 'P', 'Z'])

    def test_manual_structure_check(self):
        print("\nManual structure check:\n")
        print_tree(self.root)
        self.assertEqual(self.root.val, 'A')
        self.assertEqual(self.root.left.val, 'B')
        self.assertEqual(self.root.right.val, 'C')
        self.assertEqual(self.root.left.left.val, 'D')
        self.assertEqual(self.root.left.right.val, 'E')
        self.assertEqual(self.root.right.right.val, 'F')