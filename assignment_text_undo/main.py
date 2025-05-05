class TextOperation:
    def __init__(self, type, char=None):
        self.type = type  # operation type 'add' or 'delete'
        self.char = char  # involved character

class TextEditor:
    def __init__(self):
        self.text = ""
        self.stack = []

    def add(self, char):
        self.text += char
        operation = TextOperation("add", char)
        self.stack.append(operation)
        self.display()

    def delete(self):
        if not self.text:
            return
        deleted_char = self.text[-1]
        self.text = self.text[:-1]
        operation = TextOperation("delete", deleted_char)
        self.stack.append(operation)
        self.display()

    def undo(self):
        if not self.stack:
            return
        last_operation = self.stack.pop()
        if last_operation.type == "add":
            self.text = self.text[:-1]
        elif last_operation.type == "delete":
            self.text += last_operation.char
        self.display()

    def display(self):
        print(f"Current Text: '{self.text}'")