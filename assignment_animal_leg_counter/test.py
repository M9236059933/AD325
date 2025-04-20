import unittest
from main import count_four_legged

class TestCountFourLegged(unittest.TestCase):
    def test_normal_cases(self):
        self.assertEqual(count_four_legged(['lion', 'monkey', 'deer', 'snake', 'elephant']), 3)
        self.assertEqual(count_four_legged(['frog', 'horse', 'spider', 'ant']), 1)
        self.assertEqual(count_four_legged(['dog', 'cat', 'horse', 'dog']), 4)

    def test_edge_cases(self):
        self.assertEqual(count_four_legged([]), 0)  # Empty list
        self.assertEqual(count_four_legged(['raptor']), 0)  # Unknown animal
        self.assertEqual(count_four_legged(['LION', 'Lion', 'lion']), 3)  # Case-insensitive
        
