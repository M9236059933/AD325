import unittest
from main import *

class TestDecisionTreeDepth(unittest.TestCase):

    def test_real_questions_full_tree(self):
        root = Node("Do you want to grow your savings?")
        root.left = Node("Are you under 60?")
        root.right = Node("Do you need money urgently?")
        
        root.left.left = Node("Retirement Investment")
        root.left.right = Node("Savings Account")
        
        root.right.left = Node("Loan Approved?")
        root.right.right = Node("Job secured?")
        
        root.right.left.left = Node("Personal Loan")
        root.right.right.right = Node("Short-Term Loan")
        
        # Max path: root - right - left - left = depth 4
        self.assertEqual(max_depth(root), 4)

    def test_real_questions_short_tree(self):
        root = Node("Do you own a house?")
        root.left = Node("Apply for Home Equity Loan")
        root.right = Node("Check Rental Assistance")
        self.assertEqual(max_depth(root), 2)

    def test_single_question(self):
        root = Node("Do you have existing debt?")
        self.assertEqual(max_depth(root), 1)

    def test_empty_tree(self):
        self.assertEqual(max_depth(None), 0)

    def test_left_heavy_realistic(self):
        root = Node("Are you self-employed?")
        root.left = Node("Do you file taxes annually?")
        root.left.left = Node("You qualify for Self-Employed IRA")
        self.assertEqual(max_depth(root), 3)