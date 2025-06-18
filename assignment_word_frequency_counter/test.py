import unittest
from main import * 


class TestWordFrequencyCounter(unittest.TestCase):

    def test_normal_sentence(self):
        input_text = "Hello world hello"
        result = count_word_frequency(input_text)
        self.assertEqual(result.get("hello"), 2)
        self.assertEqual(result.get("world"), 1)

    def test_with_punctuation(self):
        input_text = "Hi, hi! Hello."
        result = count_word_frequency(input_text)
        self.assertEqual(result.get("hi"), 2)
        self.assertEqual(result.get("hello"), 1)

    def test_case_insensitive(self):
        input_text = "Apple apple APPLE"
        result = count_word_frequency(input_text)
        self.assertEqual(result.get("apple"), 3)

    def test_empty_string(self):
        input_text = ""
        result = count_word_frequency(input_text)
        self.assertTrue(len(result) == 0)

    def test_only_spaces(self):
        input_text = "     "
        result = count_word_frequency(input_text)
        self.assertTrue(len(result) == 0)

    def test_single_word(self):
        input_text = "Java"
        result = count_word_frequency(input_text)
        self.assertEqual(result.get("java"), 1)
