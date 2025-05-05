import unittest
from main import TextEditor

class TestTextEditor(unittest.TestCase):
    def test_add_and_undo(self):
        editor = TextEditor()
        editor.add('a')
        editor.add('b')
        self.assertEqual(editor.text, 'ab')
        editor.undo()
        self.assertEqual(editor.text, 'a')

    def test_delete_and_undo(self):
        editor = TextEditor()
        editor.add('x')
        editor.delete()
        self.assertEqual(editor.text, '')
        editor.undo()
        self.assertEqual(editor.text, 'x')

    def test_multiple_undos(self):
        editor = TextEditor()
        editor.add('a')
        editor.add('b')
        editor.delete()
        editor.undo()
        editor.undo()
        self.assertEqual(editor.text, 'a')

    def test_edge_undo_on_empty_stack(self):
        editor = TextEditor()
        editor.undo()
        self.assertEqual(editor.text, '')

    def test_delete_on_empty_text(self):
        editor = TextEditor()
        editor.delete()
        self.assertEqual(editor.text, '')